from enum import Enum  # Import Enum so named agent states are explicit and easy to compare with the Week 4 state diagram.

class AgentState(Enum):  # Define the states used by the refactored Week 5 orchestrator.
    IDLE = "Idle"  # Represent the state before a planning request begins.
    OBSERVING = "Observing"  # Represent the state while the application checks supplied assignments.
    WAITING_FOR_INPUT = "WaitingForInput"  # Represent the state used when no assignments were supplied.
    CALLING_TOOL = "CallingCalendarTool"  # Represent the state while the calendar port is being invoked.
    PLANNING = "Planning"  # Represent the state while the Planner creates plan items.
    COMPLETED = "Completed"  # Represent successful goal completion.
    FAILED = "Failed"  # Represent a controlled external-tool or workflow failure.
