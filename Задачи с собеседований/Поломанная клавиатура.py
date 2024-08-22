# Вчера задачу на собесе дали:
# "У Васи сломалась клавиатура. Когда он нажимает B, то она не печатается, но при этом удаляется самая правая большая
# буква, если нажимает b, то удаляется самая правая маленькая буква, остальные клавиши работают как обычно. Если нет
# буквы подходящей под удаление, то нажатие игнорируется." Нужно написать функцию, которая принимает оригинальный текст,
# а возвращает "поломаный"
# Пример: func('YetAnotherBrokenKeyboard') —> 'YetnotherrokenKeoard'


def func(text: str) -> str:
    broken_text = ''
    for i in range(len(text)):
        if text[i] == 'B':
            upper = False
            for j in range(len(broken_text)):
                if broken_text[j].isupper():
                    last_upper_index = j
                    upper = True
            if upper:
                if last_upper_index == len(broken_text) - 1:
                    broken_text = broken_text[:last_upper_index]
                else:
                    broken_text = broken_text[:last_upper_index] + broken_text[last_upper_index + 1:]
        elif text[i] == 'b':
            lower = False
            for k in range(len(broken_text)):
                if broken_text[k].islower():
                    last_lower_index = k
                    lower = True
            if lower:
                if last_lower_index == len(broken_text) - 1:
                    broken_text = broken_text[:last_lower_index]
                else:
                    broken_text = broken_text[:last_lower_index] + broken_text[last_lower_index + 1:]
        else:
            broken_text += text[i]

    return broken_text


print(func('YetAnotherBrokenKeyboard'))

# YetAnotbherBrokenKeyboBard
# YetAnotherBrokenKeyoBard
assert func('YetAnotbherBrokenKeyboBard') == 'Yetnoherrokeneoard'
