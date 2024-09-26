# Задача 2. Декорацию знаешь?
# На новой работе вы познакомились с middle-разработчиком на Python, который согласился научить вас всему,
# что умеет сам. Но перед этим он решил точечно проверить ваши знания. Он показал код, где один и тот же
# декоратор логирования использовался для каждого метода класса отдельно:
# Зная, что классы тоже можно декорировать, вы сразу поняли, как можно упростить код.
#
# Реализуйте декоратор logging, который должен декорировать класс и логировать каждый метод в нём.
# Логирование реализуйте на своё усмотрение:
# это может быть, например, вывод названия метода, его аргов, кваргов и документации на экран;
# либо вывод всей этой информации в отдельный файл вместе с датой и временем.

from typing import Callable
from datetime import datetime
from pathlib import Path
import functools


def logging(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open(Path('logs'), 'a', encoding='utf-8') as file:
            file.write(f'{datetime.now()} - {func.__name__}\n')
        return result
    return wrapper

def for_all_methods(decorator: Callable) -> Callable:
    def decorate(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                cur_method = getattr(cls, i_method_name)
                decorated_method = decorator(cur_method)
                setattr(cls, i_method_name, decorated_method)
        return cls
    return decorate


@for_all_methods(logging)
class Methods:
    def __init__(self, num: int| float):
        self.num = num

    def square(self) -> int| float:
        return self.num ** 2

    def cube(self) -> int| float:
        return self.num ** 3


my_instance = Methods(2)
my_instance.cube()
my_instance.square()