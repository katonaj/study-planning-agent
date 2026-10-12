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
|-- README.md
|-- .gitignore
|-- __init__.py
|-- app.py
|-- lab_agent.py
|-- run.py
|-- agent_memory.json
|-- agent_output.txt
|
|-- domain/
|   |-- __init__.py
|   `-- models.py
|
|-- ports/
|   |-- __init__.py
|   |-- calendar_port.py
|   `-- memory_store.py
|
|-- adapters/
|   |-- __init__.py
|   |-- fake_calendar.py
|   `-- json_memory.py
|
|-- agent/
|   |-- __init__.py
|   |-- states.py
|   |-- planner.py
|   `-- orchestrator.py
|
|-- notes/
|   `-- week1.md
|
`-- docs/
    |-- stakeholders.md
    |-- requirements.md
    |-- user-stories.md
    |-- use-cases.md
    |
    |-- models/
    |   |-- README.md
    |   |-- use-case-diagram.md
    |   |-- class-diagram.md
    |   |-- object-diagram.md
    |   |-- database-diagram.md
    |   `-- package-diagram.md
    |
    `-- behavior/
        |-- README.md
        |-- activity-diagram.md
        |-- state-machine-diagram.md
        `-- sequence-diagram.md
```

## Week 2 - Requirements Engineering

Week 2 adds stakeholder analysis, functional and non-functional requirements, AI-agent boundaries, user stories, acceptance criteria, traceability, and a Mermaid use-case-style model. The artefacts are stored in `docs/`.

## Week 3 – UML Structural Modeling

Week 3 adds structural models and a small Python domain-model application. Mermaid sources are stored in `docs/models/`, and `app.py` implements the same Student, Assignment, StudyPlan, and PlanItem concepts shown in the diagrams.

## Week 4 - Behavioral Modeling

Week 4 adds an executable planning workflow and three behavioral views of the same use case: an activity-style flowchart, a native Mermaid state machine, and a native Mermaid sequence diagram. The sequence model includes an AI-agent-style component calling a calendar tool and handling both success and failure.

## Week 5 - Software Architecture

Week 5 refactors the behavioral prototype into a small modular architecture. The project separates domain concepts, orchestration, planning, external ports, and concrete adapters. Mermaid diagrams document the decomposition and dependency direction.

## Application Status

The executable `lab_agent.py` application is unchanged from Week 1. Week 2 changes the specification and project documentation, not the implementation.

## Current Project Status

- Week 1: completed - Git workflow and introductory agent simulator
- Week 2: completed - requirements engineering and use-case modeling
- Week 3: completed - structural models and Python domain model
- Week 4: completed - behavioral models and executable agent workflow
- Week 5: completed - architectural decomposition, interfaces, coupling/cohesion, and agent architecture
- Week 6: next - conceptual data model, relational design, normalization, and persistence
