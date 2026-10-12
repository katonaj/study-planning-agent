from dataclasses import dataclass, field  # Import dataclass helpers so the Week 3 domain objects remain concise and readable.
from datetime import date  # Import date so assignment deadlines use a structured date value.

@dataclass  # Ask Python to generate common data-object behavior for Student.
class Student:  # Define the student who owns assignments and receives a study plan.
    student_id: int  # Store the unique identifier of the student.
    name: str  # Store the student's display name.

@dataclass  # Ask Python to generate common data-object behavior for Assignment.
class Assignment:  # Define one assignment that may appear in a generated study plan.
    assignment_id: int  # Store the unique identifier of the assignment.
    title: str  # Store the human-readable assignment title.
    deadline: date  # Store the assignment deadline.
    estimated_hours: float  # Store the estimated amount of work.
    priority: int  # Store a simple priority value where a lower number means higher priority.

@dataclass  # Ask Python to generate common data-object behavior for PlanItem.
class PlanItem:  # Define one scheduled study item inside a StudyPlan.
    assignment: Assignment  # Reference the assignment scheduled by this plan item.
    scheduled_slot: str  # Store the selected calendar slot.
    planned_hours: float  # Store the number of hours allocated to the assignment.

@dataclass  # Ask Python to generate common data-object behavior for StudyPlan.
class StudyPlan:  # Define the aggregate result returned by the planning use case.
    student: Student  # Reference the student who owns the plan.
    items: list[PlanItem] = field(default_factory=list)  # Create an independent PlanItem list for every StudyPlan instance.
