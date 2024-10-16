# Задача 1. Анализ цен
# Нашему другу заказали написать программу, которая анализирует цены на бирже. Она получает этот пакет данных, но делать
# что-либо с ним нельзя. Для нормальной работы аналитической программы берётся новый список, который равен тому, что
# пришло. Затем идёт работа с новым списком: если есть отрицательные цены, то программа их зануляет и в конце выводит на
# экран, сколько денег мы по итогу потеряли. Получился вот такой код:
#
# original_prices = [-12, 3, 5, -2, 1]
#
# new_prices = original_prices
#
# for i in range(len(original_prices)):
#
#     if new_prices[i] < 0:
#
#         new_prices[i] = 0
#
# print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))
#
# Однако при таких входных данных программа почему-то работает неправильно: она выводит ответ 0, когда правильный
# ответ 14. Помогите другу исправить программу, а также сделайте так, чтобы список цен генерировался случайно
# (диапазон можно выбрать любой).

# Без генерации

# original_prices = [-12, 3, 5, -2, 1]
#
# new_prices = original_prices[:]
#
# for i in range(len(original_prices)):
#     if new_prices[i] < 0:
#         new_prices[i] = 0
#
# print("Мы потеряли: ", abs(sum(original_prices) - sum(new_prices)))

# С генерацией

import random

original_prices = [random.randint(-10, 10) for _ in range(5)]
new_prices = original_prices[:]
new_prices = [0 if num < 0 else num for num in new_prices]
print(
    f"Оригинальный список: {original_prices}\n"
    f"С обнулением отрицательных цен: {new_prices}\n"
    f"Мы потеряли: {abs(sum(original_prices) - sum(new_prices))}"
)
