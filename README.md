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
-test_scheduler_detects_same_pet_time_conflicts
    - makes sure one warning is made for identical times
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

```
# Paste your pytest output here
```plugins: anyio-4.13.0
collected 11 items                                                                                                 

tests\test_pawpal.py ..                                                                                      [ 18%]
tests\test_pawpal_system.py .........                                                                        [100%]

=============================================== 11 passed in 0.14s ================================================

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.
- Scheduler
    - orders tasks by peferred times
    -missing times goes last
-Filtering
    -keeps completed or incomplete task
-conflict detections
    -returns warning strings for time matches
-recurring tasks
    -auto creates the next occurence

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | | e.g., by priority, duration |
| Filtering | | e.g., skip tasks if time runs out |
| Conflict handling | | e.g., overlapping time slots |
| Recurring tasks | | e.g., daily vs. weekly |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
