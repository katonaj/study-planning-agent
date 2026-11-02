# XP and TDD Notes - Week 8
 
## Scrum, XP and TDD are different
| Concept | What it contributes | Study Planning Agent example |
|---|---|---|
| Scrum | Sprint Goal, backlog, inspection and adaptation | Select PB-02 because trust is part of the Sprint Goal |
| Extreme Programming (XP) | Collaboration and disciplined engineering | Pair on the validation boundary, integrate small changes |
| Test-Driven Development (TDD) | Short test-first implementation feedback | Define missing-deadline behavior before writing the rule |
 
Scrum does **not** prescribe specific coding techniques. XP practices and TDD can help a team create a high-quality Increment within a Scrum Sprint.
 
## Future PB-02 Red-Green-Refactor example (not executed in Week 8)
**Scenario:** an assignment is missing a deadline.  
**Red:** write a test that expects a clarification request and no fabricated date; it fails before validation is implemented.  
**Green:** implement the smallest boundary rule that checks the missing field and returns a clarification.  
**Refactor:** move validation into a named, testable responsibility, keep the result consistent and rerun tests.
 
### Example acceptance statements
- **Given** an assignment with no deadline, **when** a plan is requested, **then** the system asks for the deadline before scheduling.
- **Given** complete assignment data, **when** a plan is requested, **then** normal planning can continue.
- **Given** missing input, **when** the user is asked for details, **then** no invented deadline is written to persistent data.
 
## XP practices to try later
- Pair programming on the most uncertain rule.
- Small integrated changes instead of a large final merge.
- Continuous review/refactoring supported by automated tests.
- Simple design with explicit interfaces for tool boundaries.
 
## Week 8 evidence boundary
This file is a **design of a future TDD cycle**, not evidence that tests were written or executed now. Week 8 does not change Python production code or add new tests.
