# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from template.build.other import ListNode, build_circle_list
from typing import Optional


class Solution:
    def detectCycle(self, head: ListNode) -> Optional[ListNode]:
        p, p2 = head, head
        while True:
            if p2 is None or p2.next is None:
                return None
            p = p.next
            p2 = p2.next.next
            if p == p2:
                break
        p = head
        while p != p2:
            p = p.next
            p2 = p2.next
        return p


l = build_circle_list("[1]", -1)
print(Solution().detectCycle(l))
