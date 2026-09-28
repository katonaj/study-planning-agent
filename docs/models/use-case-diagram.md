# Use Case Diagram

The following use-case diagram shows the main interactions between the Student, the Study Planning Agent, and the external Calendar Service.

```mermaid id="u7c4lx"
flowchart LR
    Student["Student"]
    Calendar["Calendar Service"]

    subgraph SPA["Study Planning Agent"]
        UC1(["Enter assignments"])
        UC2(["Generate weekly plan"])
        UC3(["Review plan and explanation"])
        UC4(["Regenerate plan"])
        UC5(["Read calendar availability"])
    end

    Student --- UC1
    Student --- UC2
    Student --- UC3
    Student --- UC4

    Calendar --- UC5

    UC2 -. optional data .-> UC5
```

The diagram shows that the student can enter assignments, generate a weekly plan, review the generated plan and its explanation, and request regeneration. The Study Planning Agent can also use calendar availability as optional external data when generating a plan.
