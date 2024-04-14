list_number = []

numbers = int(input("Кол-во чисел в списке: "))

for num in range(numbers):
    new_num = int(input(f"Введите {num + 1} число: "))
    list_number.append(new_num)

devider = int(input("Введите делитель: "))

sum_of_index = 0
index = 0

for num in list_number:
    if num % devider == 0:
        print(f"Индекс числа {num}: {index}")
        sum_of_index += index
    index += 1

print(f"Сумма индексов: {sum_of_index}")
