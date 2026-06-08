"""Модуль для генерации чисел ряда Фибоначчи."""

import functools
from collections.abc import Callable, Generator


def fib_elem_gen() -> Generator[int, None, None]:
    """Генератор, возвращающий элементы ряда Фибоначчи."""
    first = 0
    second = 1

    while True:
        yield first
        first, second = second, first + second


def my_genn() -> Generator[list[int], int, None]:
    """Сопрограмма, возвращающая список чисел Фибоначчи."""
    while True:
        count = yield
        generator = fib_elem_gen()
        result = [next(generator) for _ in range(count)]
        yield result


def fib_coroutine(func: Callable) -> Callable:
    """Декоратор для автоматической инициализации сопрограммы."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        coroutine = func(*args, **kwargs)
        coroutine.send(None)
        return coroutine

    return wrapper


if __name__ == "__main__":
    prepared_gen = fib_coroutine(my_genn)
    gen = prepared_gen()
    print(gen.send(8))