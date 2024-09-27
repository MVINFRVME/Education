# Задача 2. Замедление кода 2# Продолжаем работать с нашим старым кодом. Ранее мы уже писали декоратор, который перед
# выполнением декорируемой функции ждёт несколько секунд. Модернизируйте этот декоратор так, чтобы количество секунд можно было передавать в качестве аргумента. По умолчанию декоратор ждёт одну секунду.# Помимо этого сделайте так, чтобы декоратор можно было использовать как с аргументами, так и без них.

from collections.abc import Callable
import functools
import time


def delay(delay_time: int = 1) -> Callable:
    def delay_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(delay_time)
            result = func(*args, **kwargs)
            return result
        return wrapper

    return delay_decorator


@delay(delay_time=3)
def test(num: int) -> int:
    return num * 2


print(test(6))
