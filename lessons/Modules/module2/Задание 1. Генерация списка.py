# Задание 1. Генерация списка
# Что нужно сделать

# Дано целое число N. Напишите программу, которая формирует список из нечётных чисел от одного до N.
#
# Пример 1:
#
# Введите число: 1
#
# Список из нечётных чисел от одного до N: [1]
#
# Пример 2:
#
# Введите число: 14
#
# Список из нечётных чисел от одного до N: [1, 3, 5, 7, 9, 11, 13]

num = int(input("Введите число: "))
num_list = []

for i in range(1, num + 1, 2):
    num_list.append(i)

print(f"Список из нечетных чисел от одного до N: {num_list}")
