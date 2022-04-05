# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Any


"""
left:
-10  0  10
(-inf, -10]; (-10, 0]; (0, 10]; (10, inf) 
right:
(-inf, -10); [-10, 0); [0, 10); [10, inf) 
"""
def bisect_left(arr: List[Any], x: Any, lo: int = 0, hi: int = None) -> int:
    """在arr中找到x合适的插入点以维持有序. Ot(LogN) Os(1)"""
    # 没有len: 位置. len=1: 元素
    hi = len(arr) if hi is None else hi
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid  # 等于往左
    return lo


def _bisect_left(arr: List[Any], x: Any, lo: int = 0, hi: int = None) -> int:
    """另一种写法，但是可读性不好. Ot(LogN) Os(1)"""
    hi = len(arr) if hi is None else hi
    hi -= 1  # 范围是闭区间
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo


"""
1. hi: hi = mid; 
2. while lo < hi;
"""


def bisect_right(arr: List[Any], x: Any, lo: int = 0, hi: int = None) -> int:
    """在arr中找到x合适的插入点以维持有序。Ot(LogN) Os(1)"""
    hi = len(arr) if hi is None else hi
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] <= x:
            lo = mid + 1  # 等于往右
        else:
            hi = mid
    return lo


def binary_search(arr: List[Any], x: Any, lo: int = 0, hi: int = None) -> bool:
    """Ot(LogN) Os(1)"""
    hi = len(arr) if hi is None else hi
    while lo < hi:
        mid = (lo + hi) // 2
        if x == arr[mid]:
            return True
        elif x > arr[mid]:
            lo = mid + 1
        else:
            hi = mid
    return False


def binary_search2(arr: List[Any], x: Any, lo: int = 0, hi: int = None) -> int:
    """没找到返回-1. Ot(LogN) Os(1)"""
    hi = len(arr) if hi is None else hi
    while lo < hi:
        mid = (lo + hi) // 2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            lo = mid + 1
        else:
            hi = mid
    return -1


def sect_left(arr: List[Any], x: Any, lo: int = 0, hi: int = None) -> int:
    """在arr中找到x合适的插入点以维持有序. Ot(N) Os(1)"""
    hi = len(arr) if hi is None else hi
    for i in range(lo, hi):  # O(N)
        if x <= arr[i]:
            return i
    else:
        return hi


def sect_right(arr: List[Any], x: Any, lo: int = 0, hi: int = None) -> int:
    """在arr中找到x合适的插入点以维持有序。Ot(N) Os(1)"""
    hi = len(arr) if hi is None else hi
    for i in reversed(range(lo, hi)):  # O(N)
        if arr[i] <= x:
            return i + 1
    else:
        return lo


a = []
print(sect_left(a, 1))
print(sect_right(a, 1))
