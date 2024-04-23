# Задача 3. Игроки
# Что нужно сделать
# У вас есть словарь игроков, которые участвовали в трёх видах спорта. В словаре хранятся пары «ФИ — очки»:

players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
    }

# Один программист попросил нас прислать другой вариант хранения этой информации для его базы.
# Напишите программу, которая объединяет ключ словаря со значением в один кортеж, и выведите результат на экран.
# Постарайтесь использовать как можно более эффективное решение.

# Результат работы программы:
# [('Ivan', 'Volkin', 10, 5, 13), ('Bob', 'Robbin', 7, 5, 14), ('Rob', 'Bobbin', 12, 8, 2)]

# Советы и рекомендации
# Не забывайте, что кортежи можно складывать (а + б). Это приведёт к объединению всех элементов двух кортежей.
# Для упрощения кода хорошо подходят генераторы списка.

players_list = [i_key + i_value for i_key, i_value in players.items()]
print(players_list)
