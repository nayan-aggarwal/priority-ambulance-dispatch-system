"""Streamlit interface for the Priority Ambulance Dispatch educational demo."""

from datetime import datetime, timezone
import uuid

import streamlit as st

from src.dispatch.allocator import dispatch_waiting_cases
from src.triage.rules import classify_case

st.set_page_config(page_title="Priority Ambulance Dispatch", page_icon="🚑", layout="wide")

st.title("🚑 Priority Ambulance Dispatch System")
st.caption("Student prototype · simulated cases and ambulance fleet")
st.warning(
    "Educational demo only — rules are not clinically validated. Do not use this app "
    "for real diagnosis, triage, or ambulance dispatch. Do not enter real patient data. "
    "In an actual emergency, contact local emergency services."
)

if "cases" not in st.session_state:
    st.session_state.cases = []
if "ambulances" not in st.session_state:
    # Fictional sample coordinates around central New Delhi for software testing only.
    st.session_state.ambulances = [
        {"ambulance_id": "AMB-101", "latitude": 28.6139, "longitude": 77.2090, "status": "AVAILABLE", "assigned_incident_id": "—"},
        {"ambulance_id": "AMB-102", "latitude": 28.6200, "longitude": 77.2150, "status": "AVAILABLE", "assigned_incident_id": "—"},
        {"ambulance_id": "AMB-103", "latitude": 28.6000, "longitude": 77.1900, "status": "AVAILABLE", "assigned_incident_id": "—"},
    ]

symptom_options = [
    "Chest pain",
    "Severe difficulty breathing",
    "Loss of consciousness",
    "Uncontrolled bleeding",
    "Severe burn",
    "Stroke-like symptoms",
    "Fracture",
    "Moderate asthma symptoms",
    "High fever with complications",
    "Severe pain",
    "Minor cut",
    "Minor sprain",
    "Mild stomach ache",
    "Not sure / other concerning symptom",
]

report_tab, dispatch_tab = st.tabs(["Report a demo case", "Dispatch desk"])

with report_tab:
    st.subheader("Patient / bystander intake")
    st.write("Use fictional details and sample coordinates only.")
    with st.form("patient_intake", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            patient_name = st.text_input("Demo patient name or label", placeholder="Example: Demo Case A")
            age = st.number_input("Age", min_value=0, max_value=120, value=25, step=1)
            contact = st.text_input("Demo contact label (optional)", placeholder="Do not enter a real phone number")
            pain_level = st.slider("Reported pain scale (demo input)", min_value=1, max_value=10, value=5)
        with col2:
            latitude = st.number_input("Latitude (example only)", min_value=-90.0, max_value=90.0, value=28.6139, format="%.6f")
            longitude = st.number_input("Longitude (example only)", min_value=-180.0, max_value=180.0, value=77.2090, format="%.6f")
            heart_rate = st.number_input("Heart rate, if known (optional)", min_value=0, max_value=300, value=0, step=1)
            spo2 = st.number_input("SpO₂ %, if known (optional; 0 = not entered)", min_value=0, max_value=100, value=0, step=1)
        symptoms = st.multiselect("Select reported symptoms", symptom_options, default=["Not sure / other concerning symptom"])
        submitted = st.form_submit_button("Add case to demo queue", type="primary")

    if submitted:
        if not symptoms:
            st.error("Select at least one symptom for this demo case.")
        else:
            triage = classify_case(symptoms, pain_level)
            incident_id = f"CASE-{uuid.uuid4().hex[:6].upper()}"
            case = {
                "incident_id": incident_id,
                "patient_label": patient_name.strip() or "Demo patient",
                "age": int(age),
                "contact_label": contact.strip() or "Not provided",
                "latitude": float(latitude),
                "longitude": float(longitude),
                "symptoms": ", ".join(symptoms),
                "pain_level": int(pain_level),
                "heart_rate": int(heart_rate) if heart_rate else None,
                "spo2": int(spo2) if spo2 else None,
                **triage,
                "status": "WAITING",
                "ambulance_id": "—",
                "assigned_distance_km": None,
                "created_at": datetime.now(timezone.utc).isoformat(),
            }
            st.session_state.cases.append(case)
            st.success(f"Demo case {incident_id} added to the queue. Category: {triage['triage_level']}.")
            st.caption("The category comes from illustrative coding rules, not a validated medical assessment.")

with dispatch_tab:
    st.subheader("Queue and fleet status")
    cases = st.session_state.cases
    ambulances = st.session_state.ambulances
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Waiting cases", sum(c["status"] == "WAITING" for c in cases))
    m2.metric("Dispatched cases", sum(c["status"] == "DISPATCHED" for c in cases))
    m3.metric("Available demo ambulances", sum(a["status"] == "AVAILABLE" for a in ambulances))
    m4.metric("Ambulances on mission", sum(a["status"] == "ON_MISSION" for a in ambulances))

    if st.button("Run simulated dispatch", type="primary", disabled=not any(c["status"] == "WAITING" for c in cases)):
        new_cases, new_ambulances = dispatch_waiting_cases(cases, ambulances)
        st.session_state.cases = new_cases
        st.session_state.ambulances = new_ambulances
        st.success("Simulation complete. This action affects only the demo data in this browser session.")
        st.rerun()

    if cases:
        st.markdown("#### Emergency queue")
        display_cases = []
        for c in cases:
            display_cases.append({
                "Case ID": c["incident_id"],
                "Patient label": c["patient_label"],
                "Category": c["triage_level"],
                "Demo score": c["priority_score"],
                "Symptoms": c["symptoms"],
                "Status": c["status"],
                "Ambulance": c["ambulance_id"],
                "Distance (km)": c["assigned_distance_km"] if c["assigned_distance_km"] is not None else "—",
            })
        st.dataframe(display_cases, use_container_width=True, hide_index=True)
    else:
        st.info("No demo cases yet. Add a case in the first tab to populate the queue.")

    st.markdown("#### Demo ambulance fleet")
    st.dataframe([
        {"Ambulance": a["ambulance_id"], "Status": a["status"], "Assigned case": a.get("assigned_incident_id", "—"), "Latitude": a["latitude"], "Longitude": a["longitude"]}
        for a in ambulances
    ], use_container_width=True, hide_index=True)

st.divider()
st.caption("Prototype status: initial educational MVP. Data is stored only in Streamlit session memory and may disappear when the session restarts.")
