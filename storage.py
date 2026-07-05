"""Save and load tasks from a simple text file."""

from models import Task


def save_tasks(tasks, filename):
    with open(filename, "w") as f:
        for task in tasks:
            f.write(f"{task.title},{task.priority},{task.done}\n")


def load_tasks(filename):
    """Load tasks from a file. Should handle a missing file gracefully."""
    tasks = []
    try:
        with open(filename, "r") as f:
            for line in f:
                try:
                    title, priority, done = line.strip().split(",")
                    tasks.append(Task(title, int(priority), done == "True"))
                except ValueError as e:
                    print(f"Skipping malformed task: {e}")
    except FileNotFoundError:
        print(f"File '{filename}' not found. Returning empty task list.")
    return tasks