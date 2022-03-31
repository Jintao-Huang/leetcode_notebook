# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
try:
    from .build.build_list import ListNode
except ImportError:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None


def get_list_mid(head: ListNode) -> ListNode:
    # 偏左
    p, p2 = head, head
    while p2.next is not None and p2.next.next is not None:
        p = p.next
        p2 = p2.next.next
    return p


def reverse_list(start: ListNode, end: ListNode) -> ListNode:
    # [start, end). p.next = reverse_list(p.next, p2)
    p, p2 = start, end
    pe = p2
    while p != pe:
        pn = p.next
        p.next = p2
        p2 = p
        p = pn
    return p2  # start
