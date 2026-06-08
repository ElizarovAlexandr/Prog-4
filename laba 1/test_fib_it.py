"""Тесты для итераторов Фибоначчи."""

import unittest

from fib_iterator import FibonacchiLst, FibonacchiLstGetItem


class TestFibIterator(unittest.TestCase):
    """Тесты обычного итератора через __iter__ и __next__."""

    def test_normal_list(self) -> None:
        """Проверяет стандартный список."""
        result = list(FibonacchiLst([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]))
        self.assertEqual(result, [0, 1, 2, 3, 5, 8, 1])

    def test_empty_list(self) -> None:
        """Проверяет пустой список."""
        result = list(FibonacchiLst([]))
        self.assertEqual(result, [])

    def test_range_ten(self) -> None:
        """Проверяет range(10)."""
        result = list(FibonacchiLst(range(10)))
        self.assertEqual(result, [0, 1, 2, 3, 5, 8])

    def test_negative_numbers(self) -> None:
        """Проверяет список с отрицательными числами."""
        result = list(FibonacchiLst([-5, -1, 0, 1, 4, 5]))
        self.assertEqual(result, [0, 1, 5])


class TestFibGetItemIterator(unittest.TestCase):
    """Тесты упрощенного итератора через __getitem__."""

    def test_normal_list(self) -> None:
        """Проверяет стандартный список."""
        result = list(FibonacchiLstGetItem([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]))
        self.assertEqual(result, [0, 1, 2, 3, 5, 8, 1])

    def test_empty_list(self) -> None:
        """Проверяет пустой список."""
        result = list(FibonacchiLstGetItem([]))
        self.assertEqual(result, [])

    def test_range_ten(self) -> None:
        """Проверяет range(10)."""
        result = list(FibonacchiLstGetItem(range(10)))
        self.assertEqual(result, [0, 1, 2, 3, 5, 8])


if __name__ == "__main__":
    unittest.main()