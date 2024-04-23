# Задача 2. Контакты 2
# Мы уже реализовывали телефонную книгу для Степана, однако её проблема была в том, что туда нельзя было добавить людей
# с одинаковыми именами. Надо это исправить.

# Напишите программу, которая запрашивает у пользователя имя контакта, фамилию и номер телефона, добавляет их в словарь
# и выводит на экран текущий словарь контактов. Словарь состоит из пар «Ф. И. — телефон», где Ф. И. — это составной
# ключ. Запрос на добавление идёт бесконечно (но можно задать своё условие для завершения программы). Обеспечьте
# контроль ввода: если этот человек уже есть в словаре, то выведите соответствующее сообщение.


tele_dict = dict()

while True:
    first_name = input('\nВведите имя: ')
    surname = input('Введите фамилию: ')
    telephone = input('Введите телефон: ')
    if (first_name, surname) not in tele_dict:
        tele_dict[first_name, surname] = telephone
    else:
        print('Этот человек уже есть!\n')
