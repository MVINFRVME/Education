# Задача 1. Машина 2
# Модернизируйте класс Toyota из прошлого урока. Атрибуты остаются такими же:
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
#
# Добавьте два метода класса:
# Отображение информации об объекте класса.
# Метод, который позволяет устанавливать текущую скорость машины.
# Проверьте работу этих методов.

class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    cur_speed = 0

    def show_info(self):
        print('Color: {}\n'
              'Price: {}\n'
              'Max speed: {}\n'
              'Current speed: {}\n'
              .format(self.color, self.price, self.max_speed, self.cur_speed))

    def change_cur_speed(self, speed):
        self.cur_speed = speed


car = Toyota()
car.show_info()
car.change_cur_speed(180)
car.show_info()

