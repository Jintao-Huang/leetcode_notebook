# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from template.build.build_list import ListNode, build_list


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        lo = head
        prev = None
        hi = head
        while hi is not None:
            if prev is not None and hi.val != prev.val:
                lo.next = hi
                lo = lo.next
            prev = hi
            hi = hi.next
        lo.next = None
        return head


l = build_list("[1,1,2]")
l = build_list("[]")
print(Solution().deleteDuplicates(l))
