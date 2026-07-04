from models import Task, calculate_priority_score
import pytest


def test_priority_score_normal():
    tasks = [Task("A", 3), Task("B", 5)]
    assert calculate_priority_score(tasks) == 4.0


def test_priority_score_empty_list():
    # Currently FAILS -- exposes the seeded bug (ZeroDivisionError)
    with pytest.raises(ValueError):
        calculate_priority_score([])
