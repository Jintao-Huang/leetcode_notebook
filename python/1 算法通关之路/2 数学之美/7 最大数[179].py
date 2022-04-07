# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from typing import List
from functools import cmp_to_key


class Solution:
    """排序. Ot(NLogN) Os(N)"""
    def __init__(self):
        self.key = cmp_to_key(
            lambda x, y: int(y + x) - int(x + y))

    @staticmethod
    def _remove_zeros(s: str) -> str:

        for i in range(len(s)):
            if s[i] != '0':
                break
        return s[i:]

    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]
        nums.sort(key=self.key)
        return self._remove_zeros("".join(nums))


nums = [3, 30, 34, 5, 9]
# nums = [0, 0]
print(Solution().largestNumber(nums))
