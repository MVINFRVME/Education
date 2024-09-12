# Задача 1. Транспорт 2
# Используя код задачи про автомобили, лодки и амфибии, дополните абстрактный класс геттерами и сеттерами для
# соответствующих атрибутов. Используйте встроенные декораторы. Вот входные данные той задачи:
#
# У нас есть парк транспорта. У каждого транспорта есть цвет и скорость, и каждый умеет двигаться и подавать сигнал.
# В парке транспорта стоят:
#
# - Автомобили. Они могут ездить только по земле.
# - Лодки. Ездят только по воде.
# - Амфибии. Могут перемещаться и по земле, и по воде.

from abc import ABC, abstractmethod


class MusicMixin:
    def play_music(self):
        print("""
        I see trees of green
        Red roses too
        I see them bloom
        For me and for you
        And I think to myself
        What a wonderful world
        """)


class Transport(ABC):
    def __init__(self, color, speed):
        self._color = color
        self._speed = speed

    def __str__(self):
        return f'{type(self)} {self.color} {self.speed}'

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed


    @abstractmethod
    def drive(self):
        print('Умею ездить по земле!')

    @abstractmethod
    def swim(self):
        print('Умею плавать по воде!')

    def signal(self):
        print('Signal!')


class Car(Transport):
    def drive(self):
        super().drive()


class Boat(Transport):
    def swim(self):
        super().drive()


class Amphibia(Car, Boat, MusicMixin):
    pass


instance = Amphibia('Red', 200)
print(instance)
instance.drive()
instance.swim()
instance.play_music()
instance.color = 'Blue'
print(instance.color)
instance.speed = 125
print(instance.speed)

