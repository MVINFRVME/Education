def romanToInt(s):
    arabian_dig = 0
    for sym in s:
        if sym == 'M':
            arabian_dig += 1000
        elif sym == 'D':
            arabian_dig += 500
        elif sym == 'C':
            arabian_dig += 100
        elif sym == 'L':
            arabian_dig += 50
        elif sym == 'X':
            arabian_dig += 10
        elif sym == 'V':
            arabian_dig += 5
        elif sym == 'I':
            arabian_dig += 1
        return arabian_dig


s = 'XVIII'
print(romanToInt(s))
