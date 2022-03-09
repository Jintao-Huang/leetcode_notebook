# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
或使用`bisect`库
"""
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """Ot(LogN) Os(1)"""
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
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo


def upper_bound(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] > target:
            hi = mid
        else:
            lo = mid + 1
    return lo

def upper_bound2(nums: List[int], target: int) -> int:
    """右边界"""
    lo, hi = -1, len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2
        if nums[mid] <= target:
            lo = mid
        else:
            hi = mid - 1
    return lo

x = [0, 0]
print(lower_bound(x, -1))
print(lower_bound(x, 0))
print(lower_bound(x, 1))
print(upper_bound(x, -1))
print(upper_bound(x, 0))
print(upper_bound(x, 1))
print(upper_bound2(x, -1))  # -1
print(upper_bound2(x, 0))  # 1
print(upper_bound2(x, 1))  # 1
