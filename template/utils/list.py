# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from typing import List, Dict, Tuple, Union


def unique(nums: List[int]) -> None:
    """条件: nums有序"""
    lo = 1  # 写入指针
    for hi in range(1, len(nums)):
        if nums[hi] != nums[hi - 1]:
            nums[lo] = nums[hi]
            lo += 1
    for i in range(lo, len(nums)):
        nums.pop()


if __name__ == '__main__':
    l = [1, 1, 2, 2, 3]
    unique(l)
    print(l)


def counter(nums: List[int], need_sorted: bool = False) -> Union[Dict, List[List[int]]]:
    """返回 按字典序."""
    d = {}
    for x in nums:
        if x not in d:
            d[x] = 0
        d[x] += 1
    #
    if need_sorted:
        keys = sorted(d.keys())
        return [[k, d[k]] for k in keys]
    else:
        return d


def find(arr: List[int], target: int):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def reverse(arr: List[int], lo: int, hi: int) -> None:
    """[lo, hi]"""
    while lo < hi:
        arr[lo], arr[hi] = arr[hi], arr[lo]
        lo += 1
        hi -= 1


def bubble(arr, start, end) -> int:
    ans = 0
    if start < end:
        for i in range(start, end):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            ans += 1
    else:
        for i in range(start, end, -1):
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            ans += 1
    return ans
