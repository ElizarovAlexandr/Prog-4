"""Модуль с итераторами для поиска чисел Фибоначчи в списке."""

from math import isqrt
from collections.abc import Sequence


def is_fibonacci(number: int) -> bool:
    """Проверяет, является ли число элементом ряда Фибоначчи."""
    if number < 0:
        return False

    first_value = 5 * number ** 2 + 4
    second_value = 5 * number ** 2 - 4

    return (
        isqrt(first_value) ** 2 == first_value
        or isqrt(second_value) ** 2 == second_value
    )


class FibonacchiLst:
    """Итератор через __iter__ и __next__ для чисел Фибоначчи."""

    def __init__(self, numbers: Sequence[int]) -> None:
        """Инициализирует итератор."""
        self.numbers = numbers
        self.index = 0

    def __iter__(self) -> "FibonacchiLst":
        """Возвращает объект итератора."""
        return self

    def __next__(self) -> int:
        """Возвращает следующий элемент списка, входящий в ряд Фибоначчи."""
        while self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1

            if is_fibonacci(value):
                return value

        raise StopIteration


class FibonacchiLstGetItem:
    """Итератор через __getitem__ для чисел Фибоначчи."""

    def __init__(self, numbers: Sequence[int]) -> None:
        """Сохраняет только элементы, входящие в ряд Фибоначчи."""
        self.fibonacci_numbers = [
            number for number in numbers if is_fibonacci(number)
        ]

    def __getitem__(self, index: int) -> int:
        """Возвращает элемент по индексу."""
        return self.fibonacci_numbers[index]