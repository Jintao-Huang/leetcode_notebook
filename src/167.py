# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
167. 两数之和 II - 输入有序数组
- 简单
- 推荐
=
- 左右双指针
"""

from typing import List


class Solution:
    """左右双指针"""

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1  # [lo, hi]
        while lo != hi:
            sum_ = numbers[lo] + numbers[hi]
            if sum_ == target:
                return [lo + 1, hi + 1]
            elif sum_ < target:
                lo += 1
            else:
                hi -= 1


class Solution2:
    """使用dict(哈希表). 同1."""

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, x in enumerate(numbers):
            if x in d:
                return [d[x] + 1, i + 1]
            d[target - x] = i
