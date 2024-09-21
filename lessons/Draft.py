from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []
        for value in operations:
            if value.isdigit() or value.startswith('-'):
                points.append(int(value))
            elif value == 'C':
                points.pop()
            elif value == 'D':
                points.append(int(points[-1] * 2))
            elif value == '+':
                points.append(int(points[-1] + points[-2]))

        return sum(points)


ex = Solution()
assert ex.calPoints(["5","2","C","D","+"]) == 30
assert ex.calPoints(["5","-2","4","C","D","9","+","+"]) == 27
assert ex.calPoints(["1","C"]) == 0

