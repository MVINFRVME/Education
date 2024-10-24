# Задание 6. Двумерный список
# Что нужно сделать
# Часто в программировании приходится писать код исходя из результата, который требует заказчик.
# В этот раз ему нужно получить двумерный список:
#
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
#
# Напишите программу, которая генерирует такой список и выводит его на экран. Используйте только list comprehensions.

my_list = [[num, num + 4, num + 8] for num in range(1, 5)]
print(my_list)
