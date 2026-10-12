from agent.states import AgentState  # Import named states so workflow transitions remain explicit after refactoring.
from domain.models import StudyPlan  # Import StudyPlan so the orchestrator can return a valid empty result when needed.
from ports.calendar_port import CalendarUnavailableError  # Import the provider-independent calendar failure defined by the port.

class StudyPlanningOrchestrator:  # Define the application component that coordinates observation, tool use, planning, memory, and result delivery.
    def __init__(self, planner, calendar, memory):  # Receive dependencies from the composition root instead of constructing concrete classes internally.
        self.planner = planner  # Store the planning component behind a small cohesive responsibility.
        self.calendar = calendar  # Store an object that satisfies the CalendarPort contract.
        self.memory = memory  # Store an object that satisfies the MemoryStore contract.
        self.state = AgentState.IDLE  # Start the agent workflow in the Idle state.
    def move_to(self, new_state):  # Define one helper so all state changes are handled consistently.
        self.state = new_state  # Replace the current state with the supplied next state.
        print(f"STATE -> {self.state.value}")  # Print the state transition so the run remains easy to compare with the Week 4 state diagram.
        self.memory.append(f"State: {self.state.value}")  # Persist the transition through the MemoryStore abstraction.
    def generate_plan(self, student, assignments):  # Define the main application use case coordinated by the orchestrator.
        print(f"REQUEST -> Generate weekly plan for {student.name}")  # Show the incoming user goal that starts the workflow.
        self.move_to(AgentState.OBSERVING)  # Enter Observing before validating the supplied assignment list.
        if not assignments:  # Decide whether the workflow has enough assignment input to continue safely.
            self.move_to(AgentState.WAITING_FOR_INPUT)  # Enter WaitingForInput when the required domain data is missing.
            print("RESULT -> Please enter at least one assignment.")  # Explain the missing-input result instead of inventing data.
            return StudyPlan(student=student)  # Return an empty but valid StudyPlan object.
        self.move_to(AgentState.CALLING_TOOL)  # Enter the tool-call state before asking the calendar abstraction for availability.
        try:  # Protect the application workflow because an external adapter may fail.
            availability = self.calendar.get_availability()  # Call the calendar through its port without knowing the adapter implementation.
            self.memory.append("Tool result: calendar availability received")  # Store a provider-independent event through the memory abstraction.
        except CalendarUnavailableError as error:  # Handle the provider-independent error exposed by CalendarPort.
            self.move_to(AgentState.FAILED)  # Enter Failed when calendar availability cannot be obtained.
            print(f"RESULT -> Could not generate plan: {error}")  # Return a clear user-facing explanation of the failure.
            return StudyPlan(student=student)  # Return an empty plan while keeping the application stable.
        self.move_to(AgentState.PLANNING)  # Enter Planning after all information required by the Planner is available.
        plan = self.planner.create_plan(student=student, assignments=assignments, availability=availability)  # Delegate planning rules instead of embedding them in orchestration code.
        self.memory.append("Generated study plan")  # Persist successful plan generation through the MemoryStore port.
        self.move_to(AgentState.COMPLETED)  # Enter Completed after the planner has returned the final plan.
        print("RESULT -> Study plan generated")  # Tell the presentation layer that the goal completed successfully.
        return plan  # Return the generated StudyPlan to the caller.
