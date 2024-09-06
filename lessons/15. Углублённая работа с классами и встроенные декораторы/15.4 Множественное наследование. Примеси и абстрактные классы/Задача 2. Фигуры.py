from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self, pos_x, pos_y, length, width):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length
        self.width = width

    @abstractmethod
    def move(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y


class ResizableMixin:
    def resize(self, width, length):
        self.length = length
        self.width = width


class Rectangle(Figure, ResizableMixin):
    pass


class Square(Figure, ResizableMixin):

    def __init__(self, pos_x, pos_y, size):
        super().__init__(pos_x, pos_y, size, size)


rect_1 = Rectangle(pos_x=10, pos_y=20, length=5, width=6)
rect_2 = Rectangle(pos_x=30, pos_y=40, length=10, width=11)
square_1 = Square(pos_x=50, pos_y=70, size=7)

for figure in [rect_1, rect_2, square_1]:
    new_size_x = figure.length * 2
    new_size_y = figure.width * 2
    figure.resize(new_size_x, new_size_y)


# Rectangle и Square полиморфны в методе move, но не в init и resize
# у Абстрактного класса мы не сможем создать instance
