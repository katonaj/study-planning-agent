# Study Planning Agent

**Course:** Software Engineering and AI Agent Fundamentals
**Course code:** GAINBAN-SZOFMEIN-1
**Project type:** Semester laboratory project

## About This Repository

This repository contains the semester project and laboratory artefacts for the Software Engineering and AI Agent Fundamentals course.

The project is developed incrementally. Each laboratory adds software engineering documentation, models, source code, tests, or AI-agent-related components.

## Current Repository Structure

```text
study-planning-agent/
├── README.md
├── .gitignore
├── run.py
├── inspect_database.py
├── lab_agent.py
├── agent_memory.json
├── agent_output.txt
├── __init__.py
├── notes/
│   └── week1.md
├── db/
│   └── schema.sql
├── domain/
│   ├── __init__.py
│   └── models.py
├── ports/
│   ├── __init__.py
│   ├── calendar_port.py
│   ├── memory_store.py
│   └── study_repository.py
├── adapters/
│   ├── __init__.py
│   ├── fake_calendar.py
│   ├── sqlite_database.py
│   ├── sqlite_memory.py
│   └── sqlite_repository.py
├── agent/
│   ├── __init__.py
│   ├── orchestrator.py
│   ├── planner.py
│   └── states.py
└── docs/
    ├── stakeholdres.md
    ├── requirements.md
    ├── user-stories.md
    ├── use-cases.md
    ├── models/
    │   ├── README.md
    │   ├── class-diagram.md
    │   ├── database-diagram.md
    │   ├── object-diagram.md
    │   ├── package-diagram.md
    │   └── use-case-diagram.md
    ├── behavior/
    │   ├── README.md
    │   ├── activity-diagram.md
    │   ├── sequence-diagram.md
    │   └── state-machine-diagram.md
    ├── architecture/
    │   ├── README.md
    │   ├── agent-architecture.md
    │   ├── architecture-decisions.md
    │   ├── interfaces.md
    │   └── system-architecture.md
    ├── data-model/
    │   ├── README.md
    │   ├── conceptual-model.md
    │   ├── mapping.md
    │   ├── normalization.md
    │   ├── queries.md
    │   └── relational-schema.md
    └── project-management/
        ├── README.md
        ├── daily-scrum-log.md
        ├── definition-of-done.md
        ├── product-backlog.md
        ├── retrospective.md
        ├── sprint-board.md
        ├── sprint-plan.md
        ├── sprint-review.md
        └── xp-tdd-notes.md
```

## Week 2 - Requirements Engineering

Week 2 adds stakeholder analysis, functional and non-functional requirements, AI-agent boundaries, user stories, acceptance criteria, traceability, and a Mermaid use-case-style model. The artefacts are stored in `docs/`.

## Week 3 – UML Structural Modeling

Week 3 adds structural models and a small Python domain-model application. Mermaid sources are stored in `docs/models/`, and `app.py` implements the same Student, Assignment, StudyPlan, and PlanItem concepts shown in the diagrams.

## Week 4 - Behavioral Modeling

Week 4 adds an executable planning workflow and three behavioral views of the same use case: an activity-style flowchart, a native Mermaid state machine, and a native Mermaid sequence diagram. The sequence model includes an AI-agent-style component calling a calendar tool and handling both success and failure.

## Week 5 - Software Architecture

Week 5 refactors the behavioral prototype into a small modular architecture. The project separates domain concepts, orchestration, planning, external ports, and concrete adapters. Mermaid diagrams document the decomposition and dependency direction.

## Week 6 - Data Modeling and Persistence

Week 6 maps the Study Planning Agent domain model to a normalized relational schema and adds an executable SQLite persistence adapter. Students, assignments, plans and plan items are stored as business data. Planning-request state, memory events and calendar tool calls demonstrate persistence for agent workflows.

## Week 8 - Scrum Planning and Project Governance
- Planning artefacts: `docs/project-management/README.md` (index plus eight detailed Markdown files).
- Scope: Scrum planning and simulated iteration; no new production Python feature in Week 8.
- Sprint Goal: improve transparency, missing-deadline handling, and shareability.
- Selected: PB-01 (5 SP), PB-02 (3 SP), PB-03 (5 SP); 13 SP capacity.
- Final simulated board: 6 Done, 1 In Review, 1 In Progress; PB-03 is unfinished.
- Existing SQLite application remains the working technical baseline.

## Application Status

The executable `lab_agent.py` application is unchanged from Week 1. Week 2 changes the specification and project documentation, not the implementation.

## Current Project Status

- Week 1: completed - Git workflow and introductory agent simulator
- Week 2: completed - requirements engineering and use-case modeling
- Week 3: completed - structural models and Python domain model
- Week 4: completed - behavioral models and executable agent workflow
- Week 5: completed - architectural decomposition and interfaces
- Week 6: completed - conceptual data model, relational design, normalization and SQLite persistence
- Week 7: next - coding standards, code review, branching and traceability
- Week 8: completed - Scrum sprint planning, Product Backlog, Sprint Board, simulated Daily Scrum, Sprint Review, Retrospective, and XP/TDD overview
- Week 9: next - SOLID principles, design patterns and agent tool abstractions
