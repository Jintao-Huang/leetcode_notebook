# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List


# [lower_bound, upper_bound)
def bisect_left(nums: List[int], x: int,
                lo: int = 0, hi: int = None) -> int:
    """lower_bound. [lo, hi)"""
    if hi is None:
        hi = len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] >= x:
            hi = mid
        else:
            lo = mid + 1
    return lo


def bisect_right(nums: List[int], x: int,
                 lo: int = 0, hi: int = None) -> int:
    """upper_bound."""
    if hi is None:
        hi = len(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] > x:
            hi = mid
        else:
            lo = mid + 1
    return lo


if __name__ == '__main__':
    x = [0, 0]
    print(bisect_right(x, -1, 0, len(x)))
    print(bisect_right(x, 0))
    print(bisect_right(x, 1))
    print(bisect_left(x, -1))
    print(bisect_left(x, 0))
    print(bisect_left(x, 1))

    from bisect import bisect_left, bisect_right

    x = [0, 0]
    print(bisect_right(x, -1, 0, len(x)))
    print(bisect_right(x, 0))
    print(bisect_right(x, 1))
    print(bisect_left(x, -1))
    print(bisect_left(x, 0))
    print(bisect_left(x, 1))
