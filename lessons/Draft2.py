
class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        result = 0
        for sym in s:
            if count > result:
                result = count
            if sym == '(':
                count += 1
            elif sym == ')':
                count -= 1

        return result


ex = Solution()
assert ex.maxDepth("(1+(2*3)+((8)/4))+1") == 3
assert ex.maxDepth("(1)+((2))+(((3)))") == 3
assert ex.maxDepth("()(())((()()))") == 3
