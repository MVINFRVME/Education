# Задача 1. Работа с файлом
# Реализуйте класс File — контекстный менеджер для работы с файлами. Он должен принимать на вход имя файла и режим
# чтения/записи и открывать сам файл. В начале работы менеджер возвращает файловый объект, а в конце — закрывает файл.
#
# Пример основного кода:
#
# with File(‘example.txt’, ‘w’) as file:
#     file.write(‘Всем привет!’)

class File:
    def __init__(self, file_name: str, mode: str):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self) -> 'File':
        self.file = open(self.file_name, self.mode, encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True


with File('example.txt', 'w') as file:
    file.write('Всем привет!')