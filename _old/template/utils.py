# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Dict, Tuple


def unique(nums: List[int]) -> None:
    """条件: nums有序"""
    j = 1  # 写入指针
    for i in range(1, len(nums)):
        if nums[i] != nums[j - 1]:
            nums[j] = nums[i]
            j += 1
    for i in range(j, len(nums)):
        nums.pop()


l = [1, 1, 2, 2, 3]
unique(l)
print(l)


#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    p, p2 = head, None
    while p is not None:
        p_n = p.next
        p.next = p2
        p2 = p
        p = p_n
    return p2  # head
