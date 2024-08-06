import os

def gen_files_path(name: str, directory: str='F:/'):

    for dirpath, dirnames, filenames in os.walk(directory):
        for dirname in dirnames:
            if dirname.lower() == name.lower():
                print(f'''Искомая папка: {dirpath}/{dirname}
Встретились файлы: ''')
                for i in filenames:
                    yield f'{dirpath}/{i}'


for _ in gen_files_path('module10'):
    print(_)

