# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from template.build.build_list import ListNode, build_list, list_to_str


def reverse_list(head: ListNode, end: ListNode) -> ListNode:
    p, p2 = head, end.next
    pe = p2
    while p != pe:
        pn = p.next
        p.next = p2
        p2 = p
        p = pn
    return p2  # head


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        head = ListNode(0, head)
        p = head
        for i in range(left - 1):
            p = p.next
        p2 = p.next
        for i in range(left, right):
            p2 = p2.next
        p.next = reverse_list(p.next, p2)
        return head.next


l = build_list('[1,2,3,4,5]')
print(list_to_str(Solution().reverseBetween(l, 2, 4)))
