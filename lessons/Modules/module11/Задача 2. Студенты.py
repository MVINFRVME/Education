# Задача 2. Студенты
# Что нужно сделать
# Реализуйте модель с именем Student, содержащую поля «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
# Затем создайте список из десяти студентов (данные о студентах можете придумать или запросить у пользователя) и
# отсортируйте список по возрастанию среднего балла. Выведите результат на экран.

class Student:

    def __init__(self, name, group_num, grades: list):
        self.name = name
        self.group_num = group_num
        self.grades = grades


data = [
    ['Ivanov Ivan', 1, [5, 4, 4, 3, 4]],
    ['Petrov Petr', 1, [3, 4, 3, 3, 4]],
    ['Sidorov Sidor', 2, [4, 4, 5, 4, 4]],
    ['Kozlov Kozel', 2, [5, 5, 5, 5, 5]],
    ['Ivanova Irina', 1, [1, 1, 1, 1, 1]],
    ['Petrova Polina', 3, [5, 5, 4, 5, 5]],
    ['Sidorova Svetlana', 3, [3, 4, 4, 4, 4]],
    ['Kozlova Kristina', 2, [5, 5, 5, 5, 5]],
    ['Ivan Ivanov', 4, [4, 4, 3, 4, 4]],
    ['Petr Petrov', 4, [5, 5, 5, 5, 5]]
]

students = [Student(student_info[0], student_info[1], student_info[2]) for student_info in data]
print(students)

for objct in students:
    print(objct.name, objct.group_num, objct.grades)