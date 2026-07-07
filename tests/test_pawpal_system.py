from pawpal_system import DailyPlan, Owner, Pet, Task


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
