# Week 9 - Engineering Traceability
 
## Scope
 
This table connects the Week 9 refactoring goals to code, observable behavior, and verification. The identifiers W9-01 to W9-06 are *local teaching labels*, not previously approved functional requirement IDs.
 
| ID | Engineering concern | Primary evidence | Verification |
|---|---|---|---|
| W9-01 | Calendar provider selection is centralized | `factories/calendar_factory.py`, `run.py` | A normal run prints `FACTORY -> created FakeCalendarAdapter` |
| W9-02 | Core planning avoids concrete provider construction | `agent/orchestrator.py`, `ports/calendar_port.py` | Inspect imports; orchestrator has no direct FakeCalendarAdapter import |
| W9-03 | Tool-call logging is added without editing provider | `adapters/logging_calendar.py`, `adapters/fake_calendar.py` | Success run prints DECORATOR messages around the adapter call |
| W9-04 | Provider-independent tool failures remain controlled | `ports/calendar_port.py`, `agent/orchestrator.py` | Failure run reaches `Failed` and prints a clear message |
| W9-05 | Missing required input prevents tool invocation | `agent/orchestrator.py` | No-assignments run reaches `WaitingForInput` without adapter-call message |
| W9-06 | Refactoring preserves persistent business and trace data | `adapters/sqlite_repository.py`, `adapters/sqlite_memory.py`, `db/schema.sql` | `inspect_database.py` shows requests, plan items, memory events, tool calls |
 
## Verification procedure
 
**COMMAND - COPY AND RUN** (run these in order from the repository root):
 
```powershell
python run.py --reset-db
python run.py --reset-db --calendar-fail
python run.py --reset-db --no-assignments
python run.py --reset-db --calendar-provider=unknown
python run.py --reset-db
python inspect_database.py
```
 
**EXPECTED RESULTS - DO NOT COPY TO THE TERMINAL:**
 
- Normal run: `Completed` and at least one `PLAN ->` line.
- Calendar failure: `DECORATOR -> calendar call failed`, then `Failed`; no unhandled traceback.
- Missing input: `WaitingForInput` and no `FakeCalendarAdapter: get_availability()` message.
- Unknown provider: `CONFIGURATION -> Unsupported calendar provider: unknown` and exit code 2.
- Final successful run followed by database inspection: persisted request state `Completed`, study plan and tool trace entries.
 
## Trace inspection examples
 
| Event | Expected stored evidence | Why it matters |
|---|---|---|
| Request started | `planning_requests` row created | The workflow has a persistent identity |
| State transition | `planning_requests.status` and a `memory_events` entry | Task-state and memory agree |
| Calendar success/failure | `tool_calls.status` (`SUCCESS` or `FAILED`) | Tool use is auditable |
| Plan generated | `study_plans` and `plan_items` rows | The goal has a persisted result |
 
The Week 9 logging decorator prints additional terminal lines. It does not add new SQLite tables or change how `tool_calls` are persisted by the orchestrator.
 
## Week-to-week continuity
 
- **Week 2:** requirements and use-case documentation describe a study-planning goal and safe agent boundaries.
- **Week 3:** domain objects establish the Student/Assignment/StudyPlan/PlanItem vocabulary.
- **Week 4:** behavioral views explain observations, decisions, tool calls, and failure paths.
- **Week 5:** ports and adapters establish architectural boundaries.
- **Week 6:** SQLite persists plans, task state, memory, and tool traces.
- **Week 8:** Scrum artefacts record the planning and governance simulation.
- **Week 9:** Factory and Decorator clarify construction and logging without changing the business goal.
 
## Evidence to include in the Week 9 Pull Request
 
1. Updated `run.py` demonstrating factory selection and decoration.
2. `factories/calendar_factory.py` and `adapters/logging_calendar.py`.
3. These five `docs/design-patterns/` Markdown files.
4. Command outputs or reviewer notes for success, controlled failure, and missing input.
5. A concise statement that SQLite persistence and the normalized schema were preserved.
 
**Status:** this is a ready-to-use traceability reference; mark each check as verified only after running the corresponding scenario in your own repository.
