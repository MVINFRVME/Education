import os
from typing import Generator


def gen_files_path(target_directory: str = "/", folder_name: str = "") -> Generator[str, None, None]:
    """
    Рекурсивно генерирует пути всех файлов, находящихся в указанной папке и ее подкаталогах.

    :param target_directory: Директория для начала поиска (по умолчанию корневой диск).
    :param folder_name: Имя папки, для которой нужно найти файлы.
    :return: Генератор строк с путями файлов.
    """
    print(f"Начинаем поиск в директории: {target_directory}")

    # Проходим по всем каталогам и файлам
    for root, dirs, files in os.walk(target_directory):
        print(f"Проверяем каталог: {root}")

        # Если текущий каталог совпадает с искомым
        if os.path.basename(root) == folder_name:
            print(f"Найдена целевая папка: {root}")
            # Генерируем пути всех файлов в найденной папке
            for file in files:
                file_path = os.path.join(root, file)
                print(f"Найден файл: {file_path}")
                yield file_path


# Пример использования
if __name__ == "__main__":
    folder_to_search = input("Введите имя папки для поиска: ")
    file_paths = gen_files_path(folder_name=folder_to_search)

    print("\nНайденные файлы:")
    for path in file_paths:
        print(path)