def func(text):
    s_list = s.split(' ')
    space = ''
    while space in s_list:
        s_list.remove(space)
    last_word = s_list[-1]
    last_word_count = len(last_word)
    return last_word_count


s = '   fly me   to   the moon  '
print(func(s))