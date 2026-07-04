"""Save and load tasks from a simple text file."""

from models import Task


def save_tasks(tasks, filename):
    with open(filename, "w") as f:
        for task in tasks:
            f.write(f"{task.title},{task.priority},{task.done}\n")


def load_tasks(filename):
    """Load tasks from a file. Should handle a missing file gracefully."""
    # BUG: crashes with an unhandled FileNotFoundError if the file doesn't
    # exist yet, instead of returning an empty list (a totally normal case
    # for a brand new task list).
    tasks = []
    with open(filename, "r") as f:
        for line in f:
            title, priority, done = line.strip().split(",")
            tasks.append(Task(title, int(priority), done == "True"))
    return tasks
