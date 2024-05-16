# Задача 1. Сумма чисел
# Во входном файле numbers.txt записано N целых чисел, каждое в отдельной строке. Напишите программу, которая выводит их
# сумму в выходной файл answer.txt.

# Пример:
# Содержимое файла numbers.txt:
# 1
# 2
# 3
# 4
# 10

# Содержимое файла answer.txt
# 20

import os


numbers_file = open('numbers.txt', 'r')
summ = 0

print('Содержимое файла numbers.txt:')
for i_line in numbers_file:
    print(i_line, end='')
    clear_line = i_line.rstrip()
    summ += int(clear_line)
numbers_file.close()

answer_file = open('answer.txt', 'w')
answer_file.write(str(summ))
answer_file.close()

answer_file = open('answer.txt', 'r')
print(f'\n\nСодержимое файла answer.txt:'
      f'\n{answer_file.read()}')
answer_file.close()
