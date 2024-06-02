# Задача 1. Машина
# Напишите класс Toyota, состоящий из четырёх статических атрибутов:

# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Создайте три экземпляра класса и каждому из них поменяйте значение текущей скорости на случайное число от нуля до 200.

import random


class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    cur_speed = 0


car_1 = Toyota()
car_2 = Toyota()
car_3 = Toyota()
car_1.cur_speed = random.randint(0, 200)
car_2.cur_speed = random.randint(0, 200)
car_3.cur_speed = random.randint(0, 200)
print(car_1.cur_speed, car_2.cur_speed, car_3.cur_speed)
