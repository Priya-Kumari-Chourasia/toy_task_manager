"""Input validation helpers used before creating or saving tasks."""


def validate_task_title(title):
    """Should reject empty or whitespace-only titles."""
    # BUG: doesn't check for empty/whitespace-only strings, only checks type.
    if not isinstance(title, str):
        raise TypeError("Task title must be a string")
    return True
