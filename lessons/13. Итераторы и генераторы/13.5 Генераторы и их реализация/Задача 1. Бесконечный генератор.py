# Задача 1. Бесконечный генератор
# По аналогии с бесконечным итератором из практики предыдущего урока, реализуйте свой счётчик-генератор, который также в
# цикле будет бесконечно выдавать значения.
#
# Дополнительно: преобразуйте (или напишите с нуля) итератор простых чисел в функцию-генератор.

# def gen():
#     count = 0
#     while True:
#         yield count
#         count += 1
#
#
# g = gen()
# for value in g:
#     print(value)
# -------------------------------------------------------
def prime_gen(limit):
    count = 1
    while count <= limit:
        count += 1
        for num in range(2, count):
            if count % num == 0:
                break
        else:
            yield count


for elem in prime_gen(50):
    print(elem, end=' ')

# ________________________________________________________

# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#             yield number
#
#
# for i in get_prime_numbers(50):
#     print(i, end='\t')
# print()
#                         ---------Учительский--------------- ?
