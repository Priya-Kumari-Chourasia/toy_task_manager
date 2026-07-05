"""Input validation helpers used before creating or saving tasks."""


def validate_task_title(title):
    """Should reject empty or whitespace-only titles."""
    if not isinstance(title, str):
        raise TypeError("Task title must be a string")
    if title.strip() == "":
        raise ValueError("Task title cannot be empty or whitespace-only")
    return True