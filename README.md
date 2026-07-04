# Toy Task Manager

A slightly larger, multi-file toy repo for stress-testing the issue-fixer
agent beyond a single-file codebase. Used as "Level 1" testing per the
project's testing plan.

## Structure
- `models.py` -- Task class + priority scoring
- `validators.py` -- input validation
- `storage.py` -- save/load tasks from a file (imports from `models.py`)
- `main.py` -- ties everything together

## Known seeded bugs (see Issues tab)
1. `calculate_priority_score()` crashes on an empty task list
2. `validate_task_title()` doesn't reject empty/whitespace-only titles
3. `load_tasks()` crashes if the file doesn't exist yet, instead of
   returning an empty list
