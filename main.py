"""Small CLI-style entry point tying the pieces together."""

from models import Task, calculate_priority_score
from validators import validate_task_title
from storage import save_tasks, load_tasks


def add_task(tasks, title, priority):
    validate_task_title(title)
    tasks.append(Task(title, priority))
    return tasks


if __name__ == "__main__":
    tasks = load_tasks("tasks.txt")
    tasks = add_task(tasks, "Write report", 3)
    print("Average priority:", calculate_priority_score(tasks))
    save_tasks(tasks, "tasks.txt")
