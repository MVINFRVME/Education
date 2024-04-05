# Задание 3. Файлы
# Что нужно сделать
# В IT-компании есть негласные правила именования текстовых документов:
#
# Название файла не может начинаться с одного из специальных символов: @, №, $, %, ^, &, *, ().
# Файл должен заканчиваться расширением .txt или .docx.
# Напишите программу, которая получает на вход полное название файла и проверяет, соответствует ли он этим правилам.
#
# Пример 1
#
# Название файла: @example.txt.
# Ошибка: название начинается недопустимым символом.
#
# Пример 2
#
# Название файла: example.ttx.
# Ошибка: неверное расширение файла. Ожидалось .txt или .docx.
#
# Пример 3
#
# Название файла: example.txt.
# Файл назван верно.
#
# Советы и рекомендации
# Метод endswith (как и startswith) можно использовать для проверки нескольких окончаний.

file_name = input('Название файла: ')

invalid_symbols = ('@', '№', '$', '%', '^', '&', '*', '()')
valid_extensions = ('.txt', '.docx')
if file_name.startswith(invalid_symbols):
    print('Название начинается недопустимым символом.')
elif not file_name.endswith(valid_extensions):
    print('Неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')
