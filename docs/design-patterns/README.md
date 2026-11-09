# Week 9 - SOLID Refactoring and Design Patterns
 
## Purpose
 
This folder documents the Week 9 refactoring of the existing Study Planning Agent. The aim is to improve dependency boundaries and observability without changing the planning goal, SQLite schema, or controlled-failure behavior.
 
Week 9 starts from the integrated Week 8 `main` branch. We implement a Factory for calendar-provider construction and a Decorator for calendar-call logging. The existing `FakeCalendarAdapter` still acts as an Adapter for `CalendarPort`.
 
## Implemented design and exact source locations
 
| Role | Source file | Responsibility |
|---|---|---|
| Application composition | `run.py` | Reads configuration and assembles the system |
| Factory | `factories/calendar_factory.py` | Creates a provider satisfying `CalendarPort` |
| Abstract contract | `ports/calendar_port.py` | Declares `get_availability()` and `CalendarUnavailableError` |
| Adapter | `adapters/fake_calendar.py` | Returns deterministic slots or raises a controlled error |
| Decorator | `adapters/logging_calendar.py` | Logs before/after a calendar call and re-raises errors |
| Core orchestration | `agent/orchestrator.py` | Coordinates input, tool calls, task states, and persistence |
| Planning rules | `agent/planner.py` | Orders assignments and creates plan items |
| Persistence | `adapters/sqlite_repository.py` and `adapters/sqlite_memory.py` | Stores plans, request states, tool calls, and memory events |
 
All paths above are relative to the repository root. In this project's actual layout, `adapters/`, `agent/`, `factories/`, and `ports/` are root-level packages; they are not inside a `study_planning_agent/` subdirectory.
 
## Design documentation index
 
- [`solid-review.md`](solid-review.md) - concrete SRP, OCP, LSP, ISP, and DIP evidence.
- [`patterns.md`](patterns.md) - Factory, Adapter, and Decorator roles and interaction.
- [`traceability.md`](traceability.md) - requirements, code, and runtime verification links.
- [`code-review-checklist.md`](code-review-checklist.md) - checks to perform before the Pull Request.
 
## Behavior that must remain unchanged
 
1. Valid assignments and working calendar produce a non-empty plan, persist it in SQLite, and reach `Completed`.
2. An unavailable calendar produces a controlled message and reaches `Failed`; the Decorator does not hide the error.
3. Missing assignments reach `WaitingForInput` without calling the calendar provider.
4. An unknown provider name produces a configuration error and a non-zero exit code.
 
## Verification commands (run from the repository root)
 
```powershell
python run.py --reset-db
python run.py --reset-db --calendar-fail
python run.py --reset-db --no-assignments
python run.py --reset-db --calendar-provider=unknown
python run.py --reset-db
python inspect_database.py
```
 
The terminal output is *expected evidence*, not text to paste into PowerShell. The last two commands deliberately restore a successful SQLite database before inspection.
 
## Scope and version-control rules
 
Week 9 is a refactoring increment, not a new scheduling feature. Keep domain entities, relational schema, and existing requirements/models unless a real design change requires an update. Commit `run.py`, `factories/`, `adapters/logging_calendar.py`, this documentation folder, and the root `README.md` update. Do not commit runtime `*.db` files or `__pycache__/`.
 
**Integration checkpoint:** after review, merge `week9-solid-patterns` into `main`; verify `git status` reports a clean working tree.
