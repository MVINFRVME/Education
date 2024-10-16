# Задача 1. Машина 3
# Вам предстоит снова немного видоизменить класс Toyota из прошлого урока. На всякий случай вот описание класса.

# Четыре атрибута:

# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Два метода:

# Отображение информации об объекте класса.
# Метод, который позволяет устанавливать текущую скорость машины.
# Теперь все четыре атрибута должны инициализироваться при создании экземпляра класса (то есть передаваться в init).
# Реализуйте такое изменение класса.

class Toyota:

    def __init__(self, color='red', price='10000', max_speed=200, cur_speed=0):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.cur_speed = cur_speed

    def show_info(self):
        print('Color: {}\nPrice: {}\nMax speed: {}\nCurrent speed: {}\n'
             .format(self.color, self.price, self.max_speed, self.cur_speed))

    def change_speed(self, speed):
        self.cur_speed = speed


car = Toyota()
car = Toyota('green', max_speed=230)
car.show_info()
car.change_speed(10)
car.show_info()
