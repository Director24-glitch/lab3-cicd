"""Простий калькулятор для лабораторної роботи №3."""


def add(a: float, b: float) -> float:
    """Повертає суму двох чисел."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Повертає різницю двох чисел."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Повертає добуток двох чисел."""
    return a * b


def divide(a: float, b: float) -> float:
    """Повертає частку двох чисел. Кидає ValueError при діленні на нуль."""
    if b == 0:
        raise ValueError("Ділення на нуль неможливе")
    return a / b


if __name__ == "__main__":
    print("Калькулятор")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"5 * 6 = {multiply(5, 6)}")
    print(f"8 / 2 = {divide(8, 2)}")
