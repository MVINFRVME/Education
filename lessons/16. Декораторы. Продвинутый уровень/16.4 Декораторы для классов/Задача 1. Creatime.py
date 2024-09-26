# Задача 1. Createtime
# Реализуйте декоратор класса, который выдаёт дату и время создания, а также список всех методов объекта класса
# каждый раз, когда объект класса создаётся в основном коде.

from datetime import datetime


def create_time(cls):
    def wrapper(*args, **kwargs):
        instance = cls(*args, *kwargs)
        print(f'Время создания экземпляра класса: {datetime.now()}\n'
              f'Методы: {dir(cls)}')
        return instance

    return wrapper


@create_time
class Test:
    def __init__(self):
        pass


test = Test()
