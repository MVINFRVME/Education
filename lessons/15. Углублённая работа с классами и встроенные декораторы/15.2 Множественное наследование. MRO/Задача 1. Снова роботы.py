# Задача 1. Снова роботы
# На военную базу привезли очередную партию роботов. И в этот раз не абы каких, а летающих: разведывательного дрона и
# военного робота.
# Разведывательный дрон просто летает в поиске противника. При команде operate он выводит сообщение «Веду разведку с
# воздуха» и передвигается немного вперёд.
# У летающего военного робота есть оружие, и при команде operate он выводит сообщение о защите военного объекта с
# воздуха с помощью этого оружия.
# Напишите программу, которая реализует все необходимые классы роботов. Сущности «Робот» и «Может летать» должны быть
# вынесены в отдельные классы. Обычный робот имеет модель и может вывести сообщение «Я — Робот». Объект, который умеет
# летать, дополнительно имеет атрибуты «Высота» и «Скорость», а также может взлетать, летать и приземляться.

# class Robot:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f'Я - Робот {self.name}'


# class CanFly:
#     def __init__(self):
#         self.height = 0
#         self.speed = 0

#     def hop_off(self):
#         self.height += 10

#     def land(self):
#         self.height -= 10

#     def fly(self):
#         self.speed += 10


# class Scout(Robot, CanFly):
#     def __init__(self, name):
#         super().__init__(name)

#     def operate(self):
#         self.fly()
#         print("Веду разведку с воздуха")


# class Combat(Robot, CanFly):
#     def __init__(self, name, model):
#         super().__init__(name)
#         self.gun = model

#     def operate(self):
#         print(f'Защищаю при помощи {self.gun}')


# my_scout = Scout('Витя')
# my_combat = Combat('Жорик', 'AWP')

# print(my_scout)
# my_scout.operate()
# print(my_combat)
# my_combat.operate()

class Robot:

    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model

    def __str__(self):
        res = super().__str__()
        return res + ' {} model {}'.format(self.__class__.__name__, self.model)

    def operate(self):
        print('Я - Робот!')


class CanFly:

    def __init__(self, *args, **kwargs):
        self.altitude = 0  # метров
        self.velocity = 0  # км/ч

    def take_off(self):
        self.altitude = 100
        self.velocity = 300

    def fly(self):
        self.altitude = 5000

    def land_on(self):
        self.altitude = 0
        self.velocity = 0

    def operate(self):
        super().operate()
        print('летим')

    def __str__(self):
        res = super().__str__()
        return res + ' {} высота {} скорость {}'.format(
            self.__class__.__name__, self.altitude, self.velocity,
        )


class ScoutDrone(CanFly, Robot):

    def __init__(self, model):
        super().__init__(model=model)

    def operate(self):
        super().operate()
        print('Робот ведет разведку с воздуха')


class WarDrone(CanFly, Robot):

    def __init__(self, model, gun):
        super().__init__(model=model)
        self.gun = gun

    def operate(self):
        super().operate()
        print(f'Робот защищает объект при помощи {self.gun}')


print()
ScoutDrone('a1').operate()
print()
WarDrone('r2-d2', 'intellect').operate()
