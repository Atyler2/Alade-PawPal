from pawpal_system import Owner, Pet, Scheduler, Task

owner = Owner(
    name="Alade",
    available_time_minutes=60,
    preferences=["dog walking", "grooming"],
)

pet = Pet(
    name="Tala",
    species="Dog",
    needs=["exercise", "attention"],
    notes="Loves playing fetch",
)

walk = Task(title="Walk", duration_minutes=20, priority="high",
            category="general", is_recurring=True)
wash = Task(title="Wash", duration_minutes=20, priority="medium",
            category="general", is_recurring=True, preferred_time="09:00")
play = Task(title="Play", duration_minutes=15, priority="medium",
            category="general", is_recurring=True, preferred_time="09:00")
walk = Task(title="Walk", duration_minutes=20, priority="high",
            category="general", is_recurring=True, preferred_time="07:15")

owner.add_pet(pet)
pet.add_task(play)
pet.add_task(wash)
pet.add_task(walk)

plan = Scheduler(owner=owner, pet=pet)
plan.add_task(play)
plan.add_task(wash)
plan.add_task(walk)

# Add an extra task for a second pet so filtering by pet name is visible.
other_pet = Pet(name="Luna", species="Cat")
owner.add_pet(other_pet)
other_task = Task(
    title="Brush Luna",
    duration_minutes=10,
    priority="low",
    category="grooming",
    is_recurring=True,
    preferred_time="10:00",
    pet=other_pet,
)
plan.add_task(other_task)

print("Tasks in the plan before sorting:")
for task in plan.tasks:
    pet_name = task.pet.name if task.pet else "Unknown"
    print(f"- {task.title} ({pet_name}, {task.preferred_time}, {task.priority})")

plan.sort_tasks()
print("\nTasks sorted by priority:")
for task in plan.tasks:
    print(f"- {task.title} ({task.preferred_time}, {task.priority})")

plan.sort_by_time()
print("\nTasks sorted by preferred time:")
for task in plan.tasks:
    print(f"- {task.title} ({task.preferred_time}, {task.priority})")

print("\nConflict check:")
print(plan.warn_conflicts())

# Mark one task complete, then filter.
wash.mark_complete()
completed = plan.filter_tasks(is_complete=True)
incomplete = plan.filter_tasks(is_complete=False)

print("\nCompleted tasks:")
for task in completed:
    print(f"- {task.title}")

print("\nIncomplete tasks:")
for task in incomplete:
    print(f"- {task.title}")

print("\nTasks filtered by pet name 'Tala':")
for task in plan.filter_tasks(pet_name="Tala"):
    print(f"- {task.title} ({task.pet.name})")
