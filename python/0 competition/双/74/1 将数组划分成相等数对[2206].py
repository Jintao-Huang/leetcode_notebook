# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from collections import defaultdict


class Solution:
    """哈希表"""

    def divideArray(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for i in range(len(nums)):
            x = nums[i]
            d[x] += 1

        for v in d.values():
            if v % 2 == 1:
                return False
        return True
