from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)


nums = list(map(int, input("Enter numbers: ").split(",")))
solution = Solution()
result = solution.missingNumber(nums)
print(result)