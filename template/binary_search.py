# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
或使用`bisect`库
"""
from bisect import bisect_right, bisect_left
from typing import List


def binary_search(nums: List[int], target: int) -> bool:
    """Ot(LogN) Os(1)"""
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2  # 偶数时: 中点偏左
        if target == nums[mid]:
            return True
        elif target > nums[mid]:
            lo = mid + 1
        else:
            hi = mid - 1
    return False


# [lower_bound, upper_bound)
def lower_bound(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if target > nums[mid]:
            lo = mid + 1
        else:  # 相等与小于时等价的
            hi = mid - 1
    return lo


def upper_bound(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if target >= nums[mid]:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo


nums = [1, 2, 2, 2, 3]
print(binary_search(nums, 2))
print(lower_bound(nums, 2))  # 1
print(upper_bound(nums, 2))  # 4
#
print(lower_bound(nums, 0))  # 0
print(lower_bound(nums, 4))  # 5
print(upper_bound(nums, 0))  # 0
print(upper_bound(nums, 4))  # 5
# 同上
print(bisect_left(nums, 2))
print(bisect_right(nums, 2))
#
print(bisect_left(nums, 0))
print(bisect_left(nums, 4))
print(bisect_right(nums, 0))
print(bisect_right(nums, 4))
