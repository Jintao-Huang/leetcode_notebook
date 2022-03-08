# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
或使用`bisect`库
"""
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """Ot(LogN) Os(1). binary_search框架"""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2  # 偶数时: 中点偏左
        if target == nums[mid]:
            return mid
        elif nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo if nums[lo] == target else -1


def lower_bound(nums: List[int], target: int) -> int:
    """lower_bound2框架."""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo


def upper_bound(nums: List[int], target: int) -> int:
    """upper_bound2框架."""
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] > target:
            hi = mid
        else:
            lo = mid + 1
    return lo


nums = [1, 2, 2, 2, 3]
print(binary_search(nums, 2))  # 2
print(lower_bound(nums, 2))  # 1
print(upper_bound(nums, 2))  # 4
#
print(lower_bound(nums, 0))  # 0
print(lower_bound(nums, 4))  # 5
print(upper_bound(nums, 0))  # 0
print(upper_bound(nums, 4))  # 5
