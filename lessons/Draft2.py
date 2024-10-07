from typing import Callable, List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i, j = nums[0], nums[1]
        if i < j:
            i, j = nums[1], nums[0]

        for num in nums[2:]:
            if num > i and num > j:
                j = i
                i = num
            elif num > i:
                i = num
            elif num > j:
                j = num
        return (i - 1) * (j - 1)


ex = Solution()
assert ex.maxProduct(nums = [3,4,5,2]) == 12
assert ex.maxProduct(nums = [4,3,5,2]) == 12
assert ex.maxProduct(nums = [1,5,4,5]) == 16
assert ex.maxProduct(nums = [3,7]) == 12
assert ex.maxProduct(nums = [2,4,1,2,3,1,2,5,6,2,4,5,5,5,6,6,6,7,6,5,3,2,7]) == 36
assert ex.maxProduct(nums = [2,4,1,2,3,1,2,5,6,2,4,5,5,5,6,6,6,7,6,5,3,2]) == 30
assert ex.maxProduct(nums = [2,4,1,2,3,1,2,5,6,2,4,5,5,5,6,6,6,6,5,3,2]) == 25