# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.s = [0]
        for i in range(len(nums)):
            self.s.append(self.s[-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left]