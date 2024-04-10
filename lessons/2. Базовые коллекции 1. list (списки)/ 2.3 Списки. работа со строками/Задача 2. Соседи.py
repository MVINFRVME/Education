text = list(input('Введите строку: '))
check_index = int(input('Номер символа: ')) - 1

left_symbol = text[check_index - 1]
right_symbol = text[check_index + 1]

print(f'Символ слева: {left_symbol}')
print(f'Символ справа: {right_symbol}')

count = 0
if left_symbol == text[check_index]:
    count += 1
if right_symbol == text[check_index]:
    count += 1

if count == 2:
    print('Есть два таких символа.')
elif count == 1:
    print('Есть ровно один такой же символ.')
else:
    print('Таких же символов нет.')