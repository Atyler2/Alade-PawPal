from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Owner:
    """Represents the pet owner and their scheduling preferences."""

    name: str
    available_time_minutes: int = 180
    preferences: List[str] = field(default_factory=list)
    pets: List["Pet"] = field(default_factory=list)

    def add_preference(self, preference: str) -> None:
        """Add a new owner preference if it is not already present."""
        if preference and preference not in self.preferences:
            self.preferences.append(preference)

    def update_available_time(self, minutes: int) -> None:
        """Set the owner's available time to a non-negative value."""
        self.available_time_minutes = max(0, minutes)

    def add_pet(self, pet: "Pet") -> None:
        """Attach a pet to this owner if it is not already linked."""
        if pet not in self.pets:
            self.pets.append(pet)
            pet.owner = self

    def remove_pet(self, pet_name: str) -> None:
        """Remove a pet from this owner by matching its name."""
        matching_pet = next(
            (pet for pet in self.pets if pet.name == pet_name), None)
        if matching_pet is not None:
            self.pets.remove(matching_pet)
            matching_pet.owner = None


@dataclass
class Pet:
    """Represents the pet whose care tasks need to be planned."""

    name: str
    species: str
    needs: List[str] = field(default_factory=list)
    notes: Optional[str] = None
    owner: Optional["Owner"] = None
    tasks: List["Task"] = field(default_factory=list)

    def add_need(self, need: str) -> None:
        """Add a care need to the pet if it is not already listed."""
        if need and need not in self.needs:
            self.needs.append(need)

    def update_notes(self, notes: str) -> None:
        """Update the pet's notes with new information."""
        self.notes = notes

    def add_task(self, task: "Task") -> None:
        """Attach a task to this pet if it is not already present."""
        if task not in self.tasks:
            self.tasks.append(task)
            task.pet = self

    def remove_task(self, task_title: str) -> None:
        """Remove a task from this pet by matching its title."""
        for task in self.tasks:
            if task.title == task_title:
                self.tasks.remove(task)
                task.pet = None
                break


@dataclass
class Task:
    """Represents a single pet care task that can be scheduled."""

    title: str
    duration_minutes: int
    priority: str = "medium"
    category: str = "general"
    is_recurring: bool = False
    preferred_time: Optional[str] = None
    pet: Optional["Pet"] = None
    is_complete: bool = False

    def get_priority_score(self) -> int:
        """Return a numeric score for the task's priority."""
        priority_map = {"low": 1, "medium": 2, "high": 3}
        return priority_map.get(self.priority.lower(), 2)

    def is_feasible(self, available_minutes: int) -> bool:
        """Return whether the task fits within the available time."""
        return self.duration_minutes <= max(0, available_minutes)

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.is_complete = True


@dataclass
class DailyPlan:
    """Builds and explains a daily plan for the pet owner."""

    owner: Owner
    pet: Pet
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to the plan if it is not already included."""
        if task not in self.tasks:
            self.tasks.append(task)
            if task.pet is None:
                task.pet = self.pet

    def remove_task(self, task_title: str) -> None:
        """Remove a task from the plan by matching its title."""
        self.tasks = [task for task in self.tasks if task.title != task_title]

    def sort_tasks(self) -> None:
        """Sort tasks by priority, duration, and title."""
        self.tasks = sorted(
            self.tasks,
            key=lambda task: (-task.get_priority_score(),
                              task.duration_minutes, task.title.lower()),
        )

    def generate_plan(self) -> List[Task]:
        """Create a feasible schedule within the owner's available time."""
        available_time = self.owner.available_time_minutes
        candidate_tasks = list(
            self.tasks) if self.tasks else list(self.pet.tasks)
        selected_tasks: List[Task] = []

        for task in sorted(
            candidate_tasks,
            key=lambda task: (-task.get_priority_score(),
                              task.duration_minutes, task.title.lower()),
        ):
            if task in selected_tasks:
                continue
            if task.is_feasible(available_time):
                selected_tasks.append(task)
                available_time -= task.duration_minutes

        self.tasks = selected_tasks
        return selected_tasks

    def explain_plan(self) -> List[str]:
        """Return a short reason for each task in the final plan."""
        if not self.tasks:
            self.generate_plan()

        if not self.tasks:
            return ["No tasks fit in the available time for today."]

        explanations: List[str] = []
        for task in self.tasks:
            explanations.append(
                f"{task.title} was included because it is a {task.priority} priority task "
                f"that fits within the remaining time."
            )
        return explanations
