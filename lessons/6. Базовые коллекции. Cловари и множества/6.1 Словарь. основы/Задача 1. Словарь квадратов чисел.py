# Задача 1. Словарь квадратов чисел
# На вход программе поступает целое число num. Напишите программу создания словаря, который включает в себя ключи
# от 1 до num, а значениями соответствующего ключа будет значение ключа в квадрате.
#
# Пример:
# Введите целое число: 5
# Результат: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

num = int(input("Введите целое число: "))
square_nums_dict = {}
for i_num in range(1, num + 1):
    square_nums_dict[i_num] = i_num**2

print(f"Результат: {square_nums_dict}")
