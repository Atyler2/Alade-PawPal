from datetime import date, timedelta

from pawpal_system import DailyPlan, Owner, Pet, Scheduler, Task


def test_owner_and_pet_relationships():
    owner = Owner(name="Jordan")
    pet = Pet(name="Mochi", species="dog")

    owner.add_preference("morning walks")
    owner.add_pet(pet)

    assert "morning walks" in owner.preferences
    assert pet in owner.pets
    assert pet.owner is owner


def test_task_priority_and_feasibility():
    task = Task(title="Feeding", duration_minutes=10, priority="high")

    assert task.get_priority_score() == 3
    assert task.is_feasible(15) is True
    assert task.is_feasible(5) is False


def test_daily_plan_generation_selects_tasks_within_time():
    owner = Owner(name="Jordan", available_time_minutes=40)
    pet = Pet(name="Mochi", species="dog")
    owner.add_pet(pet)

    walk = Task(title="Morning walk", duration_minutes=20, priority="high")
    feeding = Task(title="Feeding", duration_minutes=10, priority="medium")
    grooming = Task(title="Grooming", duration_minutes=30, priority="low")

    pet.add_task(walk)
    pet.add_task(feeding)
    pet.add_task(grooming)

    plan = DailyPlan(owner=owner, pet=pet)
    plan.add_task(walk)
    plan.add_task(feeding)
    plan.add_task(grooming)

    scheduled = plan.generate_plan()

    assert [task.title for task in scheduled] == ["Morning walk", "Feeding"]
    assert len(scheduled) == 2


def test_explain_plan_returns_reasoning_strings():
    owner = Owner(name="Jordan", available_time_minutes=20)
    pet = Pet(name="Mochi", species="dog")
    owner.add_pet(pet)

    task = Task(title="Medication", duration_minutes=10, priority="high")
    pet.add_task(task)

    plan = DailyPlan(owner=owner, pet=pet)
    plan.add_task(task)
    plan.generate_plan()

    explanation = plan.explain_plan()

    assert len(explanation) == 1
    assert "Medication" in explanation[0]


def test_filter_tasks_by_completion_status():
    owner = Owner(name="Jordan")
    pet = Pet(name="Mochi", species="dog")
    owner.add_pet(pet)

    task1 = Task(title="Feed", duration_minutes=10, priority="high")
    task2 = Task(title="Walk", duration_minutes=20, priority="medium")
    task2.mark_complete()

    plan = DailyPlan(owner=owner, pet=pet)
    plan.add_task(task1)
    plan.add_task(task2)

    incomplete = plan.filter_tasks(is_complete=False)
    complete = plan.filter_tasks(is_complete=True)

    assert [task.title for task in incomplete] == ["Feed"]
    assert [task.title for task in complete] == ["Walk"]


def test_filter_tasks_by_pet_name():
    owner = Owner(name="Jordan")
    pet1 = Pet(name="Mochi", species="dog")
    pet2 = Pet(name="Toby", species="cat")
    owner.add_pet(pet1)
    owner.add_pet(pet2)

    task1 = Task(title="Feed Mochi", duration_minutes=10,
                 priority="high", pet=pet1)
    task2 = Task(title="Play with Toby", duration_minutes=15,
                 priority="medium", pet=pet2)

    plan = DailyPlan(owner=owner, pet=pet1)
    plan.add_task(task1)
    plan.add_task(task2)

    machi_tasks = plan.filter_tasks(pet_name="Mochi")

    assert [task.title for task in machi_tasks] == ["Feed Mochi"]


def test_scheduler_detects_same_pet_time_conflicts():
    owner = Owner(name="Jordan")
    pet = Pet(name="Mochi", species="dog")
    owner.add_pet(pet)

    task1 = Task(title="Morning walk", duration_minutes=20,
                 priority="high", preferred_time="07:00", pet=pet)
    task2 = Task(title="Feeding", duration_minutes=10,
                 priority="medium", preferred_time="07:00", pet=pet)

    scheduler = Scheduler(owner=owner, pet=pet)
    scheduler.add_task(task1)
    scheduler.add_task(task2)

    warnings = scheduler.detect_time_conflicts()

    assert len(warnings) == 1
    assert "Morning walk" in warnings[0]
    assert "Feeding" in warnings[0]


def test_scheduler_detects_different_pet_time_conflicts():
    owner = Owner(name="Jordan")
    pet1 = Pet(name="Mochi", species="dog")
    pet2 = Pet(name="Luna", species="cat")
    owner.add_pet(pet1)
    owner.add_pet(pet2)

    task1 = Task(title="Morning walk", duration_minutes=20,
                 priority="high", preferred_time="07:00", pet=pet1)
    task2 = Task(title="Luna snack", duration_minutes=10,
                 priority="medium", preferred_time="07:00", pet=pet2)

    scheduler = Scheduler(owner=owner, pet=pet1)
    scheduler.add_task(task1)
    scheduler.add_task(task2)

    warnings = scheduler.detect_time_conflicts()

    assert len(warnings) == 1
    assert "Mochi" in warnings[0]
    assert "Luna" in warnings[0]


def test_mark_complete_creates_next_daily_and_weekly_occurrences():
    owner = Owner(name="Jordan")
    pet = Pet(name="Mochi", species="dog")
    owner.add_pet(pet)

    today = date.today()
    daily_task = Task(
        title="Daily check-in",
        duration_minutes=5,
        priority="medium",
        is_recurring=True,
        recurrence="daily",
        due_date=today,
        pet=pet,
    )
    weekly_task = Task(
        title="Weekly grooming",
        duration_minutes=30,
        priority="high",
        is_recurring=True,
        recurrence="weekly",
        due_date=today,
        pet=pet,
    )

    pet.add_task(daily_task)
    pet.add_task(weekly_task)

    next_daily = daily_task.mark_complete()
    next_weekly = weekly_task.mark_complete()

    assert next_daily is not None
    assert next_daily.due_date == today + timedelta(days=1)
    assert next_daily.recurrence == "daily"
    assert next_daily.pet is pet
    assert next_daily in pet.tasks

    assert next_weekly is not None
    assert next_weekly.due_date == today + timedelta(weeks=1)
    assert next_weekly.recurrence == "weekly"
    assert next_weekly.pet is pet
    assert next_weekly in pet.tasks
