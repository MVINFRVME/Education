# Задание 7. IP-адрес 2
# Что нужно сделать
# При написании клиент-серверного приложения часто приходится работать с IP-адресами. Как вы уже знаете, IP-адрес
# состоит из четырёх целых чисел в диапазоне от 0 до 255, разделённых точками.
# Пользователь вводит строку. Напишите программу, которая определяет, действительно ли заданная строка — правильный
# IP-адрес. Обеспечьте контроль ввода, где предусматривается добавление целых чисел от 0 до 255 и точек между ними.
#
# Пример 1
# Введите IP: 128.16.35.a4
# a4 — это не целое число.
#
# Пример 2
# Введите IP: 240.127.56.340
# 340 превышает 255.
#
# Пример 3
# Введите IP: 34.56.42,5
# Адрес — это четыре числа, разделённые точками.
#
# Пример 4
# Введите IP: 128.0.0.255
# IP-адрес корректен.


def dot_check(value):
    if len(value) == 4:
        return True
    else:
        print("Адрес — это четыре числа, разделённые точками.")


def digit_check(value):
    for num in value:
        if not num.isdigit():
            print(f"{num} - это не целое число.")
            break
    else:
        return True


def num_range(value):
    for num in value:
        if int(num) > 255:
            print(f"{num} превышает 255.")
            break
        elif int(num) < 0:
            print(f"{num} меньше 0.")
            break
    else:
        return True


ip = input("Введите IP: ").split(".")
if dot_check(ip) and digit_check(ip) and num_range(ip):
    print("IP-адрес корректен.")
