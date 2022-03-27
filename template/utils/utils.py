# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Dict, Tuple, Union


def unique(nums: List[int]) -> None:
    """条件: nums有序"""
    lo = 1  # 写入指针
    for hi in range(1, len(nums)):
        if nums[hi] != nums[hi - 1]:
            nums[lo] = nums[hi]
            lo += 1
    for i in range(lo, len(nums)):
        nums.pop()


if __name__ == '__main__':
    l = [1, 1, 2, 2, 3]
    unique(l)
    print(l)

#
try:
    from .build.build_list import ListNode
except ImportError:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None


def get_list_mid(head: ListNode) -> ListNode:
    p, p2 = head, head
    while p2.next is not None and p2.next.next is not None:
        p = p.next
        p2 = p2.next.next
    return p


def reverse_list(head: ListNode) -> ListNode:
    p, p2 = head, None
    while p is not None:
        p_n = p.next
        p.next = p2
        p2 = p
        p = p_n
    return p2  # head


#
def counter(nums: List[int], need_sorted: bool = False) -> Union[Dict, List[List[int]]]:
    """返回 按字典序."""
    d = {}
    for x in nums:
        if x not in d:
            d[x] = 0
        d[x] += 1
    #
    if need_sorted:
        keys = sorted(d.keys())
        return [[k, d[k]] for k in keys]
    else:
        return d
