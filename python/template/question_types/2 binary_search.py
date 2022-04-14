# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


"""二分法
1. 存在ans的必要条件. mid看作ans: 二分法(lower_bound)
   1. hi初始化为len-1, len. 区别.
   2. 最高位一定是(隐式的)正确答案. (即满足必要条件)
   3. ans是满足必要条件的最小值.
2. 若存在ans的充要条件: 三分法+外判断.
"""

"""
或使用`bisect`库
"""
from typing import List


def binary_search(nums: List[int], target: int) -> bool:
    """Ot(LogN) Os(1)"""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2  # 偶数时: 中点偏左
        if target == nums[mid]:
            return True
        elif nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return target == nums[lo]


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
    """右边界. 最左边]"""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2  # !
        if nums[mid] <= target:
            lo = mid  # !
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
