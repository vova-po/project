import pytest
from project.main import add_numbers

def test_add_positive_numbers():
    """Тест для додавання двох додатних чисел."""
    assert add_numbers(3, 5) == 8

def test_add_negative_numbers():
    """Тест для додавання двох від'ємних чисел."""
    assert add_numbers(-3, -7) == -10

def test_add_mixed_numbers():
    """Тест для додавання додатного і від'ємного числа."""
    assert add_numbers(10, -4) == 6