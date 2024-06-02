# Задача 3. Отцы, матери и дети
# Что нужно сделать:
# Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:

# Имя,
# возраст,
# список детей.
# И он может:

# Сообщить информацию о себе,
# успокоить ребёнка,
# покормить ребёнка.
# У ребёнка есть:

# Имя,
# возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
# состояние спокойствия,
# состояние голода.
# Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг», и словарь состояний, и что-то поинтереснее

import random


class Parent:

    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = children

    def show_info(self):
        print(f'Имя: {self.name}\n'
              f'Возраст: {self.age}\n'
              f'Список детей: {self.children}\n')

    def calm_down(self):
        for child in self.children:
            if child.mind_state < 2:
                child.mind_state += 1
                print(f'Успокаиваем... {child.name} теперь {child.mind_states[child.mind_state]}')
            else:
                print(f'{child.name} уже {child.mind_states[child.mind_state]}')

    def feed(self):
        for child in self.children:
            if child.hunger_state < 3:
                child.hunger_state += 1
                print(f'Кормим...{child.name} теперь {child.hunger_states[child.hunger_state]}')
            else:
                print(f'{child.name} {child.hunger_states[child.hunger_state]}')


class Child:
    hunger_states = {0: 'очень голодный', 1: 'голодный', 2: 'слегка Голоден', 3: 'сытый'}
    mind_states = {0: 'плачет', 1: 'обеспокоен', 2: 'спокоен'}

    def __init__(self, name, age, hunger_state=0, mind_state=0):
        self.name = name
        self.age = age
        self.hunger_state = hunger_state
        self.mind_state = mind_state


parent_name = input('Введите имя родителя: ')
parent_age = int(input('Введите возраст родителя: '))
all_children = []
children_num = int(input('Введите кол-во детей: '))

for _ in range(children_num):
    child_name = input('Введите имя ребенка: ')
    while True:
        child_age = int(input('Введите возраст ребенка: '))
        if parent_age - child_age < 16:
            print('Разница между ребенком и родителем не должна быть меньше 16 лет!')
        else:
            break
    adding_child = Child(child_name, child_age, random.randint(0, 3), random.randint(0, 2))
    all_children.append(adding_child)

cur_parent = Parent(parent_name, parent_age, all_children)

print()
for i_child in all_children:
    print(f'{i_child.name} {i_child.mind_states[i_child.mind_state]} и {i_child.hunger_states[i_child.hunger_state]}')

while True:
    action = int(input('\nУспокоить детей, введите "1"\n'
                       'Покормить детей, введите "2"\n'
                       'Показать информацию о родителе, введите "3"\n'
                       'Выйти из программы, введите "4"\n'))
    if action == 1:
        cur_parent.calm_down()
    elif action == 2:
        cur_parent.feed()
    elif action == 3:
        cur_parent.show_info()
    elif action == 4:
        break
    else:
        print('Ошибка Ввода!\n')
