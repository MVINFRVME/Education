import os


def print_dirs(project):
    print(f'\nСодержимое директории {project}')
    if os.path.exists(project):
        for i_elem in os.listdir(project):
            path = os.path.join(project, i_elem)
            print('    ', path)
    else:
        print('Каталога проекта не существует.')


projects_list = ['Prod', 'Education', 'Modules']
for i_project in projects_list:
    path_to_project = os.path.abspath(os.path.join('..', '..', i_project))
    print_dirs(path_to_project)
