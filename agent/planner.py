from domain.models import PlanItem, StudyPlan  # Import only the domain objects needed to build a plan.

class Planner:  # Define a cohesive component whose single responsibility is turning inputs into plan items.
    def create_plan(self, student, assignments, availability):  # Define the planning operation used by the orchestrator.
        ordered = sorted(assignments, key=lambda item: (item.priority, item.deadline))  # Order assignments with the same transparent rule used in Week 4.
        plan = StudyPlan(student=student)  # Create an empty StudyPlan aggregate for the supplied student.
        for index, assignment in enumerate(ordered):  # Process the ordered assignments one by one.
            slot = availability[index % len(availability)]  # Select a calendar slot and reuse the small demo list when necessary.
            hours = min(assignment.estimated_hours, 2.0)  # Keep each demonstration session at no more than two hours.
            plan.items.append(PlanItem(assignment=assignment, scheduled_slot=slot, planned_hours=hours))  # Add one fully constructed PlanItem to the plan.
        return plan  # Return the completed StudyPlan to the orchestrator.
