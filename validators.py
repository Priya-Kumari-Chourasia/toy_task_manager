def validate_task_title(title):
    if not isinstance(title, str) or title.strip() == '':
        raise TypeError("Task title must be a non-empty string")
    return True