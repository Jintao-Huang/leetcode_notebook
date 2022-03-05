# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """二分法. 求最小k. lower_bound2框架.
    Ot(NLog(M)) Os(1). N=len(piles), M=max(piles)"""

    def test(self, piles: List[int], h: int, k: int) -> bool:
        for i in range(len(piles)):
            h -= (piles[i] - 1) // k + 1
            if h < 0:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.test(piles, h, mid):  # 满足取左
                hi = mid
            else:
                lo = mid + 1
        return lo


piles = [3, 6, 7, 11]
H = 8
print(Solution().minEatingSpeed(piles, H))
