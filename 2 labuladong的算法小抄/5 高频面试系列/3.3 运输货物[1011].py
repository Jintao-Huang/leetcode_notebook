# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    def is_ok(self, weights, days, mid):
        n = mid
        d = 1
        for i in range(len(weights)):
            w = weights[i]
            if w > n:
                n = mid
                d += 1
            n -= w
            if d > days:
                return False
        return True

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.is_ok(weights, days, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
print(Solution().shipWithinDays(weights, days))
