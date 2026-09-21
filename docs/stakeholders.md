# Stakeholders

## Stakeholder Analysis

| Stakeholder | Type | Why they matter | Main need | Main concern |
|---|---|---|---|---|
| Student | Primary | The student is the main user of the Study Planning Agent. | A useful and realistic 7-day study plan. | Wrong priorities, unrealistic plans, or loss of privacy. |
| Instructor | Secondary | Instructors define coursework, expectations, and deadlines. | Course tasks and deadlines should be represented accurately. | The agent must not invent deadlines or claim instructor approval. |
| Department / Project Owner | Secondary | The department sponsors, evaluates, or governs the system. | A useful system with a clear and manageable scope. | Cost, quality, compliance, and project risk. |
| IT / Security Administrator | Secondary | IT staff maintain access, authentication, and integrations. | Safe authentication and minimum necessary permissions. | Credential leakage, excessive permissions, or insecure integrations. |
| Calendar / Data Service | External system | The external service may provide calendar availability to the agent. | Well-formed requests using allowed access. | Rate limits, outages, and permission scope. |

## Primary and Secondary Stakeholders

- **Primary stakeholder:** Student
- **Secondary stakeholders:** Instructor, Department / Project Owner, IT / Security Administrator
- **External dependency:** Calendar / Data Service

## Raw Needs

- The student wants urgent deadlines to be clearly visible.
- The student wants a weekly plan that considers estimated effort and priority.
- The student wants to understand why a task was scheduled earlier than another task.
- The student does not want the agent to edit the calendar automatically.
- The student wants to regenerate the plan when deadlines or priorities change.
- The instructor wants course deadlines to be represented accurately.
- The instructor does not want the system to invent assignment requirements.
- IT wants integrations to use the minimum permissions necessary.
- IT wants external-service failures to be visible rather than silently ignored.
- The department wants the system scope to remain clear and testable.
