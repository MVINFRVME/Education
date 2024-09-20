from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        count = 0
        highest = 0
        for value in gain:
            count += value
            if count > highest:
                highest = count
        return highest

ex = Solution()
assert ex.largestAltitude() == 1
assert ex.largestAltitude() == 0
assert ex.largestAltitude() == 781
