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
            if mid >= int(sqrt(x)):
                hi = mid
            else:
                lo = mid + 1
        return lo


class Solution2:
    """二分法. upper_bound2框架"""

    def mySqrt(self, x: int) -> int:
        lo, hi = 0, int(sqrt(2 ** 31 - 1))
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if mid ** 2 <= x:
                lo = mid
            else:
                hi = mid - 1
        return lo


class Solution3:
    """二分法. binary_search框架"""

    def mySqrt(self, x: int) -> int:
        lo, hi = 0, int(sqrt(2 ** 31 - 1))
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if mid ** 2 > x:
                hi = mid - 1
            elif (mid + 1) ** 2 <= x:
                lo = mid + 1
            else:  # mid ** 2 <= x < (mid + 1) ** 2
                return mid
        return -1  # 结果必存在, 运行不到这


x = 8
print(Solution().mySqrt(x))
print(Solution2().mySqrt(x))
print(Solution3().mySqrt(x))
