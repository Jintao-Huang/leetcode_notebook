# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from template.build.build_list import build_list, ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        head = ListNode(0, head)
        p, p2 = head, head
        # 找倒数n+1个
        for _ in range(n + 1):
            p2 = p2.next
        while p2 is not None:
            p = p.next
            p2 = p2.next
        # 删除p.next
        p.next = p.next.next

        return head.next
