from models import Task
from validators import validate_task_title

def save_tasks(tasks, filename):
    with open(filename, "w") as f:
        for task in tasks:
            try:
                validate_task_title(task.title)
                f.write(f"{task.title},{task.priority},{task.done}\n")
            except ValueError as e:
                raise ValueError(f"Invalid title for task: {task.title}. {str(e)}")
