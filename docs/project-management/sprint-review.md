# Sprint Review - Week 8 (Simulated)
 
## Sprint Goal
Make the Study Planning Agent easier to trust and review by improving visibility of saved plans, handling missing deadline information explicitly, and providing a shareable plan output.
 
## Evidence inspected
- Current executable baseline: existing SQLite-enabled agent still runs (`python run.py --reset-db` and `python inspect_database.py`).
- Exercise artefacts: planned saved-request display, missing-deadline acceptance conditions, Markdown export outline.
- Final simulated board: 6 Done, 1 In Review, 1 In Progress.
 
## Selected work at review
| PBI | Simulated task progress | Real product feature delivered? | Review decision |
|---|---|---|---|
| PB-01 | T-01, T-02, T-03 all Done | **No** | Design exercise complete; implementation future work |
| PB-02 | T-04, T-05 both Done | **No** | Rules clarified; implementation future work |
| PB-03 | T-06 Done; T-07 In Progress; T-08 In Review | **No** | Open; review priority in backlog refinement |
 
## Stakeholder feedback (classroom role-play)
1. Show a request identifier and final state beside each saved planning request.
2. When an assignment lacks a deadline, ask for clarification rather than generate a guessed date.
3. Markdown export must remain legible and include enough context to explain the plan.
 
## Sprint Goal assessment
**Partially achieved in the classroom simulation:** PB-01 and PB-02 planning/design tasks reached simulated Done; PB-03 remains unfinished. **No new functioning production Increment was delivered in Week 8.** The working software baseline is unchanged.
 
## Product Backlog adaptation
- Return PB-03's unfinished design/integration work to backlog refinement (not automatically into the next Sprint).
- Add “show request ID and final state” to PB-01's acceptance notes.
- Keep all product feature implementation work visible for a later coding Sprint.
- Review PB-03 priority based on stakeholder feedback and current team capacity.
 
## Follow-up
The Product Owner discusses ordering; Developers refine and re-estimate unresolved items. The next Sprint Planning decides what to select, rather than automatically carrying over work.
