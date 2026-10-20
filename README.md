# Priority Ambulance Dispatch System

An educational prototype for recording emergency requests, assigning a demo triage category, and simulating priority-based ambulance allocation.

> **Safety notice:** This is a student/demo project only. Its rules are illustrative and are not clinically validated. Do not use it to diagnose patients, decide real-world medical urgency, or dispatch real ambulances. In a real emergency, contact the local emergency service immediately and follow qualified professionals' instructions.

## Problem statement

A first-come, first-served approach may not reflect the urgency of different emergencies. This project explores a workflow where reported symptoms are checked against simple demonstration rules, cases are placed in a priority queue, and the nearest available demo ambulance is assigned to the highest-priority waiting case.

## Current prototype includes

- A Streamlit patient/bystander form.
- Illustrative Red / Yellow / Green rules (not a medical model).
- A demo dispatch queue ordered by category, demonstration score, and waiting time.
- Haversine distance calculation to compare ambulance coordinates.
- A dispatch dashboard showing case and ambulance status.
- Fictional sample ambulance coordinates for demonstration.

## Tech stack

- Python 3.10+
- Streamlit for the web interface
- Python standard library (`math`, `datetime`, `unittest`)

The first version uses in-memory session data; records are not stored permanently. SQLite, a properly sourced/labelled ML model, maps, authentication, and operational integrations are future work.

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this repository folder.
3. Create and activate a virtual environment (recommended):

   **Windows**
   ```bash
   py -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS / Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the demo:
   ```bash
   streamlit run app.py
   ```

Streamlit will print a local URL, usually `http://localhost:8501`.

## Repository structure

```text
priority-ambulance-dispatch-system/
├── app.py                      # Streamlit demo UI
├── requirements.txt
├── .gitignore
├── README.md
├── docs/
│   └── project-design.pdf      # Original design brief
├── src/
│   ├── triage/
│   │   └── rules.py             # Illustrative triage rules
│   └── dispatch/
│       └── allocator.py         # Queue ordering and distance-based allocation
└── tests/
    └── test_dispatch.py
```

## Workflow

1. A user enters demo patient details, symptoms, pain level, and example coordinates.
2. The rule module assigns an illustrative category.
3. The dispatch desk orders waiting cases by Red > Yellow > Green, then demo score and waiting time.
4. Each waiting case is assigned the nearest ambulance whose status is `AVAILABLE`, until no available ambulance remains.
5. Assigned ambulances change to `ON_MISSION`; cases change to `DISPATCHED`.

## Testing

Run the unit tests from the repository root:

```bash
python -m unittest discover -s tests -v
```

## Roadmap

- [ ] Persist cases and fleet status in SQLite.
- [ ] Add input validation and automated tests for more dispatch scenarios.
- [ ] Design a role-based dispatcher workflow.
- [ ] Investigate appropriately governed, validated data before any ML experiment.
- [ ] Add map visualisation using clearly labelled demo data.
- [ ] Conduct clinical, privacy, security, and operational review before any real-world use.

## Project status

**Initial educational prototype / under development.** The attached PDF is the source design brief; the current code is a simple demonstration and does not implement a validated AI/ML diagnostic model.
