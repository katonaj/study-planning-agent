from dataclasses import dataclass, field  # Import dataclass helpers so the Week 3 domain objects remain concise and readable.
from datetime import date  # Import date so assignment deadlines and scheduled study dates use a structured date type.
from enum import Enum  # Import Enum so the agent states match the Week 4 state-machine model explicitly.
from pathlib import Path  # Import Path so the application can store a small persistent memory file safely.
import json  # Import json so memory events can be saved in a human-readable format.
import sys  # Import sys so simple command-line switches can select success and failure scenarios.

MEMORY_FILE = Path("week4_memory.json")  # Define the persistent memory file created by the Week 4 application.

@dataclass  # Ask Python to generate common data-object behavior for Student.
class Student:  # Keep the Student domain concept introduced in Week 3.
    student_id: int  # Store the unique identifier of the student.
    name: str  # Store the student's display name.

@dataclass  # Ask Python to generate common data-object behavior for Assignment.
class Assignment:  # Keep the Assignment domain concept introduced in Week 3.
    assignment_id: int  # Store the unique identifier of the assignment.
    title: str  # Store the human-readable assignment title.
    deadline: date  # Store the assignment deadline.
    estimated_hours: float  # Store the estimated amount of work.
    priority: int  # Store a simple priority value where a lower number means higher priority.

@dataclass  # Ask Python to generate common data-object behavior for PlanItem.
class PlanItem:  # Represent one scheduled study item inside the generated plan.
    assignment: Assignment  # Reference the Assignment scheduled by this item.
    scheduled_slot: str  # Store the calendar slot selected for the assignment.
    planned_hours: float  # Store the number of hours allocated in the plan.

@dataclass  # Ask Python to generate common data-object behavior for StudyPlan.
class StudyPlan:  # Represent the result returned by the planning workflow.
    student: Student  # Reference the student who owns the plan.
    items: list[PlanItem] = field(default_factory=list)  # Create a separate PlanItem list for every StudyPlan object.

class AgentState(Enum):  # Define the states that appear in the Week 4 state-machine diagram.
    IDLE = "Idle"  # Represent the state before a planning request starts.
    OBSERVING = "Observing"  # Represent the state while the agent checks the supplied assignments.
    WAITING_FOR_INPUT = "WaitingForInput"  # Represent the state used when required assignment input is missing.
    CALLING_TOOL = "CallingCalendarTool"  # Represent the state while the external calendar tool is being called.
    PLANNING = "Planning"  # Represent the state while the study plan is being created.
    COMPLETED = "Completed"  # Represent successful goal completion.
    FAILED = "Failed"  # Represent a recoverable tool or workflow failure.

class CalendarToolError(Exception):  # Define a small custom exception so tool failure is explicit in the workflow.
    pass  # No extra behavior is needed beyond giving the failure a meaningful type.

class CalendarTool:  # Define a deterministic teaching tool that stands in for an external calendar service.
    def __init__(self, should_fail=False):  # Allow the caller to request a simulated tool failure for the failure-path demo.
        self.should_fail = should_fail  # Store whether this tool instance should fail when called.
    def get_availability(self):  # Define the external-style operation invoked by the agent.
        print("CalendarTool: get_availability() called")  # Make the tool-call message visible for comparison with the sequence diagram.
        if self.should_fail:  # Check whether the current scenario asks us to simulate an unavailable external service.
            raise CalendarToolError("Calendar service unavailable")  # Stop the tool call with a controlled, explainable failure.
        return ["Monday 14:00-16:00", "Tuesday 10:00-12:00"]  # Return stable fake data so no account or API key is required.

class JsonMemory:  # Define a tiny persistence helper that demonstrates memory as part of the behavioral workflow.
    def load(self):  # Define the operation that reads previously stored workflow events.
        if not MEMORY_FILE.exists():  # Check whether this is the first run and no memory file exists yet.
            return []  # Return an empty event history when there is nothing to load.
        return json.loads(MEMORY_FILE.read_text(encoding="utf-8"))  # Read and parse the existing JSON event list.
    def append(self, event):  # Define the operation that stores one new workflow event.
        events = self.load()  # Load the existing persistent history before adding the new event.
        events.append(event)  # Add the supplied event string to the in-memory list.
        MEMORY_FILE.write_text(json.dumps(events, indent=2), encoding="utf-8")  # Save the updated list back to disk.

class StudyPlanningAgent:  # Define the agent whose behavior is modeled by the Week 4 diagrams.
    def __init__(self, calendar_tool, memory):  # Receive the tool and memory dependencies from the outside.
        self.calendar_tool = calendar_tool  # Store the calendar tool used by the tool-calling step.
        self.memory = memory  # Store the persistent memory component used by the workflow.
        self.state = AgentState.IDLE  # Start the state machine in the Idle state.
    def move_to(self, new_state):  # Define one helper operation for visible and consistent state transitions.
        self.state = new_state  # Replace the current state with the supplied next state.
        print(f"STATE -> {self.state.value}")  # Print the transition so the terminal output can be compared with the state diagram.
        self.memory.append(f"State: {self.state.value}")  # Persist the state transition so the run can be inspected later.
    def generate_plan(self, student, assignments):  # Define the main use case represented by the activity and sequence diagrams.
        print(f"REQUEST -> Generate weekly plan for {student.name}")  # Show the incoming request that starts the workflow.
        self.move_to(AgentState.OBSERVING)  # Enter Observing before checking the supplied assignment data.
        if not assignments:  # Make the activity-diagram decision: are assignments available?
            self.move_to(AgentState.WAITING_FOR_INPUT)  # Enter WaitingForInput when the required data is missing.
            print("RESULT -> Please enter at least one assignment.")  # Return a clear user-facing explanation instead of inventing data.
            return StudyPlan(student=student)  # Return an empty plan because planning cannot continue safely.
        self.move_to(AgentState.CALLING_TOOL)  # Enter the tool-call state before requesting calendar availability.
        try:  # Start a protected block because external tools can fail.
            availability = self.calendar_tool.get_availability()  # Send the tool message shown in the sequence diagram.
            self.memory.append("Tool result: calendar availability received")  # Record successful tool use in persistent memory.
        except CalendarToolError as error:  # Handle only the controlled calendar failure used by this laboratory.
            self.move_to(AgentState.FAILED)  # Enter Failed because the external dependency did not return data.
            print(f"RESULT -> Could not generate plan: {error}")  # Explain the failure to the user without silently losing input.
            return StudyPlan(student=student)  # Return an empty result object while preserving the original assignments outside it.
        self.move_to(AgentState.PLANNING)  # Enter Planning after the tool result is available.
        ordered = sorted(assignments, key=lambda item: (item.priority, item.deadline))  # Apply a deterministic rule so the planning decision is transparent.
        plan = StudyPlan(student=student)  # Create the result aggregate that will collect scheduled items.
        for index, assignment in enumerate(ordered):  # Process the ordered assignments one by one.
            slot = availability[index % len(availability)]  # Select a calendar slot and reuse the small demo list when necessary.
            hours = min(assignment.estimated_hours, 2.0)  # Limit each demo session to at most two hours for a simple visible rule.
            plan.items.append(PlanItem(assignment=assignment, scheduled_slot=slot, planned_hours=hours))  # Add the scheduled assignment to the study plan.
        self.move_to(AgentState.COMPLETED)  # Enter Completed after all plan items have been generated.
        print("RESULT -> Study plan generated")  # Tell the caller that the goal was completed successfully.
        return plan  # Return the generated StudyPlan object to the caller.

def build_demo_input():  # Define deterministic input that students can compare with the Mermaid diagrams.
    student = Student(student_id=1, name="Alex Student")  # Create the same example student used in the Week 3 model.
    assignments = [  # Create a small list of assignments for the successful planning path.
        Assignment(assignment_id=101, title="UML Behavioral Models", deadline=date(2026, 9, 27), estimated_hours=3.0, priority=1),  # Create the highest-priority Week 4 assignment.
        Assignment(assignment_id=102, title="Python Agent Workflow", deadline=date(2026, 9, 29), estimated_hours=4.0, priority=2),  # Create the second assignment used by the demo.
    ]  # Finish the list of deterministic assignments.
    return student, assignments  # Return both input objects to the program entry point.

def print_plan(plan):  # Define a helper that prints the final plan as observable output.
    for item in plan.items:  # Iterate through every generated PlanItem object.
        print(f"PLAN -> {item.scheduled_slot}: {item.assignment.title} ({item.planned_hours} h)")  # Print the slot, assignment title, and planned duration.

if __name__ == "__main__":  # Run the following scenario setup only when app.py is executed directly.
    student, assignments = build_demo_input()  # Create the deterministic Week 4 input objects.
    calendar_fails = "--calendar-fail" in sys.argv  # Detect whether the user requested the simulated calendar-failure path.
    no_assignments = "--no-assignments" in sys.argv  # Detect whether the user requested the missing-input path.
    selected_assignments = [] if no_assignments else assignments  # Choose an empty or populated assignment list based on the requested scenario.
    calendar_tool = CalendarTool(should_fail=calendar_fails)  # Create the fake external tool configured for the selected scenario.
    memory = JsonMemory()  # Create the persistent memory component used by the agent.
    agent = StudyPlanningAgent(calendar_tool=calendar_tool, memory=memory)  # Inject the tool and memory into the agent.
    plan = agent.generate_plan(student=student, assignments=selected_assignments)  # Execute the behavioral workflow represented by the Week 4 diagrams.
    print_plan(plan)  # Print any generated plan items so the final result can be inspected in the terminal.
