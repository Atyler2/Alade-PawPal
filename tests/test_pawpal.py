from pawpal_system import Pet, Task


def test_task_completion_marks_task_complete():
    task = Task(title="Walk", duration_minutes=15, priority="high")

    assert task.is_complete is False

    task.mark_complete()

    assert task.is_complete is True


def test_adding_task_increases_pet_task_count():
    pet = Pet(name="Mochi", species="dog")
    initial_count = len(pet.tasks)

    task = Task(title="Feeding", duration_minutes=10, priority="medium")
    pet.add_task(task)

    assert len(pet.tasks) == initial_count + 1
    assert task in pet.tasks
