# Задача 4. Уникальный шифр
# Контекст
# Представьте, что вы — детектив, который получил загадочное письмо с шифровкой. Нужно найти количество
# уникальных символов в письме, чтобы разгадать его и раскрыть тайну.
#
# Задача.
# Напишите функцию, которая принимает строку и возвращает количество уникальных символов в строке.
# Используйте для выполнения задачи lambda-функции и map и/или filter.
#
# Сделайте так, чтобы алгоритм НЕ был регистрозависим: буквы разного регистра должны считаться одинаковыми.
#
# Советы
# 1. Работать с регистрами помогут методы строк lower/upper.
# 2. Уникальными считаются буквы, которые повторяются только один раз
# (например строка «аа» будет содержать 0 уникальных букв).

# Пример:
# message = "Today is a beautiful day! The sun is shining and the birds are singing."
# unique_count = count_unique_characters(message)
# print("Количество уникальных символов в строке:", unique_count)
# Вывод: количество уникальных символов в строке — 5.

from collections import Counter


def count_unique_characters(string: str) -> int:
    """Функция, которая принимает строку и возвращает количество уникальных символов в строке."""
    lower_list = list(map(lambda x: x.lower(), string)) # Сначала переводим в символы в нижний регистр
    cnt = Counter(lower_list) # Производим подсчет символов
    unique_list = list(filter(lambda x: x == 1, cnt.values())) # Создаем список только с уникальными символами
    return len(unique_list) # Возвращаем кол-во уникальных символов.

message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
