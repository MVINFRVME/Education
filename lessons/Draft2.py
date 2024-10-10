from typing import Callable, List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0:
            return 0
        g.sort(), s.sort()
        result = 0
        for j in range(len(s)):
            if s[j] >= g[0]:
                start_index = j
                break
        else:
            return 0

        for i in range(start_index, len(g)):




ex = Solution()
assert ex.findContentChildren(g = [5,4,3,3,2], s = []) == 0
assert ex.findContentChildren(g = [5,4,3,3,2], s = [2,1]) == 1
assert ex.findContentChildren(g = [1,2,3], s = [1,1]) == 1
assert ex.findContentChildren(g = [1,2], s = [1,2,3]) == 2
assert ex.findContentChildren(g = [2,4,3,3,2], s = [2,1,6,8]) == 3
