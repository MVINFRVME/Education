# Задача 2. Плагины
# Один проект состоит из огромного количества разнообразных функций, часть из которых используется в других проектах в
# качестве плагинов, то есть они как бы «подключаются» и создают дополнительный функционал.
#
# Реализуйте специальный декоратор, который будет «регистрировать» нужные функции как плагины и заносить их в
# соответствующий словарь.

from typing import Callable, Dict


PLUGINS: Dict[str, Callable] = dict()


def register(func: Callable) -> Callable:
    """Декоратор. Регистрирует функцию как плагин."""
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name: str) -> str:
    return f'Hello {name}! '


@register
def say_goodbye(name: str) -> str:
    return f'Goodbye {name}! '


print(PLUGINS)
