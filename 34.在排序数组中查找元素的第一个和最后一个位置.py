class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index = searchElement(nums, target)
        if index == -1:
            return [-1, -1]
        left = index
        while left >= 1 and nums[left-1] == target:
            left -= 1
        right = index
        while right < len(nums) -1 and nums[right+1] == target:
            right += 1
        return [left,right]


def searchElement(nums: List[int], target: int):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
