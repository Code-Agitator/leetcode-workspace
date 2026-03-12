#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max = 0
        for num in nums_set:
            i = 1
            if (num - 1) in nums_set:
                continue
            while num + 1 in nums_set:
                i += 1
                num += 1
            if i > max:
                max = i
        return max


# @lc code=end
