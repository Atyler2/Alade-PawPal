# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```

## 🧪 Testing PawPal+

python -m pytest
-test_owner_and_pet_relationships
-checks if owner can stor preferences,add pet and link the pet.
-test_task_priority_and_feasibility
-verfies priority scoring and whether a task fits given time
-test_daily_plan_generation_selects_tasks_within_time
-makes sure plan selects high priority that is within the owners time frame
-test_explain_plan_returns_reasoning_strings
-plan explanation includes the sleected task by name
-test_filter_tasks_by_completion_status
-does filering tasks go into completed or incompleted correctly

- test_filter_tasks_by_pet_name
  -checks if filter task by specific name
  -test_scheduler_detects_same_pet_time_conflicts - makes sure one warning is made for identical times
  -test_scheduler_detects_different_pet_time_conflicts
  -makes sure one warning is made for different times
  -test_mark_complete_creates_next_daily_and_weekly_occurrences
  -verifies recurring tasks

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

````
# Paste your pytest output here
```plugins: anyio-4.13.0
collected 11 items

tests\test_pawpal.py ..                                                                                      [ 18%]
tests\test_pawpal_system.py .........                                                                        [100%]

=============================================== 11 passed in 0.14s ================================================

## 📐 Smarter Scheduling

### Features
- Sorting by time: tasks can be ordered by `preferred_time` in `HH:MM` format.
- Filtering tasks: tasks can be filtered by completion status or by pet name.
- Conflict warnings: the scheduler returns warnings when multiple tasks share the same scheduled time.
- Daily recurrence: recurring tasks can auto-create the next occurrence for daily or weekly schedules.
- Priority-based planning: the plan selects tasks that fit within the owner’s available time and priority constraints.

## Demo Walkthrough

### Main UI features
- Enter owner and pet details, including available daily time.
- Add tasks with a title, duration, priority, and preferred time.
- Generate a schedule and view the planned tasks in a clear table.
- See conflict warnings when multiple tasks are assigned the same time.
- Review sorted tasks, completed/incomplete tasks, and pet-specific task views.

### Example workflow
1. Add a pet and set the owner’s available time.
2. Add one or more care tasks such as walks, feeding, or grooming.
3. Generate the schedule to see which tasks fit the day.
4. Review the time-sorted task list and any conflict warnings.
5. Mark a task complete and see how recurring tasks are handled.

### Key Scheduler behaviors shown
- Sorting by time: tasks are displayed in chronological order using `preferred_time`.
- Conflict warnings: overlapping same-time tasks raise a warning message.
- Filtering: tasks can be filtered by completion status or by pet name.
- Recurring tasks: completing a daily or weekly task creates the next occurrence automatically.

### Sample CLI output from `main.py`
```text
Tasks in the plan before sorting:
- Play (Tala, 09:00, medium)
- Wash (Tala, 09:00, medium)
- Walk (Tala, 07:15, high)
- Brush Luna (Luna, 10:00, low)

Tasks sorted by priority:
- Walk (07:15, high)
- Play (09:00, medium)
- Wash (09:00, medium)
- Brush Luna (10:00, low)

Tasks sorted by preferred time:
- Walk (07:15, high)
- Play (09:00, medium)
- Wash (09:00, medium)
- Brush Luna (10:00, low)

Conflict check:
Warning: tasks scheduled at the same time: 'Play' (Tala), 'Wash' (Tala).

Completed tasks:
- Wash

Incomplete tasks:
- Walk
- Play
- Brush Luna

Tasks filtered by pet name 'Tala':
- Walk (Tala)
- Play (Tala)
- Wash (Tala)
```
````
