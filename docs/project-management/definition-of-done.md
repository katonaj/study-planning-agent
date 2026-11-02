# Definition of Done - Week 8
 
## Why a Definition of Done matters
A Definition of Done is a shared quality standard for a usable Increment. A task moving to `Done` because someone stopped working is not enough. This lab uses a **simulation-level exercise checklist** to teach the concept, and separately states the stronger criteria required for actual shipped software.
 
## Classroom simulation: design / documentation task checklist
- [x] Selected backlog item and expected value are stated.
- [x] Acceptance conditions or verification steps are written for the design task.
- [x] Task output is understandable to another team member.
- [x] Relevant architecture boundaries and risks are documented.
- [x] A peer reviews the exercise artefact before its simulated status becomes Done.
- [x] Its board status and Daily Scrum log are consistent.
- [x] The simulated review identifies remaining unfinished work honestly.
 
**Apply this exercise checklist only to the six tasks marked Done in the sample board.** It does **not** mean that PB-01 or PB-02 exists as working production functionality.
 
## Real software Increment: required when implementing a feature later
- [ ] Acceptance criteria are satisfied by running code.
- [ ] New behavior has suitable automated tests or verified test evidence.
- [ ] Regression tests pass and existing behavior still runs.
- [ ] Code respects architecture/dependency boundaries.
- [ ] Peer review is complete and required documents are current.
- [ ] No secrets or runtime `.db`, `.db-shm`, `.db-wal` files are committed.
- [ ] The change is integrated and potentially releasable.
 
These production boxes are **intentionally unchecked** for Week 8 because no feature was implemented.
 
## Review rule
A Product Backlog Item can be described as fully delivered only if its integrated software meets the real Definition of Done. The Week 8 board tracks **simulated planning/design work**, not shipped feature delivery.
