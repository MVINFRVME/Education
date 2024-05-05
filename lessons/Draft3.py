def maximumNumberOfStringPairs(words):
    word_dict = dict()
    count = 0
    for word in words:
        rev = word[::-1]
        if rev in word_dict:
            word_dict.pop(rev)
            count += 1
        else:
            word_dict[word] = 1

    return count


words = ["cd","ac","dc","ca","zz"]
print(maximumNumberOfStringPairs(words))
