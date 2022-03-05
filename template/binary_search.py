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
    while lo <= hi:
        mid = lo + (hi - lo) // 2  # 偶数时: 中点偏左
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


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


# [lower_bound2, upper_bound2]
# lower_bound2与lower_bound功能类似. upper_bound2与upper_bound差别巨大
def lower_bound2(nums: List[int], target: int) -> int:
    """lower_bound2框架."""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] >= target:
            hi = mid
        else:  # 相等与小于时等价的
            lo = mid + 1
    return lo if nums[lo] == target else -1


def upper_bound2(nums: List[int], target: int) -> int:
    """upper_bound2框架."""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2
        if nums[mid] <= target:
            lo = mid
        else:
            hi = mid - 1
    return lo if nums[lo] == target else -1


nums = [0, 1]
print(lower_bound(nums, 0))  # 0
print(upper_bound(nums, 0))  # 1
print(lower_bound2(nums, 0))  # 0
print(upper_bound2(nums, 0))  # 0

nums = [0, 0]
print(lower_bound(nums, 0))  # 0
print(upper_bound(nums, 0))  # 2
print(lower_bound2(nums, 0))  # 0
print(upper_bound2(nums, 0))  # 1

nums = [-1]
print(lower_bound(nums, 0))  # 1
print(upper_bound(nums, 0))  # 1
print(lower_bound2(nums, 0))  # -1
print(upper_bound2(nums, 0))  # -1

nums = [1]
print(lower_bound(nums, 0))  # 0
print(upper_bound(nums, 0))  # 0
print(lower_bound2(nums, 0))  # -1
print(upper_bound2(nums, 0))  # -1

nums = [-1, 1]
print(lower_bound(nums, 0))  # 1
print(upper_bound(nums, 0))  # 1
print(lower_bound2(nums, 0))  # -1
print(upper_bound2(nums, 0))  # -1

nums = [False, False, True, True]
print(lower_bound2(nums, False))  # 0
print(lower_bound2(nums, True))  # 2
print(upper_bound2(nums, False))  # 1
print(upper_bound2(nums, True))  # 3

# 1. 第一版的使用: 会出现越界索引
# 2. 第二版的使用:

# nums = [1, 2, 2, 2, 3]
# print(binary_search(nums, 2))
# print(lower_bound(nums, 2))  # 1
# print(upper_bound(nums, 2))  # 4
# #
# print(lower_bound(nums, 0))  # 0
# print(lower_bound(nums, 4))  # 5
# print(upper_bound(nums, 0))  # 0
# print(upper_bound(nums, 4))  # 5
# # 同上
# print(bisect_left(nums, 2))
# print(bisect_right(nums, 2))
# #
# print(bisect_left(nums, 0))
# print(bisect_left(nums, 4))
# print(bisect_right(nums, 0))
# print(bisect_right(nums, 4))
