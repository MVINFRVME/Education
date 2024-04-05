# Задача 1. Шифр Цезаря 2
# Мы уже писали программу, которая шифрует строку с помощью шифра Цезаря. Напомним, что в таком способе шифрования
# каждая буква заменяется на следующую по алфавиту через K позиций по кругу.
#
# Напишите (модифицируйте) программу, которая реализует этот алгоритм шифрования. Не используйте конкатенацию и
# сделайте так, чтобы текст был в одном регистре.

def cipher_func(text, shift):
    cipher_list = [alphabet[((alphabet.index(sym)) + shift) % len(alphabet)] if sym in alphabet
                   else sym
                   for sym in text]
    cipher = ''.join(cipher_list)
    return cipher


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
user_text = input('Введите текст: ').lower()
user_shift = int(input('Введите сдвиг: '))
print(cipher_func(user_text, user_shift))


