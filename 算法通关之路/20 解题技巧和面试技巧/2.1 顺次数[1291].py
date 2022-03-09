# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from bisect import bisect_right, bisect_left


class Solution:
    """二分法. 构造法. Ot(1) Os(1)"""

    def __init__(self):
        s = "123456789"
        self.ans = []
        for k in range(2, 10):
            for i in range(10 - k):
                j = i + k
                self.ans.append(int(s[i:j]))

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        lo = bisect_left(self.ans, low)
        hi = bisect_right(self.ans, high)

        return self.ans[lo:hi]


low = 10
high = 1000000000
print(Solution().sequentialDigits(low, high))
