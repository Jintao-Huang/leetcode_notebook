# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from math import gcd


class ListNode:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next

def create_list(nums):
    head = ListNode(0, None, None)
    prev = head
    for i in range(len(nums)):
        x = nums[i]
        p = ListNode(x, prev, None)
        prev.next = p
        prev = p
    return head


x = create_list([1, 2, 3])
print()


def remove_node(p: ListNode) -> ListNode:
    """返回前一个"""
    prev = p.prev
    next = p.next
    prev.next = next
    if next is not None:
        next.prev = prev
    return prev


x = create_list([1, 2, 3])
x2 = x.next.next
print(remove_node(x2).val)

class Solution:
    """链表"""
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        head = create_list(nums)  # type: ListNode
        p = head.next  # type: ListNode
        while p.next is not None:
            x = p.val
            x2 = p.next.val
            gcd_ = gcd(x, x2)
            if gcd_ > 1:
                lcm = x * x2 // gcd_
                remove_node(p.next)
                p.val = lcm
                if p != head.next:
                    p = p.prev
            else:
                p = p.next
        p = head.next
        ans = []
        while p is not None:
            ans.append(p.val)
            p = p.next

        return ans




nums = [6, 4, 3, 2, 7, 6, 2]
print(Solution().replaceNonCoprimes(nums))
