# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
1. 使用for循环一定要必须执行一次，不然最好用while
  while True!!!
2. 3数比较至少比较2次
"""
from typing import Tuple, List


class Solution5:
    """最长回文子串.

    方法2: 动态规划略"""

    def longestPalindrome(self, s: str) -> str:
        """中心扩展算法. Ot(N^2) Os(1)"""

        def expand_from_center(lo: int, hi: int) -> Tuple[int, int]:
            """Ot(N)"""
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            return lo + 1, hi - 1  # 回溯

        res = [0, 0]  # 或用start, end
        for i in range(len(s)):
            # [lo, hi]
            lo, hi = expand_from_center(i - 1, i + 1)
            lo2, hi2 = expand_from_center(i, i + 1)
            # 3数比较至少比较2次
            if hi2 - lo2 > hi - lo:
                lo, hi = lo2, hi2
            if hi - lo > res[1] - res[0]:
                res = [lo, hi]
        return s[res[0]: res[1] + 1]


print(Solution5().longestPalindrome("babad"))


class Solution10:
    pass


class Solution11:
    pass


class Solution15:
    pass


class Solution17:
    pass


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution19:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """双指针. Ot(N) Os(1)"""
        head = ListNode(0, head)  # 头节点
        prev_i = head  # type: ListNode
        j = head.next  # type: ListNode
        while n > 0:
            n -= 1
            j = j.next
        while j is not None:
            prev_i = prev_i.next
            j = j.next
        prev_i.next = prev_i.next.next
        return head.next


def print_list(head):
    """head不含头结点"""
    items = []
    p = head
    while p is not None:
        items.append(str(p.val))
        p = p.next
    print("LinkedList([%s])" % ', '.join(items))


head = ListNode(1, ListNode(2))
print_list(head)
head = Solution19().removeNthFromEnd(head, 2)
print_list(head)
