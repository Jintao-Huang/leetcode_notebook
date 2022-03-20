# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from template.build.build_list import ListNode, build_list
from typing import Optional, List


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        # get tail, len
        i = 1
        p = head
        while p.next is not None:
            p = p.next
            i += 1
        p.next = head
        # get node k
        k = i - k % i - 1
        p = head
        for _ in range(k):
            p = p.next
        # 断开
        ans = p.next
        p.next = None
        return ans

head = build_list("[1,2,3,4,5]")
k = 2
print(Solution().rotateRight(head, k))