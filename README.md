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
|-- app.py
|-- lab_agent.py
|-- agent_memory.json
|-- agent_output.txt
|-- notes/
|   `-- week1.md
`-- docs/
    |-- stakeholders.md
    |-- requirements.md
    |-- user-stories.md
    |-- use-cases.md
    |-- models/
    |   |-- README.md
    |   |-- use-case-diagram.md
    |   |-- class-diagram.md
    |   |-- object-diagram.md
    |   |-- database-diagram.md
    |   `-- package-diagram.md
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

## Application Status

The executable `lab_agent.py` application is unchanged from Week 1. Week 2 changes the specification and project documentation, not the implementation.

## Current Project Status
- Week 1: completed - Git workflow and introductory agent simulator
- Week 2: completed - requirements engineering and use-case modeling
- Week 3: completed - structural modeling and Python domain model
- Week 4: completed - behavioral modeling and executable agent/tool workflow
- Week 5: next - architecture, interfaces, coupling/cohesion, and agent architecture
