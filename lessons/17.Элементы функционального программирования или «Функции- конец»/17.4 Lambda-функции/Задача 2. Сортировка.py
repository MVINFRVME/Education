# Задача 2. Сортировка
# Таблица базы данных состоит из строк, в которых хранится информация о каждом человеке: его имя, возраст и
# остальные данные. Вас попросили реализовать для этой базы сортировку по возрасту (по убыванию и по возрастанию).
# Реализуйте класс Person с соответствующей инициализацией, а также сеттерами и геттерами. Затем создайте список
# из хотя бы трёх людей и отсортируйте их. Для сортировки используйте лямбда-функцию.

class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    def __repr__(self):
        return f'{self.__name} {self.__age} {self.__gender}'

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def gender(self):
        return self.__gender

    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age

    @gender.setter
    def gender(self, gender):
        self.__gender = gender


people = [Person('Витя', 30, 'male'),
          Person('Тася', 25, 'female'),
          Person('Гога', 34, 'male')
          ]

print(people)
sorted_people = sorted(people, key=lambda x: x.age)
print(sorted_people)