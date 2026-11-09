# Week 9 - Code Review Checklist
 
## Review details
 
- **Branch:** `week9-solid-patterns`
- **Target branch:** `main`
- **Review scope:** Factory, Decorator, dependency direction, preserved workflow behavior, persistence, documentation, and Git hygiene.
- **Reviewer:** assigned peer or structured self-review.
- **Review outcome:** mark checks only after verifying the actual Week 9 implementation.
 
## A. Structure and responsibilities
 
- [ ] `factories/__init__.py` and `factories/calendar_factory.py` exist in the repository root.
- [ ] `adapters/logging_calendar.py` exists and imports `CalendarPort` from `ports.calendar_port`.
- [ ] `CalendarAdapterFactory.create()` returns a `CalendarPort` implementation for `fake`.
- [ ] Unknown provider names raise `ValueError`; `run.py` prints a controlled configuration message.
- [ ] `agent/orchestrator.py` does not import Factory, Decorator, or the concrete fake provider.
- [ ] `agent/planner.py` still owns scheduling rules, not provider selection.
 
## B. Contract and safe behavior
 
- [ ] `LoggingCalendarDecorator` implements `CalendarPort` and forwards `get_availability()`.
- [ ] Successful availability is returned unchanged.
- [ ] The decorator logs before and after a successful tool call.
- [ ] A tool failure is logged and re-raised without being silently converted to success.
- [ ] Missing assignments stop before the calendar tool is invoked.
 
## C. Reproducible verification
 
| Command | Expected check | Mark after running |
|---|---|---|
| `python run.py --reset-db` | Plan saved; `Completed`; Factory + Decorator messages | [ ] |
| `python run.py --reset-db --calendar-fail` | Controlled `Failed`, original error preserved | [ ] |
| `python run.py --reset-db --no-assignments` | `WaitingForInput`; no calendar call | [ ] |
| `python run.py --reset-db --calendar-provider=unknown` | Configuration message, exit code 2 | [ ] |
| `python run.py --reset-db` then `python inspect_database.py` | Plan and trace rows persisted | [ ] |
 
Do not copy expected terminal output lines into PowerShell. Run only commands shown in the first column.
 
## D. Documentation and repository hygiene
 
- [ ] `README.md`, `solid-review.md`, `patterns.md`, `traceability.md`, and this file are saved under `docs/design-patterns/`.
- [ ] Markdown tables and Mermaid diagram in `patterns.md` render correctly.
- [ ] Root `README.md` accurately reflects Week 9 and real repository paths.
- [ ] Modified Python lines are explained with comments in the laboratory style.
- [ ] `git diff` contains only intended Week 9 changes.
- [ ] No `*.db`, `*.db-wal`, `*.db-shm`, `__pycache__/`, or `.pyc` files are staged.
- [ ] Pull Request explains the changes and lists verification scenarios.
- [ ] After merge, local `main` is synchronized and `git status` is clean.
 
## E. Example reviewer comments and resolution
 
| Potential observation | Required action |
|---|---|
| A reference still uses `study_planning_agent/adapters/...` | Correct it to the real root-level `adapters/...` layout |
| Decorator catches the calendar error but returns an empty list | Re-raise the original error and repeat the failure test |
| `run.py` still constructs `FakeCalendarAdapter` directly | Delegate construction to `CalendarAdapterFactory` |
| README claims the SQLite schema changed in Week 9 | Correct the description; schema remains unchanged |
| Runtime database appears in the staged list | Unstage it and confirm `.gitignore` is correct |
 
## Final review record
 
- **Checks passed:** fill in after testing (do not claim success in advance).
- **Outstanding issues:** record any issue and its owner before merging.
- **Decision:** approve only if the preserved behavior and dependency rules are demonstrated.
