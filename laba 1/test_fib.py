"""Тесты для сопрограммы Фибоначчи."""

import unittest

from gen_fib import fib_coroutine, my_genn


class TestFibCoroutine(unittest.TestCase):
    """Тесты для сопрограммы my_genn."""

    def test_zero_elements(self) -> None:
        """Проверяет генерацию нуля элементов."""
        prepared_gen = fib_coroutine(my_genn)
        gen = prepared_gen()
        self.assertEqual(gen.send(0), [])

    def test_one_element(self) -> None:
        """Проверяет генерацию одного элемента."""
        prepared_gen = fib_coroutine(my_genn)
        gen = prepared_gen()
        self.assertEqual(gen.send(1), [0])

    def test_three_elements(self) -> None:
        """Проверяет генерацию трех элементов."""
        prepared_gen = fib_coroutine(my_genn)
        gen = prepared_gen()
        self.assertEqual(gen.send(3), [0, 1, 1])

    def test_five_elements(self) -> None:
        """Проверяет генерацию пяти элементов."""
        prepared_gen = fib_coroutine(my_genn)
        gen = prepared_gen()
        self.assertEqual(gen.send(5), [0, 1, 1, 2, 3])

    def test_eight_elements(self) -> None:
        """Проверяет генерацию восьми элементов."""
        prepared_gen = fib_coroutine(my_genn)
        gen = prepared_gen()
        self.assertEqual(gen.send(8), [0, 1, 1, 2, 3, 5, 8, 13])


if __name__ == "__main__":
    unittest.main()