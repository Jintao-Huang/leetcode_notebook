# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from math import ceil


class Solution:

    def is_ok(self, time, totalTrips, t):
        trip = 0
        for i in range(len(time)):
            trip += t // time[i]
            if trip >= totalTrips:
                return True
        return False

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        lo, hi = 1, ceil(totalTrips * min(time))
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.is_ok(time, totalTrips, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

time = [2]
totalTrips = 1
print(Solution().minimumTime(time, totalTrips))
