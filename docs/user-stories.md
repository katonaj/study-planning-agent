# User Stories

## US-01 Generate a Weekly Study Plan

As a student, I want the agent to generate a 7-day plan from my assignments, so that I can focus on the most urgent and important work first.

**Related requirements:** FR-01, FR-02, NFR-01, AG-01, AG-02

### Acceptance criteria

**AC-01**  
Given the student has entered three assignments with valid deadlines,  
When the student generates a weekly plan,  
Then all three assignments shall appear in the 7-day plan.

**AC-02**  
Given two assignments have different deadlines and priorities,  
When the plan is generated,  
Then the system shall produce an ordering that uses the available assignment data.

**AC-03**  
Given one assignment has no deadline,  
When the student requests a plan,  
Then the agent shall ask for the missing deadline instead of inventing one.

---

## US-02 Review the Reason for a Recommendation

As a student, I want to see why a task was scheduled early, so that I can judge whether the suggestion makes sense.

**Related requirements:** FR-04, NFR-03, AG-04

### Acceptance criteria

**AC-01**  
Given a weekly plan has been generated,  
When the student reviews a scheduled task,  
Then the system shall show at least one factor that influenced its position in the plan.

**AC-02**  
Given the task order was influenced by deadline, estimated effort, or priority,  
When the explanation is displayed,  
Then the relevant influencing data shall be identifiable.

**AC-03**  
Given an explanation is displayed,  
When the student reads it,  
Then user-provided facts shall be distinguishable from agent-generated suggestions.

---

## US-03 Regenerate the Plan After a Change

As a student, I want to regenerate the plan after changing a deadline, so that the plan reflects current information.

**Related requirements:** FR-03, NFR-04, AG-04

### Acceptance criteria

**AC-01**  
Given a study plan already exists,  
When the student changes an assignment deadline and regenerates the plan,  
Then the new plan shall use the updated deadline.

**AC-02**  
Given the student changes an assignment priority,  
When the plan is regenerated,  
Then the updated priority shall be available to the planning process.

**AC-03**  
Given an external calendar service is unavailable,  
When the student regenerates the plan,  
Then the system shall report the external-service failure and preserve the entered assignment data.

---

## US-04 Limit External Integration Permissions

As an IT administrator, I want external integrations to use minimum permissions, so that unnecessary account access is avoided.

**Related requirements:** NFR-02, NFR-04, AG-03

### Acceptance criteria

**AC-01**  
Given calendar integration is enabled with read permission,  
When the agent checks calendar availability,  
Then it shall only read data allowed by the granted permission scope.

**AC-02**  
Given the agent proposes a calendar change,  
When no explicit user confirmation has been given,  
Then the system shall not perform the calendar write operation.

**AC-03**  
Given the external calendar service rejects a request or is unavailable,  
When the integration fails,  
Then the system shall report the failure without silently deleting assignment data.
