# Week 8 - Scrum Planning and Project Governance
 
**Project:** Study Planning Agent  
**Branch:** `week8-scrum-planning`  
**Learning mode:** classroom simulation; no production Python feature is implemented in Week 8.
 
## Purpose
This directory records a simulated Scrum iteration built on the existing SQLite-enabled Study Planning Agent. It documents decisions, relative estimates, roles, task movement, inspection and adaptation. **Simulated board completion is not proof that a product feature has been implemented.**
 
## Artefact index
| File | What it records |
|---|---|
| [product-backlog.md](product-backlog.md) | Ordered PB-01 to PB-08, story points, value and risks |
| [sprint-plan.md](sprint-plan.md) | Sprint Goal, 13 SP capacity, selected work and roles |
| [sprint-board.md](sprint-board.md) | T-01 to T-08 and simulated status changes |
| [daily-scrum-log.md](daily-scrum-log.md) | Three daily inspection/adaptation rounds |
| [definition-of-done.md](definition-of-done.md) | Quality agreement and simulation boundaries |
| [sprint-review.md](sprint-review.md) | Goal inspection, feedback, open work and backlog adaptation |
| [retrospective.md](retrospective.md) | Team-process learning and measurable improvement |
| [xp-tdd-notes.md](xp-tdd-notes.md) | XP practices and a planned Red-Green-Refactor example |
 
## Sprint at a glance
- Product direction: make the study-planning process trustworthy and reviewable.
- Selected PBIs: PB-01 (5 SP), PB-02 (3 SP), PB-03 (5 SP) = **13 SP**.
- Exercise owners: Developer A, Developer B and Developer C (replace with real team names if appropriate).
- Final simulated board: **6 Done, 1 In Review, 1 In Progress**.
- Simulated planning outcome: PB-01 and PB-02 complete in the exercise; PB-03 remains open.
- **Real product state:** Week 6 SQLite application remains the executable baseline; no new feature is claimed.
 
## Verification and working agreements
1. Read the eight documents in the order shown above.
2. Check that `sprint-plan.md` and `product-backlog.md` both total 13 selected story points.
3. Check that the final board contains exactly eight tasks and that daily notes explain the movements.
4. Verify the existing application with `python run.py --reset-db` and `python inspect_database.py`.
5. Do not commit `.db`, `.db-shm` or `.db-wal` runtime files.
6. Review and merge documentation through a Pull Request into `main`.
