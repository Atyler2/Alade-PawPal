from pawpal_system import DailyPlan, Owner, Pet, Task

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
            category="general", is_recurring=True)
play = Task(title="Play", duration_minutes=15, priority="medium",
            category="general", is_recurring=True)

owner.add_pet(pet)
pet.add_task(walk)
pet.add_task(wash)
pet.add_task(play)

plan = DailyPlan(owner=owner, pet=pet)
plan.add_task(walk)
plan.add_task(wash)
plan.add_task(play)

scheduled_tasks = plan.generate_plan()
print("Today's plan for", pet.name)
for task in scheduled_tasks:
    print(f"- {task.title} ({task.duration_minutes} min, {task.priority})")
