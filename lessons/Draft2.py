def func(num):
    my_list = []
    for i in range(0, num + 1, 2):
        my_list.append(i)

    return my_list

print(func(10))