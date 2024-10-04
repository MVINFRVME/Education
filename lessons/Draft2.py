from typing import Callable, List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        is_k = False
        minimal = 0
        for num in nums:
            if (num < 0) and (-num in nums) and (num < minimal):
                minimal = num
                is_k = True
        if is_k:
            return -minimal
        return -1

ex = Solution()
assert ex.findMaxK(nums = [-10,8,6,7,-2,-3]) == -1
assert ex.findMaxK(nums = [-1,10,6,7,-7,1]) == 7
assert ex.findMaxK(nums = [-1,2,-3,3]) == 3
assert ex.findMaxK(nums = [-37,37,-9,2,47,18,13,-11,9,-28]) == 37
assert ex.findMaxK(nums = [-2,-3,-1,1]) == 1