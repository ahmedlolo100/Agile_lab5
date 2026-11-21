"""Refactored tuition-fee calculation module."""

from dataclasses import dataclass
from enum import Enum


HOURLY_FEE = 350
STAFF_CHILD_RATE = 0.5
HIGH_FEE_THRESHOLD = 6000
HIGH_FEE_REDUCTION = 200
SUMMER_SURCHARGE = 150


class StudentType(Enum):
    """Supported student categories."""

    REGULAR = 1
    STAFF_CHILD = 2
    SCHOLARSHIP = 3


@dataclass(frozen=True)
class Course:
    """A course represented by its number of credit hours."""

    hours: int


def tuition_fee(
    courses: list[Course],
    student_type: StudentType,
    summer: bool = False,
    discount: float = 0,
    extras: tuple[float, ...] = (),
) -> float:
    """Calculate tuition while preserving the legacy fee rules."""
    hourly_rates = {
        StudentType.REGULAR: HOURLY_FEE,
        StudentType.STAFF_CHILD: HOURLY_FEE * STAFF_CHILD_RATE,
        StudentType.SCHOLARSHIP: 0,
    }
    rate = hourly_rates[student_type]
    total = sum(course.hours * rate for course in courses)

    if total > HIGH_FEE_THRESHOLD:
        total -= HIGH_FEE_REDUCTION
    if summer:
        total += SUMMER_SURCHARGE

    total -= discount
    total += sum(extras)
    return total


def report(
    courses: list[Course],
    student_type: StudentType,
    summer: bool = False,
    discount: float = 0,
) -> str:
    """Return a readable fee report without printing."""
    amount = tuition_fee(courses, student_type, summer, discount)
    if student_type is StudentType.REGULAR:
        label = "Student fee"
    elif student_type is StudentType.STAFF_CHILD:
        label = "Staff child fee"
    else:
        label = "Scholarship fee"

    message = f"{label}: {amount:g}"
    if amount > HIGH_FEE_THRESHOLD:
        message += "\nHigh fee"
    return message


def process_all(students: list[dict]) -> dict[str, float]:
    """Return the calculated fee for every student."""
    results = {}
    for student in students:
        results[student["name"]] = tuition_fee(
            student["courses"],
            student["type"],
            student["summer"],
        )
    return results
