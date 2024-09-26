# Задача 1. Повторение кода# В одной из практик вы уже писали декоратор do_twice, который повторяет вызов декорируемой
# функции два раза. В этот раз реализуйте декоратор repeat, который повторяет задекорированную функцию уже n раз.


from collections.abc import Callable
import functools


def repeat(n: int) -> Callable:
    def repeat_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return repeat_decorator


@repeat(3)
def test(name):
    print(f'Hello! {name}')


test('Митклуксикс')
