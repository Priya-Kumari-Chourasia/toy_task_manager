"""Task data model and priority scoring."""


class Task:
    def __init__(self, title, priority, done=False):
        self.title = title
        self.priority = priority
        self.done = done


def calculate_priority_score(tasks):
    """Average priority across all tasks. Higher = more urgent overall."""
    if not tasks:
        return 0
    total = sum(task.priority for task in tasks)
    return total / len(tasks)