class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name[-1] != typed[-1]:
            return False
        l = 0
        r = 0
        while l < len(name):
            while name[l] == typed[r]:
                r += 1
            l += 1

        l = 0
        for i in range(len(typed)):
            if typed[i] == name[0]:
                continue

            else:
                if (typed[l] != typed[r]) or (len(typed) == 1):
                    return False
                r += 1

        while r < len(typed) - 1:
            if name[l - 1] == typed[r]:
                r += 1
            else:
                return False

        return True


ex = Solution()
assert ex.isLongPressedName("vtkgn","vttkgnn") == True
assert ex.isLongPressedName("alex" ,"aaleexa") == False
assert ex.isLongPressedName("alex","aaleex") == True
assert ex.isLongPressedName("a","b") == False
assert ex.isLongPressedName("saeed", "ssaaedd") == False
assert ex.isLongPressedName("alex", "aaleexeex") == False
assert ex.isLongPressedName("abcd", "aaabbbcccddd") == True

