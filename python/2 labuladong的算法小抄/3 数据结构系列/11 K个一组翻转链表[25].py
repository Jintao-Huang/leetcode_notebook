# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import Optional
from template.build.build_list import ListNode, build_list, list_to_str
from template.utils.linked_list import reverse_list



class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        head = ListNode(0, head)  # 避免修改head
        p = head
        p2 = p
        i = 0
        while p2 is not None:
            if i >= k:
                p3 = p.next
                p.next = reverse_list(p3, p2.next)
                p = p3
                p2 = p
                i = 0
            p2 = p2.next
            i += 1
        return head.next


l1 = build_list("[1,2,3,4,5]")
print(list_to_str(Solution().reverseKGroup(l1, 1)))
