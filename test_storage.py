from storage import load_tasks
import os


def test_load_missing_file_returns_empty_list():
    # Currently FAILS -- exposes the seeded bug (unhandled FileNotFoundError)
    if os.path.exists("nonexistent_tasks.txt"):
        os.remove("nonexistent_tasks.txt")
    result = load_tasks("nonexistent_tasks.txt")
    assert result == []
