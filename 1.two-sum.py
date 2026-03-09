#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp= dict()
        for i in range(len(nums)):
            if target - nums[i] in temp.keys():
                return [i,temp[target-nums[i]]]
            else:
                temp[nums[i]]= i
# @lc code=end
