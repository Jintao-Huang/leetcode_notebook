# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from math import gcd
from template.data_structure.linked_list import ListNode, LinkedList


class Solution:
    """链表"""

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ll = LinkedList(nums)
        p = ll.head  # type: ListNode
        p = p.next
        while not ll.is_tail(p.next):
            x = p.val
            x2 = p.next.val
            g = gcd(x, x2)
            if g > 1:
                lcm = x * x2 // g
                ll.delete(p.next)
                p.val = lcm
                if p != ll.head.next:
                    p = p.prev
            else:
                p = p.next
        #
        p = ll.head.next
        ans = []
        while not ll.is_tail(p):
            ans.append(p.val)
            p = p.next

        return ans


class Solution2:
    """栈"""

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = []  # stack
        for x in nums:
            while len(ans) > 0:
                g = gcd(ans[-1], x)
                if g > 1:
                    x = ans[-1] * x // g
                    ans.pop()
                else:
                    break
            ans.append(x)
        return ans


nums = [6, 4, 3, 2, 7, 6, 2]
print(Solution().replaceNonCoprimes(nums))
print(Solution2().replaceNonCoprimes(nums))
