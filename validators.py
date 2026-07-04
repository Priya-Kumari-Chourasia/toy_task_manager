"""Input validation helpers used before creating or saving tasks."""


def validate_task_title(title):
    """Should reject empty or whitespace-only titles."""
    if not isinstance(title, str) or not title.strip():
        raise TypeError("Task title must be a non-empty string")
    return True