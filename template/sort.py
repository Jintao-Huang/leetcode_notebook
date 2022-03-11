# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


def partition(nums: List[int], lo: int, hi: int) -> int:
    """Ot(N) Os(1). [lo, hi]. 返回索引"""
    x = nums[lo]
    while lo < hi:
        while lo < hi and x <= nums[hi]:
            hi -= 1
        nums[lo] = nums[hi]
        while lo < hi and x >= nums[lo]:
            lo += 1
        nums[hi] = nums[lo]
    nums[lo] = x
    return lo


def _quick_sort(nums: List[int], lo: int, hi: int) -> None:
    # [lo, hi]. 先序.
    if lo >= hi:
        return
    mid = lo + (hi - lo) // 2
    nums[lo], nums[mid] = nums[mid], nums[lo]
    mid = partition(nums, lo, hi)
    _quick_sort(nums, lo, mid - 1)
    _quick_sort(nums, mid + 1, hi)


def quick_sort(nums: List[int]) -> None:
    # [lo, hi]
    return _quick_sort(nums, 0, len(nums) - 1)


def merge(nums: List[int], lo: int, mid: int, hi: int) -> None:
    """mid: 是两个有序序列的分割点[lo, mid), [mid, hi]. Ot(N) Os(N)"""
    b = nums[lo:mid].copy()
    i, j = 0, mid
    k = lo
    while i < len(b) and j <= hi:
        if b[i] <= nums[j]:
            nums[k] = b[i]
            i += 1
        else:
            nums[k] = nums[j]
            j += 1
        k += 1
    while i < len(b):
        nums[k] = b[i]
        i += 1
        k += 1


def _merge_sort(nums: List[int], lo: int, hi: int) -> None:
    # [lo, hi]. 后序
    if lo >= hi:
        return
    mid = lo + (hi - lo) // 2
    _merge_sort(nums, lo, mid)
    _merge_sort(nums, mid + 1, hi)
    merge(nums, lo, mid + 1, hi)


def merge_sort(nums: List[int]) -> None:
    _merge_sort(nums, 0, len(nums) - 1)


from template.modules.heapq import _siftdown_max, heapify_max


def heap_sort(nums: List[int]) -> None:
    heapify_max(nums)
    for hi in range(len(nums) - 1, -1, -1):
        nums[0], nums[hi] = nums[hi], nums[0]
        _siftdown_max(nums, 0, hi - 1)


if __name__ == '__main__':
    nums = [4, 1]
    partition(nums, 0, len(nums) - 1)
    print(nums)
    nums = [1, 3, 5, 7, 2, 4, 6]
    merge(nums, 0, 4, 6)
    print(nums)

    #
    nums = [1, 6, 7, 9, 4, 3, 5, 2, 0, 8]
    quick_sort(nums)
    print(nums)
    nums = [1, 6, 7, 9, 4, 3, 5, 2, 0, 8]
    merge_sort(nums)
    print(nums)
    nums = [1, 6, 7, 9, 4, 3, 5, 2, 0, 8]
    heap_sort(nums)
    print(nums)
