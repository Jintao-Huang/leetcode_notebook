# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # type: int
        self.next = next  # type: ListNode


def traverse_list(head: ListNode):
    # [前序遍历]
    traverse_list(head.next)
    # [后序遍历]
