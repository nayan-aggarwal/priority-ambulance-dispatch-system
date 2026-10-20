# Proposed Repository Structure

This is a plan for organising the project as implementation progresses. The future folders listed below do not mean those modules have already been coded.

## Current documentation-only structure

```text
priority-ambulance-dispatch-system/
├── README.md
└── docs/
    ├── project-design.pdf
    └── planned-structure.md
```

## Proposed structure for a later coding phase

```text
priority-ambulance-dispatch-system/
├── README.md
├── docs/
│   ├── project-design.pdf
│   └── planned-structure.md
├── app/             # Future: intake form and dashboard
├── triage/          # Future: priority rules and validated ML work
├── dispatch/        # Future: queue and ambulance allocation logic
├── database/        # Future: storage schema and data access
└── tests/           # Future: tests for implemented features
```

## Planned modules

- **Patient intake:** collect patient details, symptoms, available vital signs, and location.
- **Triage:** apply clearly documented rules; any machine-learning model would require suitable, appropriately labelled data and validation.
- **Dispatch:** prioritise emergency requests and consider available ambulance locations.
- **Dashboard:** display active requests and ambulance statuses for review by dispatch staff.
- **Database:** store emergency requests and fleet status when this module is implemented.

The exact structure may change once implementation begins and the project requirements are confirmed.
