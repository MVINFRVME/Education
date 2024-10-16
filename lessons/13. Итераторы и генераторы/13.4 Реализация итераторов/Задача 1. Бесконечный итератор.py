# Задача 1. Бесконечный итератор
# Реализуйте итератор-счётчик, который не принимает никаких атрибутов и имеет только один статический атрибут — счётчик.
# Итератор увеличивает счётчик и возвращает предыдущее значение. У вас должен получиться бесконечный итератор.
#
# То есть при вызове такого кода в основной программе
#
# my_iter = СountIterator()
# for i_elem in my_iter:
#     print(i_elem)
# значения будут выдаваться бесконечно.

class CountIterator:
    __count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.__count += 1
        return self.__count


my_iter = CountIterator()
for i_elem in my_iter:
    print(i_elem)

# class CountIterator:
#     count = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         CountIterator.count += 1
#         return CountIterator.count - 1
#
#
# my_iter = CountIterator()
