# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from math import sqrt


class Solution:
    """二分法. lower_bound2框架. Ot(LogN) Os(1). 其中N=int(sqrt(2 ** 31 - 1))"""
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, int(sqrt(2 ** 31 - 1))
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if (mid + 1) ** 2 > x:
                hi = mid
            else:
                lo = mid + 1
        return lo


x = 8
print(Solution().mySqrt(x))

x = 4
print(Solution().mySqrt(x))