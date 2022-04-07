# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
import math
from typing import List

"""
递归的空间复杂度: 递归最大的深度 * 递归函数的Os + 递归函数调用的其他函数的Os

常见递归时间复杂度
Tn                     复杂度          递归深度                e.g.
T(n/2) + O(1)           Ot(LogN)        LogN                二分查找
T(n-1) + O(1)           Ot(N)           N                   求和
2T(n/2) + O(1)          Ot(N)           LogN                求max
2T(n/2) + O(N)          Ot(NLogN)       LogN                归并、理想快排
T(N-1) + O(N)           Ot(N^2)         N                   不理想的快排
T(N-1) + T(N-2) + O(1)  Ot(2^N)         N                   菲波那切数列
"""


class Solution509:
    """斐波那契数"""

    def fib(self, n: int) -> int:
        """动态规划. Ot(N) Os(1)"""
        x, y = 0, 1
        for _ in range(n):
            x, y = y, x + y
        return x

    def fib2(self, n: int) -> int:
        """递归. Ot(2^N) Os(1)"""

        def _fib(_n):
            if _n == 0:
                return 0
            if _n == 1:
                return 1
            return _fib(_n - 1) + _fib(_n - 2)

        return _fib(n)

    def fib3(self, n: int) -> int:
        """通项公式"""
        sqrt5 = math.sqrt(5)
        fibN = (((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n) / sqrt5
        return round(fibN)


print(Solution509().fib(30))
print(Solution509().fib2(30))
print(Solution509().fib3(30))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
1. 判断条件为索引越界/属性访问服务
"""


class Solution206:
    """反转链表. 其他见(链表)"""

    def reverseList4(self, head: ListNode) -> ListNode:
        """递归. Ot(N) Os(N)"""

        def _reverseList(_head: ListNode) -> ListNode:
            if _head is None or _head.next is None:
                return _head
            n = _head.next
            p = _head
            _head = _reverseList(p.next)
            n.next = p
            p.next = None
            return _head

        return _reverseList(head)


"""
1. 递归注意终止条件（4要素）

"""


class Solution344:
    """反转字符串"""

    def reverseString(self, s: List[str]) -> None:
        """对撞双指针. Ot(N) Os(1)"""
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    def reverseString2(self, s: List[str]) -> None:
        """递归. Ot(N) Os(N)"""

        def _reverseString(_s: List[str], lo: int, hi: int) -> None:
            """hi代表索引"""
            if lo >= hi:
                return
            _reverseString(_s, lo + 1, hi - 1)
            _s[lo], _s[hi] = _s[hi], _s[lo]

        _reverseString(s, 0, len(s) - 1)


s = ["h", "e", "l", "l", "o"]
# Solution344().reverseString(s)
Solution344().reverseString2(s)
print(s)
