# Задача 3. Простые числа
# Реализуйте класс-итератор Primes, который принимает максимальное число N и выдаёт все простые числа от 1 до N.
#
# Основной код:
#
# prime_nums = Primes(50)
# for i_elem in prime_nums:
#     print(i_elem, end=' ')
#
# Ожидаемый результат кода:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47

class Primes:
    def __init__(self, limit):
        self.__limit = limit
        self.__count = 1

    def __iter__(self):
        self.__count = 1
        return self

    def __next__(self):
        while True:
            if self.__count <= self.__limit:
                self.__count += 1
                for i in range(2, self.__count):
                    if self.__count % i == 0:
                        break
                else:
                    return self.__count
            else:
                raise StopIteration


prime_nums = Primes(50)
for i_elem in prime_nums:
    print(i_elem, end=' ')
