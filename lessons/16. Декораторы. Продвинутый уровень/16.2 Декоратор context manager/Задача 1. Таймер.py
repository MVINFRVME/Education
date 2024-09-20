# Задача 1. Таймер
# Реализуйте функцию (не класс) timer в качестве контекст-менеджера: функция должна работать с оператором with
# и замерять время работы вложенного кода.

from collections.abc import Iterator
from contextlib import contextmanager
from time import time


@contextmanager
def timer() -> Iterator:
    start_time = time()
    try:
        yield
    except Exception as exc:
        print(exc)
    finally:
        print(time() - start_time)


with timer() as t1:
    value = 100 * 100 ** 1000000
