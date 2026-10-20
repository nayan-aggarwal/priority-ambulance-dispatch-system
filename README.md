# Priority Ambulance Dispatch System

## Project overview

This repository documents the design of a priority-based ambulance dispatch system. The idea is to help dispatch teams review emergency requests by medical urgency and then consider the location and availability of ambulances.

## Problem statement

A first-come, first-served process may not always put the most urgent emergency first. The proposed system is intended to organise incoming requests by priority so that critical cases can be reviewed first.

## Proposed workflow

1. A patient or bystander submits basic patient details, symptoms, available vital signs, and location.
2. A triage component evaluates the reported information and labels the case Red (critical), Yellow (urgent), or Green (non-urgent).
3. A dispatch component considers priority, severity, waiting time, and the proximity of available ambulances.
4. A dashboard presents emergency requests and ambulance statuses to dispatch staff.

## Planned components

- Patient / bystander intake portal
- Triage rules and, in a later phase, an appropriately trained machine-learning model
- Priority queue and ambulance allocation
- Hospital / dispatch dashboard
- Data storage for requests and ambulance status

## Proposed technology

The design document suggests Python, Streamlit, scikit-learn, and SQLite as possible technologies for a student prototype. These are plans, not a claim that the application has already been implemented.

## Repository status

**Current stage: design and planning.** This repository contains the original project design PDF and a proposed folder structure. Application source code is intentionally not included yet.

See [`docs/planned-structure.md`](docs/planned-structure.md) for the proposed layout.

## Safety note

This is an academic project concept, not a clinically validated medical triage tool or an operational ambulance dispatch service. It must not be used to make real emergency-care decisions.
