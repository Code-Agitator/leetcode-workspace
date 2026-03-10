#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if not l1:
            return l2
        if not l2:
            return l1

        result_head = ListNode(0)
        result_current = result_head
        delta = 0
        l1_current = l1
        l2_current = l2
        while l1_current is not None or l2_current is not None or delta == 1:
            current_value = self.zero_if_none(l1_current) + self.zero_if_none(
                l2_current
            )
            current_value = current_value + delta
            delta = 0 
            if current_value >= 10:
                delta = 1
                current_value = current_value % 10
                   
            result_current.next = ListNode(current_value)
            result_current = result_current.next
            if l1_current is not None:
                l1_current = l1_current.next
            if l2_current is not None:
                l2_current = l2_current.next
        return result_head.next

    def zero_if_none(self, l):
        return 0 if l is None else l.val


# @lc code=end
