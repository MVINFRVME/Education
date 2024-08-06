# Задача 2. Очень большой файл
# Вам на обработку пришёл огромнейший файл с данными. Настолько огромный, что при его открытии компьютер просто зависает
# , так как данные не помещаются в оперативной памяти вашего суперкомпьютера (не очень-то и «супер»).
#
# В файле numbers.txt есть N чисел, разделённых пробелами и литералом пропуска строки. Напишите программу, которая
# подсчитает общую сумму чисел в файле. Для считывания файла реализуйте специальный генератор.

from pathlib import Path


def gen(file_name):
    with open(Path(file_name), 'r', encoding='utf-8') as num_file:
        for line in num_file:
            clear_seq = line.rstrip().split()
            for num in clear_seq:
                yield int(num)


print(f'Сумма чисел в файле: {sum(gen("numbers.txt"))}')


# Ещё один вариант решения с функцией map()

# def file_parser(path_to_file):
#     with open(path_to_file) as file:
#         for line in file:
#             clear_line_sum = sum(map(int, line.rstrip().split()))
#             # https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-map/
#             yield clear_line_sum
#
#
# all_sum = 0
# for number in file_parser("numbers.txt"):
#     all_sum += number
#
# print("Вариант №2", all_sum)
