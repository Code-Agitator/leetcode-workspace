#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#


# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(height) -1
        result = 0
        while left_ptr <= right_ptr:
            current = min(height[left_ptr], height[right_ptr]) * (right_ptr - left_ptr)
            result = max(result, current)
            if height[left_ptr] > height[right_ptr]:
                right_ptr-=1
            else:
                left_ptr+=1
        return result



# @lc code=end
