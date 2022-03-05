# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from template.build.build_list import build_list, ListNode


def reverse_list(head: ListNode) -> ListNode:
    p, p2 = head, None
    while p is not None:
        p_n = p.next
        p.next = p2
        p2 = p
        p = p_n
    return p2  # head


class Solution:
    """快慢指针, 链表反转. Ot(N) Os(1)"""

    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head
        prev = None
        while fast is not None:
            prev = slow
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
        #
        h = reverse_list(slow)
        prev.next = h
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
