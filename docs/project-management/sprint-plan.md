# Sprint Plan - Week 8 Classroom Simulation
 
## Sprint Goal
Make the Study Planning Agent easier to trust and review by improving visibility of saved plans, handling missing deadline information explicitly, and providing a shareable plan output.
 
## Scope and assumptions
- Existing SQLite-enabled agent application is a **read-only technical baseline** for this lab.
- This is a **simulated iteration for learning Scrum**; writing these documents does not deliver the three production features.
- Simulated Sprint capacity: **13 story points**.
- Story points measure relative effort/complexity/uncertainty; **not a fixed number of hours**.
 
## Selected Sprint Backlog
| PBI | Intended outcome | SP | Why selected |
|---|---|---:|---|
| PB-01 | Review saved planning requests | 5 | Reuses current SQLite persistence |
| PB-02 | Make missing deadlines explicit | 3 | Protects an agent boundary requirement |
| PB-03 | Share a plan as Markdown | 5 | Visible reviewable output |
| **TOTAL** | | **13** | Fits the classroom capacity |
 
## Scrum accountabilities for the exercise
| Accountability | Example person / responsibility |
|---|---|
| Product Owner | Student acting as PO: orders PBIs and clarifies value |
| Scrum Master | Student facilitator: helps remove impediments and protect events |
| Developers | Developer A, B, C: estimate, plan and coordinate work collectively |
 
The names above are **role placeholders**. Replace them with the actual team's names if needed; one person may enact multiple roles in a small classroom exercise.
 
## Task-level plan (hours are coordination estimates only)
| Task | Parent PBI | Owner | Estimate | Intended evidence |
|---|---|---|---:|---|
| T-01 Saved-request query design | PB-01 | Developer A | 2 h | Query sketch / sample fields |
| T-02 History display design | PB-01 | Developer B | 1 h | Display layout sketch |
| T-03 History acceptance checks | PB-01 | Developer C | 1 h | Test scenarios written |
| T-04 Missing-deadline rule | PB-02 | Developer A | 1 h | Explicit validation rule |
| T-05 Clarification response | PB-02 | Developer B | 1 h | Response scenarios written |
| T-06 Markdown export format | PB-03 | Developer C | 1 h | Markdown outline |
| T-07 Export integration point | PB-03 | Developer A | 1 h | Proposed dependency boundary |
| T-08 Demo/review preparation | PB-03 | Developer B | 1 h | Demo notes for review |
 
## Risks and decisions
1. **Ambiguous deadline handling:** clarify PB-02 acceptance before treating it as complete.
2. **Architectural coupling:** put Markdown export at an application edge, not the domain model.
3. **Insufficient review time:** keep unfinished work visible instead of marking all tasks Done.
4. **Scope change:** do not edit production Python code in this lab; capture ideas for later sprints.
 
## Event plan
- Sprint Planning: decide Goal and select 13 SP.
- Daily Scrum simulations: Day 1, Day 2, Day 3 (see log).
- Sprint Review: inspect simulated outcome and stakeholder feedback.
- Retrospective: identify one measurable improvement for next Sprint.
