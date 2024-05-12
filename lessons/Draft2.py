import random
import os


def find_file(cur_path, file_names):
    all_paths = []
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if i_elem in file_names:
            all_paths.append(os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, file_names)
            if result:
                all_paths.extend(result)

    return all_paths


def check_file_inside(path_to_file):
    file = open(path_to_file, "r", encoding="utf8")
    for line in file:
        print(line)
    file.close()


my_path = os.path.abspath(os.path.join(os.path.sep, 'Education', 'test dir'))
paths = find_file(my_path, ("fiona", "shrek"))
check_file_inside(random.choice(paths))
