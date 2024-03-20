worker_check = False

ID_list = []

number_of_workers = int(input('Кол-во сотрудников в офисе: '))

for _ in range(number_of_workers):
    ID_num = int(input('ID сотрудника: '))
    ID_list.append(ID_num)

searching_ID = int(input('Какой ID ищем? '))

for ID in ID_list:
    if ID == searching_ID:
        worker_check = True

if worker_check:
    print('Сотрудник на месте')
else:
    print('Сотрудник не работает!')