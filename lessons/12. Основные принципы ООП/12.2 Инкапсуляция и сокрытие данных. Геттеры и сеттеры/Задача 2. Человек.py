# Задача 2. Человек
# Реализуйте класс «Человек», который инициализируется именем (имя должно состоять только из букв) и возрастом (должен
# быть в диапазоне от 0 до 100), а внутри класса считается общее количество инициализированных объектов. Реализуйте
# сокрытие данных для всех атрибутов (как статических, так и динамических), а для изменения и получения данных объекта
# напишите специальные геттеры и сеттеры.

# При тестировании класса измените приватный атрибут (например, возраст) двумя способами: сеттером и
# «крайне нерекомендуемым», который был показан в уроке.

class Human:
    __count = 0

    def __init__(self, name, age):
        self.__name = ''
        self.__age = 0
        self.set_name(name)
        self.set_age(age)
        Human.__count += 1

    def set_name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            raise Exception('Имя должно содержать только буквы!')

    def set_age(self, age):
        if 0 <= age <= 100:
            self.__age = age
        else:
            raise Exception('Возраст может быть только в диапазоне от 0 до 100!')

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


human_1 = Human('Толя', 20)
print(human_1.get_name(), human_1.get_age())
human_1._Human__name = 'Шрек'
print(human_1.get_name())
