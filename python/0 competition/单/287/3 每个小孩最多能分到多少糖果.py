# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List


def is_ok(candies, k, mid):
    x = 0
    for i in range(len(candies)):
        x += candies[i] // mid
        if x >= k:
            return True
    return False


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        lo, hi = 0, sum(candies) // k
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if is_ok(candies, k, mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
# candies = [5,8,6]
# k = 3
# print(Solution().maximumCandies(candies, k))
# candies = [2,5]
# k = 11
# print(Solution().maximumCandies(candies, k))

# candies =[4,7,5]
# k = 4
# print(Solution().maximumCandies(candies, k))

candies =[4,7,5]
k = 16
print(Solution().maximumCandies(candies, k))