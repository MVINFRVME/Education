# Задача 1. Квадраты чисел
# Что нужно сделать
# Пользователь вводит число N. Напишите программу, которая генерирует последовательность из квадратов чисел от 1
# до N (1 ** 2, 2 ** 2, 3 ** 2 и так далее). Реализацию напишите тремя способами: класс-итератор, функция-генератор и
# генераторное выражение.
#
# Что оценивается
# Результат вычислений корректен.
# Input содержит корректные приглашения для ввода.
# Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
# При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
# Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
# Для создания нового класса на основе уже существующего используется наследование.
# Сообщения о процессе получения результата осмыслены и понятны для пользователя.
# Переменные, функции и собственные методы классов имеют значащие имена (не a, b, c, d).
# Классы и методы/функции имеют прописанную документацию.
# Есть аннотация типов для методов/функций и их аргументов (кроме args и kwargs). Если функция/метод ничего не
# возвращает, то используется None.


from collections.abc import Iterable


class SquareIterator:
<<<<<<< HEAD
    """Класс SquareIterator генерирует последовательность из квадратов чисел от 1 до limit

    Args:
        limit (int): передается число до которого(включительно) будет генерироваться последовательность квадратов

    Attributes:
        __limit (int): предел, до которого генерируются квадраты
        __count (int): счетчик итераций
        """
=======

>>>>>>> origin/dev
    def __init__(self, limit: int) -> None:
        self.__count = 0
        self.__limit = limit

    def __iter__(self):
<<<<<<< HEAD
        """Метод  __iter__ возвращает итератор для данного объекта.

        :return: возвращает сам объект итератора"""
        return self

    def __next__(self):
        """Метод __next__ создает следующее значение числа в квадрате

         :return self.__count ** 2: возвращает квадрат числа
         :rtype: int

         :raises StopIteration: если текущее число превышает указанный предел
         """
=======
        return self

    def __next__(self):
>>>>>>> origin/dev
        while self.__count < self.__limit:
            self.__count += 1
            return self.__count ** 2
        else:
            raise StopIteration


my_iter = SquareIterator(10)
for num in my_iter:
    print(num, end=' ')
print()
# --------------------------------------------------------------------------------


def square_generator(limit: int) -> Iterable[int]:
    for i in range(1, limit + 1):
        yield i ** 2


for num in square_generator(10):
    print(num, end=' ')
print()

# --------------------------------------------------------------------------------

squares = (num ** 2 for num in range(1, 11))
for num in square_generator(10):
    print(num, end=' ')
print()
