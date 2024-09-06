# Задача 1. Транспорт
# У нас есть парк транспорта. У каждого транспорта есть цвет и скорость, и каждый умеет двигаться и подавать сигнал.
# В парке транспорта стоят:
#
# Автомобили. Они могут ездить только по земле.
# Лодки. Ездят только по воде.
# Амфибии. Могут перемещаться и по земле, и по воде.
# Напишите код, который реализует соответствующие классы и методы. Класс «Транспорт» должен быть абстрактным и
# содержать абстрактные методы.
#
# Также добавьте класс-примесь, в котором реализован функционал проигрывания музыки. «Замешайте» этот класс в «Амфибию»
#

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
        self.color = color
        self.speed = speed

    def __str__(self):
        return f'{type(self)} {self.color} {self.speed}'

    @abstractmethod
    def drive(self):
        print('Умею ездить по земле!')

    @abstractmethod
    def swim(self):
        print('Умею плавать по воде!')


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
