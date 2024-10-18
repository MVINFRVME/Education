# Задача 1. Двойной вызов
# Реализуйте декоратор do_twice, который дважды вызывает декорируемую функцию. Не забывайте про документацию и аннотации
# типов.
#
# Пример декорируемой функции:
# def greeting(name):
#     print('Привет, {name}!'.format(name=name))
#
# Основной код:
# greeting('Tom')
#
# Результат:
# Привет, Tom!
# Привет, Tom!

from typing import Callable, Any


def do_twice(func: Callable) -> Callable:
    """Декоратор, дублирующий функцию"""

    def wrapped_func(*args, **kwargs) -> Any:
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapped_func


@do_twice # greeting = do_twice(greeting)
def greeting(name):
    print('Привет, {name}!'.format(name=name))


greeting('Tom')
