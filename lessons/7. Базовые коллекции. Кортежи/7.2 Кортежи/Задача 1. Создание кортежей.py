# Задача 1. Создание кортежей
# Заполните один кортеж десятью случайными целыми числами от 0 до 5 включительно. Также заполните второй кортеж числами
# от −5 до 0. Объедините два кортежа, создав тем самым третий кортеж. С помощью метода кортежа определите в нём
# количество нулей. Выведите на экран третий кортеж и количество нулей в нём.

# import random
#
# my_list_1 = list()
# for _ in range(10):
#     my_list_1.append(random.randint(0, 5))
# tuple_1 = tuple(my_list_1)
# print(f'Первый кортеж: {tuple_1}')
#
#
# my_list_2 = list()
# for _ in range(10):
#     my_list_2.append(random.randint(-5, 0))
# tuple_2 = tuple(my_list_2)
# print(f'Второй кортеж: {tuple_2}')
#
# my_list_1.extend(my_list_2)
# tuple_3 = tuple(my_list_1)
# print(f'Объединенные кортежи: {tuple_3}')
#
# zero_count = tuple_3.count(0)
# print(f'Количество нулей: {zero_count}')

# или через list comprehension

import random


def generation(start, stop, times):
    return tuple([random.randint(start, stop) for _ in range(times)])


tup_1 = generation(0, 5, 10)
tup_2 = generation(-5, 0, 10)
common_tup = tup_1 + tup_2
print(f'{common_tup}\n'
      f'Количество нулей: {common_tup.count(0)}')
