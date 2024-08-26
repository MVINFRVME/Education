# Задача 2. Замедление кода
# Что нужно сделать
# В программировании иногда возникает ситуация, когда работу функции нужно замедлить. Типичный пример — функция,
# которая постоянно проверяет, изменились ли данные на веб-странице или её код.

# Реализуйте декоратор, который перед выполнением декорируемой функции ждёт несколько секунд.

# Что оценивается
# Результат вычислений корректен.
# Сообщения о процессе получения результата осмыслены и понятны для пользователя.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы/функции имеют прописанную документацию.
# Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs). Если функция/метод ничего не
# возвращает, то используется None.
# Во всех декораторах используется functools.wraps().


from functools import wraps
from typing import Callable
from time import sleep


def slow_down(func: Callable) -> Callable:
    """Декоратор, который перед выполнением декорируемой функции ждет несколько секунд."""
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        sleep(2)
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@slow_down
def test():
    print('123')


test()
