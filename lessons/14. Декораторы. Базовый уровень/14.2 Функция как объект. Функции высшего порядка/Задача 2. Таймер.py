# Задача 2. Таймер
# Вы работаете в отделе тестирования, и вам поручили с помощью различных функций замерить скорость передачи данных на
# нескольких десятках сайтов. Конечно же, вручную «щёлкать» сайты и замерять время вам было лень, поэтому возникла идея
# написать «автотест», который всё сделает сам.
# С помощью понятия функции высшего порядка реализуйте функцию-таймер, которая замеряет время работы переданной функции
# func и выдаёт ответ на экран.
# Проверьте работу таймера на какой-нибудь «тяжеловесной» функции.

from typing import Callable, Any
import time


def timer(func: Callable, *args, **kwargs) -> Any:
    start_point = time.time()
    result = func(*args, **kwargs)
    end_point = time.time()
    run_time = round(end_point - start_point, 4)
    print(f'Функция работала: {run_time} cек.')
    return result


def cubes_sum(number) -> int:
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 3 for i_num in range(100000)])

    return result


def squares_sum() -> int:
    number = 100
    result = 0
    for _ in range(number + 1):
        result += sum([i_num ** 2 for i_num in range(100000)])

    return result


print(timer(cubes_sum, 10))
print(timer(squares_sum))
