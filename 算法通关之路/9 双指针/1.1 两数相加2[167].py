# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """双指针-头尾. Ot(N) Ot(1)"""

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            x = numbers[lo] + numbers[hi]
            if x == target:
                return [lo + 1, hi + 1]
            elif x < target:
                lo += 1
            else:
                hi -= 1


class Solution2:
    """哈希表. Ot(N) Os(N)"""

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, x in enumerate(numbers):
            if x in d:
                return [d[x] + 1, i + 1]
            d[target - x] = i
