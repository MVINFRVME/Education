s = "lotut"
vowels = set('aeiou')
res = list(s)
i, j = 0, len(s) - 1

while i < j:
    if res[i] not in vowels:
        i += 1
    elif res[j] not in vowels:
        j -= 1
    else:
        res[i], res[j] = res[j], res[i]
        i += 1
        j -= 1

res_str = ''.join(res)

print(res_str)
