# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/linked-list-cycle-ii/
142. 环形链表 II
- 中等
=
- 快慢双指针
"""

from typing import Optional, Union, List
import json


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def build_circle_list(list_: Union[str], pos: int) -> Optional[ListNode]:
    """pos=-1: 没有环. 142."""
    list_ = json.loads(list_)  # type: List[int]
    if not len(list_):
        return
    #
    prev = dummy = ListNode(0)  # head = dummy.next. dummy node: 哑节点
    memo = None  # type: Optional[ListNode]
    #
    for i in range(len(list_)):
        node = list_[i]
        prev.next = ListNode(node)
        prev = prev.next
        #
        if i == pos:
            memo = prev
    #
    if memo is not None:
        prev.next = memo
    return dummy.next


class Solution:
    """快慢双指针"""
    def detectCycle(self, head: ListNode) -> Optional[ListNode]:
        fast = slow = head
        while True:
            if fast is None or fast.next is None:
                return None
            #
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        # head->slow: k; cycle_start->slow: m; cycle周长=k;
        # => head->cycle_start = slow->cycle_start = k-m
        p1 = slow  # type: ListNode
        p2 = head  # type: ListNode
        del slow, fast
        #
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1


head = "[3,2,0,-4]"
pos = -1
head = build_circle_list(head, pos)
print(Solution().detectCycle(head))
#
head = "[3,2,0,-4]"
pos = 1
head = build_circle_list(head, pos)
print(Solution().detectCycle(head).val)


class Solution2:
    """双指针改用set."""
