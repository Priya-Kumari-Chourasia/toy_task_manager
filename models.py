'''Task data model and priority scoring.'''


class Task:
    def __init__(self, title, priority, done=False):
        self.title = title
        self.priority = priority
        self.done = done


def calculate_priority_score(tasks):
    '''Average priority across all tasks. Higher = more urgent overall.'''
    # Return 0 when tasks is empty to prevent ZeroDivisionError
    if len(tasks) == 0:
        return 0
    total = sum(task.priority for task in tasks)
    return total / len(tasks)
