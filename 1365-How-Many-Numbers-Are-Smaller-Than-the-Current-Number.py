from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dict = {}
        ret = []
        temp = sorted(nums)

        for idx, val in enumerate(temp):
            if val not in dict:
                dict[val] = idx

        for i in nums:
            ret.append(dict[i])

        return ret

nums = list(map(int, input("Enter numbers : ").split(",")))
solution = Solution()
result = solution.smallerNumbersThanCurrent(nums)
print(result)