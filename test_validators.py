from validators import validate_task_title
import pytest


def test_valid_title():
    assert validate_task_title("Write report") is True


def test_rejects_non_string():
    with pytest.raises(TypeError):
        validate_task_title(123)


def test_rejects_empty_title():
    # Currently FAILS -- exposes the seeded bug (empty string not rejected)
    with pytest.raises(ValueError):
        validate_task_title("")


def test_rejects_whitespace_title():
    # Currently FAILS -- exposes the seeded bug (whitespace not rejected)
    with pytest.raises(ValueError):
        validate_task_title("   ")
