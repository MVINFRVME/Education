# Задача 2. Таймер 2
# Для замера времени передачи различных данных на множество сайтов вы написали специальную функцию, которая сделала всю
# работу за вас, что позволило большую часть времени смотреть видео с котиками в интернете. Однако, увидев свой код, вы
# как программист с опытом поняли, что этот код можно написать намного красивее и удобнее.
#
# Реализуйте декоратор, который замеряет время работы задекорированной функции и выводит ответ на экран. Для проверки
# примените декоратор к какой-нибудь «тяжеловесной» функции и вызовите её в основной программе.

from time import time
from typing import Callable


def timer(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs):
        start_at = time()
        result = func(*args, **kwargs)
        end_at = time()
        run_time = round(end_at - start_at, 4)
        print(f'Функция работала {run_time} сек.')
        return result
    return wrapped_func


@timer
def sum_cubes(limit):
    summ = 0
    for num in range(1, limit + 1):
        summ += num ** 3
    return summ


print(sum_cubes(10157700))
