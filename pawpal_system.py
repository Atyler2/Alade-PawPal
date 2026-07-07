from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Owner:
    """Represents the pet owner and their scheduling preferences."""

    name: str
    available_time_minutes: int = 180
    preferences: List[str] = field(default_factory=list)

    def add_preference(self, preference: str) -> None:
        pass

    def update_available_time(self, minutes: int) -> None:
        pass


@dataclass
class Pet:
    """Represents the pet whose care tasks need to be planned."""

    name: str
    species: str
    needs: List[str] = field(default_factory=list)
    notes: Optional[str] = None

    def add_need(self, need: str) -> None:
        pass

    def update_notes(self, notes: str) -> None:
        pass


@dataclass
class Task:
    """Represents a single pet care task that can be scheduled."""

    title: str
    duration_minutes: int
    priority: str = "medium"
    category: str = "general"
    is_recurring: bool = False
    preferred_time: Optional[str] = None

    def get_priority_score(self) -> int:
        pass

    def is_feasible(self, available_minutes: int) -> bool:
        pass


@dataclass
class DailyPlan:
    """Builds and explains a daily plan for the pet owner."""

    owner: Owner
    pet: Pet
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, task_title: str) -> None:
        pass

    def sort_tasks(self) -> None:
        pass

    def generate_plan(self) -> List[Task]:
        pass

    def explain_plan(self) -> List[str]:
        pass
