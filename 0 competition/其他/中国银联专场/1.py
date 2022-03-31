# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import Optional
from template.build.build_list import ListNode, build_list, list_to_str
from template.utils.linked_list import get_list_mid, reverse_list

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        head = ListNode(0, head)
        mid = get_list_mid(head)
        mn = mid.next
        mid.next = ListNode(mid.next.val, None)
        p2_c = reverse_list(mn, None)
        p_c = head.next
        print(p_c, p2_c)
        #
        p, p2 = p_c, p2_c
        error = False
        ans = True
        while p is not None and p2 is not None:
            if p.val == p2.val:
                p = p.next
                p2= p2.next
            else:
                if error:
                    ans = False
                    break
                else:
                    error = True
                    p = p.next
        if ans:
            return True

        p, p2 = p_c, p2_c
        error = False
        ans = True
        while p is not None and p2 is not None:
            if p.val == p2.val:
                p = p.next
                p2 = p2.next
            else:
                if error:
                    ans = False
                    break
                else:
                    error = True
                    p2 = p2.next
        return ans

head = build_list('[1,2,3,2,1]')
print(Solution().isPalindrome(head))
