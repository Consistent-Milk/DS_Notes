# Importing List from typing is not necessary
# in newer versions of python as 'list' can be natively used
# for type annotation now
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for index, value in enumerate(nums):
            if (target - value) in nums_dict:
                return [nums_dict[target - value], index]
            nums_dict[value] = index
