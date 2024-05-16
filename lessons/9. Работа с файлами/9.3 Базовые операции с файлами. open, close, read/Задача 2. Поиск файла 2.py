# Задача 2. Поиск файла 2
# Как мы помним, скрипты — это просто куча строк текста, хоть они и понятны только программисту. Таким образом, с ними
# можно работать точно так же, как и с обычными текстовыми файлами.
#
# Используя функцию поиска файла из предыдущего урока, реализуйте программу, которая находит внутри указанного пути все
# файлы с искомым названием и выводит на экран текст одного из них (выбор можно сгенерировать случайно).
# Подсказка: можно использовать, например, список для сохранения найденного пути.

import os
import random


def find_file(cur_path, files, paths=None):
    paths = paths or []
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if i_elem in files:
            paths.append(path)
        elif os.path.isdir(path):
            result = find_file(path, files)
            if result:
                paths.extend(result)

    return paths


def read_and_print(path):
    file = open(path, 'r', encoding='utf-8')
    for i_line in file:
        print(i_line)
    file.close()


searching_files = ('shrek', 'fiona')
my_path = os.path.abspath(os.path.join(os.path.sep, 'Education', 'test dir'))
my_paths = find_file(my_path, searching_files)
read_and_print(random.choice(my_paths))
