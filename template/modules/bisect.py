# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List


# [lower_bound, upper_bound)
def bisect_left(arr: List[int], x: int,
                lo: int = 0, hi: int = None) -> int:
    """lower_bound."""
    hi = len(arr) - 1 if hi is None else hi
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:  # 相等与小于时等价的
            hi = mid - 1
    return lo


def bisect_right(arr: List[int], x: int,
                 lo: int = 0, hi: int = None) -> int:
    """upper_bound."""
    hi = len(arr) - 1 if hi is None else hi

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] <= x:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo
