# Use Cases

## Actors

- **Student** - primary human actor
- **Calendar Service** - external system used when calendar availability is enabled

## Use cases

- **UC-01 Enter assignments**
- **UC-02 Generate weekly plan**
- **UC-03 Review plan and explanation**
- **UC-04 Regenerate plan**
- **UC-05 Read calendar availability**

## Mermaid use-case-style diagram

```mermaid
flowchart LR
    Student["Student"]
    Calendar["Calendar Service"]

    subgraph SPA["Study Planning Agent"]
        UC1(["UC-01 Enter assignments"])
        UC2(["UC-02 Generate weekly plan"])
        UC3(["UC-03 Review plan and explanation"])
        UC4(["UC-04 Regenerate plan"])
        UC5(["UC-05 Read calendar availability"])
    end

    Student --- UC1
    Student --- UC2
    Student --- UC3
    Student --- UC4
    Calendar --- UC5
    UC2 -. optional data .-> UC5
```

## Notes

- Actors are outside the system boundary.
- Use cases are inside the **Study Planning Agent** boundary.
- Use-case names describe goals, not buttons or implementation details.
- Calendar availability is optional.
