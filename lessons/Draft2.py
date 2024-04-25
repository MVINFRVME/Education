def arrayStringsAreEqual(word1, word2):
    w1 = w2 = 0
    i = j = 0

    while w1 < len(word1) and w2 < len(word2):
        if word1[w1][i] != word2[w2][j]:
            return False

        i, j = i + 1, j + 1
        if i == len(word1[w1]):
            w1 += 1
            i = 0
        if j == len(word2[w2]):
            w2 += 1
            j = 0

    if w1 != len(word1):
        return False
    return True


word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(arrayStringsAreEqual(word1, word2))

