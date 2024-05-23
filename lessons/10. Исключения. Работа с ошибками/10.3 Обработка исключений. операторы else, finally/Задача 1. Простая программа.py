# Задача 1. Простая программа
# Напишите программу, которая открывает файл и записывает туда введённую пользователем строку. Используйте операторы try
# except else finally. Обработайте возможные ошибки:

# 1. Проблема при открытии файла.
# 2. Нельзя преобразовать данные в целое.
# 3. Неожиданная ошибка.

my_file = None

try:
    my_file = open('file.txt', 'w', encoding='utf-8')
    user_text = input('Введите текст: ')
    my_file.write(user_text)

except (FileNotFoundError, IsADirectoryError, PermissionError) as exc:
    print(f'{type(exc)} - Проблемы при открытии файла')
except ValueError as exc:
    print(f'{type(exc)} - Нельзя преобразовать данные в целое')
except Exception as exc:
    print(f'{type(exc)} - Неожиданная ошибка')

else:
    print('Запись прошла успешна')

finally:
    if my_file and not my_file.closed:
        my_file.close()
