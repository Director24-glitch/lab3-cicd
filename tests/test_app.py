import pytest
from app import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(5, 5) == 0
    assert subtract(0, 3) == -3


def test_multiply():
    assert multiply(5, 6) == 30
    assert multiply(0, 100) == 0
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(8, 2) == 4
    assert divide(9, 3) == 3
    assert divide(1, 2) == 0.5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Ділення на нуль"):
        divide(10, 0)
