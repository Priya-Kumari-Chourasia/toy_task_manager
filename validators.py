def validate_task_title(title):
    """Should reject empty or whitespace-only titles."""
    if not isinstance(title, str) or title.strip() == "":
        raise ValueError("Task title cannot be empty or whitespace-only")
