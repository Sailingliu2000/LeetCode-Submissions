from typing import List

class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return True
        else:
            return False

nums = list(map(int, input("Enter numbers: ").split(",")))

solution = Solution()
result = solution.contains_duplicate(nums)
print(result)