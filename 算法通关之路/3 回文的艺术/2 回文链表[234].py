# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from template.build.build_list import build_list, ListNode
from template.utils import get_list_mid, reverse_list


class Solution:
    """快慢指针, 链表反转. Ot(N) Os(1)"""

    def isPalindrome(self, head: ListNode) -> bool:
        mid = get_list_mid(head)
        #
        h = reverse_list(mid.next)
        mid.next = h
        #
        p1, p2 = head, h
        while p2 is not None:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True


l = build_list("[1,2,1]")
print(Solution().isPalindrome(l))
