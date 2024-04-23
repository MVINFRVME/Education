# Задача 2. Универсальная программа
# Что нужно сделать
# Напишите функцию, возвращающую список элементов итерируемого объекта (кортежа, строки, списка, словаря), у которых
# индекс — это простое число.

# Для проверки на простое число напишите отдельную функцию is_prime.

# Необязательное усложнение: сделайте так, чтобы основная функция состояла только из оператора return и так же
# возвращала список.

# Пример вызова функции:
# print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# Ответ в консоли: [2, 3, 5, 7]

# Пример вызова функции:
# print(crypto('О Дивный Новый мир!'))
# Ответ в консоли: ['Д', 'и', 'н', 'й', 'в', 'й', 'р']

# Советы и рекомендации
# Для нумерации элементов используйте функцию enumerate. Это позволит работать одинаково со всеми структурами данных.

def is_prime(x):
    if x <= 1:
        return False

    for num in range(2, int(x ** 0.5) + 1):
        if x % num == 0:
            return False
    else:
        return True


def crypto(seq):
    res_list = list()
    for i_sym, sym in enumerate(seq):
        if is_prime(i_sym):
            res_list.append(sym)

    return res_list


print(crypto('О Дивный Новый мир!'))
print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Необязательное усложнение: сделайте так, чтобы основная функция состояла только из оператора return и так же
# возвращала список.

# Вот так что-ли?

#
# def is_prime(x):
#     if x <= 1:
#         return False
#
#     for num in range(2, int(x ** 0.5) + 1):
#         if x % num == 0:
#             return False
#     else:
#         return True
#
#
# def check_index(seq):
#     res_list = list()
#     for i_sym, sym in enumerate(seq):
#         if is_prime(i_sym):
#             res_list.append(sym)
#
#     return res_list
#
#
# def crypto(seq):
#     return check_index(seq)
#
#
# print(crypto('О Дивный Новый мир!'))
# print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
