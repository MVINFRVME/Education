# Задача 1. Счётчик 2
# Как-то мы уже создавали декоратор counter, который считает и выводит количество вызовов декорируемой функции.
# Для этого мы использовали интересную особенность классов. В этот раз реализуйте тот же декоратор, но уже с
# использованием знаний о локальных и глобальных переменных.
# Реализуйте декоратор двумя способами:
# 1.используя глобальную переменную count;
# 2.используя локальную переменную count внутри декоратора.
# Дополнительно: найдите команду (в интернете или даже сами), которая перечисляет все функции и методы, находящиеся
# во встроенном пространстве имён в Python.
# Результат выполнения команды:
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__'  ну и так далее.

from typing import Callable

def counter(func: Callable):
    count = 0
    def wrapped(*args, **kwargs):
        global count
        func(*args, **kwargs)
        count += 1
        print(f'Кол-во вызовов: {count}')
    return wrapped

@counter
def test():
    return 'OK'

count = 0

for _ in range(5):
    test()



# from typing import Callable
#
# def counter(func: Callable):
#     count = 0
#     def wrapped(*args, **kwargs):
#         nonlocal count
#         func(*args, **kwargs)
#         count += 1
#         print(f'Кол-во вызовов: {count}')
#     return wrapped
#
# @counter
# def test():
#     return 'OK'
#
# for _ in range(5):
#     test()
