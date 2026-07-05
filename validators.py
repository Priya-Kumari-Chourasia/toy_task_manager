'''Input validation helpers used before creating or saving tasks.'''

def validate_task_title(title):
    '''Should reject empty or whitespace-only titles.'''
    if not isinstance(title, str) or title.strip() == "":
        raise ValueError("Task title must be a non-empty string")
    return True