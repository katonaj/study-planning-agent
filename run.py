from datetime import date  # Import date so deterministic demonstration assignments can contain real deadlines.
import sys  # Import sys so command-line switches can select the normal and failure scenarios.

from domain.models import Student, Assignment  # Import the stable domain input objects.
from agent.planner import Planner  # Import the cohesive planning component.
from agent.orchestrator import StudyPlanningOrchestrator  # Import the application orchestrator that coordinates the use case.
from adapters.fake_calendar import FakeCalendarAdapter  # Import the concrete calendar adapter selected for this demonstration.
from adapters.json_memory import JsonMemoryStore  # Import the concrete persistent-memory adapter selected for this demonstration.

def build_demo_input():  # Define deterministic input so students can compare runs with the Week 4 behavioral models.
    student = Student(student_id=1, name="Alex Student")  # Create the same example student used in earlier weeks.
    assignments = [  # Create two assignments that the planner will schedule.
        Assignment(assignment_id=101, title="Architecture Diagram", deadline=date(2026, 10, 4), estimated_hours=3.0, priority=1),  # Create the higher-priority architecture task.
        Assignment(assignment_id=102, title="Python Refactoring", deadline=date(2026, 10, 6), estimated_hours=4.0, priority=2),  # Create the second Week 5 task.
    ]  # Finish the deterministic assignment list.
    return student, assignments  # Return both input values to the composition root.

def print_plan(plan):  # Define a small presentation helper that displays the generated result.
    for item in plan.items:  # Iterate through every PlanItem returned by the application.
        print(f"PLAN -> {item.scheduled_slot}: {item.assignment.title} ({item.planned_hours} h)")  # Print one readable line for each scheduled item.

if __name__ == "__main__":  # Execute the following composition-root code only when run.py is started directly.
    student, assignments = build_demo_input()  # Create the deterministic domain input used by all Week 5 scenarios.
    calendar_fails = "--calendar-fail" in sys.argv  # Detect whether the user requested a simulated calendar-adapter failure.
    no_assignments = "--no-assignments" in sys.argv  # Detect whether the user requested the missing-input scenario.
    selected_assignments = [] if no_assignments else assignments  # Select empty or populated input according to the command-line scenario.
    planner = Planner()  # Construct the planning component.
    calendar = FakeCalendarAdapter(should_fail=calendar_fails)  # Construct the concrete CalendarPort adapter chosen for this run.
    memory = JsonMemoryStore()  # Construct the concrete MemoryStore adapter chosen for this run.
    application = StudyPlanningOrchestrator(planner=planner, calendar=calendar, memory=memory)  # Inject all dependencies into the orchestrator in one visible composition root.
    plan = application.generate_plan(student=student, assignments=selected_assignments)  # Run the same planning use case that was modeled behaviorally in Week 4.
    print_plan(plan)  # Display any generated plan items as the final observable program output.