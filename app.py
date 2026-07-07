import streamlit as st
from pawpal_system import Owner, Pet, Scheduler, Task

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This app now uses the core PawPal classes to manage owners, pets, tasks, and scheduling.
"""
)

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan", available_time_minutes=180)
if "pet" not in st.session_state:
    st.session_state.pet = Pet(name="Mochi", species="dog")
if "plan" not in st.session_state:
    st.session_state.plan = None

owner = st.session_state.owner
pet = st.session_state.pet

st.subheader("Owner and Pet")
owner_name = st.text_input("Owner name", value=owner.name)
pet_name = st.text_input("Pet name", value=pet.name)
species = st.selectbox(
    "Species",
    ["dog", "cat", "other"],
    index=["dog", "cat", "other"].index(pet.species) if pet.species in [
        "dog", "cat", "other"] else 0,
)
available_time = st.number_input(
    "Available time (minutes)",
    min_value=1,
    max_value=480,
    value=owner.available_time_minutes,
)

if st.button("Save owner and pet"):
    owner.name = owner_name
    owner.update_available_time(int(available_time))

    if pet.name != pet_name or pet.species != species:
        new_pet = Pet(name=pet_name, species=species)
        owner.add_pet(new_pet)
        st.session_state.pet = new_pet
        pet = new_pet
    else:
        pet.name = pet_name
        pet.species = species

    st.session_state.owner = owner
    st.session_state.pet = pet
    st.session_state.plan = None
    st.success("Owner and pet saved.")

st.markdown("### Add a task")
col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input(
        "Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

preferred_time = st.text_input("Preferred time (HH:MM)", value="09:00")

if st.button("Add task"):
    task = Task(
        title=task_title,
        duration_minutes=int(duration),
        priority=priority,
        preferred_time=preferred_time or None,
    )
    pet.add_task(task)
    st.session_state.pet = pet
    st.session_state.plan = None
    st.success(f"Added {task.title} to {pet.name}'s care plan.")

if pet.tasks:
    st.subheader("Current tasks")
    task_rows = [
        {
            "title": task.title,
            "duration_minutes": task.duration_minutes,
            "priority": task.priority,
            "complete": task.is_complete,
        }
        for task in pet.tasks
    ]
    st.table(task_rows)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
if st.button("Generate schedule"):
    plan = Scheduler(owner=owner, pet=pet)
    for task in pet.tasks:
        plan.add_task(task)

    conflict_message = plan.warn_conflicts()
    if conflict_message != "No scheduling conflicts detected.":
        st.warning(conflict_message)
    else:
        st.success(conflict_message)

    plan.sort_by_time()
    st.subheader("Tasks ordered by preferred time")
    st.table(
        [
            {
                "title": task.title,
                "preferred_time": task.preferred_time,
                "duration_minutes": task.duration_minutes,
                "priority": task.priority,
            }
            for task in plan.tasks
        ]
    )

    scheduled_tasks = plan.generate_plan()
    st.session_state.plan = plan

    if scheduled_tasks:
        st.success("Plan generated!")
        st.subheader("Scheduled tasks")
        st.table(
            [
                {
                    "title": task.title,
                    "duration_minutes": task.duration_minutes,
                    "priority": task.priority,
                }
                for task in scheduled_tasks
            ]
        )

        st.subheader("Why this plan")
        for reason in plan.explain_plan():
            st.write(f"- {reason}")
    else:
        st.info("No tasks fit within the available time.")
