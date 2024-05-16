# Задача 2. Всё в одном
# Ваш друг, который тоже проходит курс Python Basic, поехал с ноутбуком в другой город, и там у него случилась беда:
# его диск пришлось отформатировать, а доступ в интернет отсутствует. Остался только телефон с мобильным интернетом.
# Так как со связью (и с памятью) проблемы, друг попросил вас скинуть одним файлом все решения и скрипты, которые у вас
# сейчас есть.

# Напишите программу, которая копирует код каждого скрипта в папке проекта python_basic в файл scripts.txt, разделяя код
# строкой из 40 символов *.
# ****************************************

import os


def find_file(cur_path, paths=None):
    paths = paths or []
    for i_elem in os.listdir(cur_path):
        path = os.path.abspath(os.path.join(cur_path, i_elem))
        if os.path.isfile(path):
            paths.append(path)
        else:
            paths.extend(find_file(path))
    return paths


def get_text(paths):
    script_file = open('scripts.txt', 'a', encoding='utf-8')
    for path in paths:
        text_file = open(path, 'r', encoding='utf-8')
        text = text_file.read()
        script_file.write(text)
        script_file.write('\n****************************************\n')
        text_file.close()

    script_file.close()


my_path = os.path.abspath(os.path.join('.'))
file_paths = find_file(my_path)
get_text(file_paths)

