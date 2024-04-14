# Задача 3. Удаление части
# Дан список из N чисел, а также числа А и В (можно сгенерировать случайно, при этом А < B). Напишите программу, которая
# удаляет элементы списка с индексами от А до В. Не используйте дополнительные переменные и методы списков.

import random

N = int(input("Введите кол-во чисел: "))
rand_list = [random.randint(0, 10) for _ in range(N)]
A = random.randint(0, len(rand_list))
B = random.randint(A, len(rand_list))

print(f"Список: {rand_list}\n" f"A = {A}\n" f"B = {B}\n")

rand_list = rand_list[:A] + rand_list[B:]
print(f"Модифицированный список: {rand_list}")
