class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        current_index = 0
        while left <= right:
            mid = int((left + right) / 2)
            current_index = mid
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            else:
                return mid
        return current_index if  nums[current_index] > target else current_index+1
