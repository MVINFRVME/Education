words_list = []
count = [0, 0, 0]

for i in range(3):
    word = input(f'Введите {i + 1} слово: ')
    words_list.append(word)

text = input('\nВведите текст: ')
while text != 'end':
    for i in range(3):
        if text == words_list[i]:
            count[i] += 1
    text = input('Введите текст: ')

print('\nПодсчет слов в тексте: ')
for i in range(3):
    print(f'{words_list[i]}: {count[i]}')


