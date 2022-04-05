# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
# Ref: https://www.bilibili.com/video/BV16D4y1d7d1


"""排序笔记总结
        排序方法    时间复杂度(最好/最坏/平均)     空间复杂度       稳定性    特点
插入排序：                                                               适用于几乎有序
1. 直接插入         O(N) O(N^2) O(N^2)          O(1)            稳定      (前有序，后无序)
2. 折半插入         O(NLogN) O(N^2) O(N^2)      O(1)            稳定      搜索O(LogN), 移动O(N). (前有序，后无序)
3. 希尔            未知                         O(1)            不稳定    对每个子序列进行直插排序

交换排序                                                                  每趟排序确定一个最终位置
1. 冒泡            O(N) O(N^2) O(N^2)           O(1)           稳定       从前往后冒泡. (后有序，前无序)
2. 快速            O(NLogN) O(N^2) O(NLogN)     O(LogN)-O(N)   不稳定

选择排序                                                                  每趟排序确定一个最终位置
1. 简单选择         O(N^2) O(N^2) O(N^2)        O(1)           不稳定      (前有序，后无序)
2. 堆              O(NLogN) O(NLogN) O(NLogN)  O(1)           不稳定      非递减用大根堆. (后有序，前无序)
                                                                         建堆、删除(下滤). 插入(上滤)
二路归并排序        O(NLogN) O(NLogN) O(NLogN)  O(N)           稳定

复杂度与初始状态相关：插排 * 2, 冒泡, 快速
前有序，后无序: 直接插入, 折半插入; 简单选择
后有序，前无序: 冒泡, 堆
"""

from typing import Any, Callable, List
import time
from copy import copy

import random


def get_runtime(func, *args, **kwargs):
    t = time.time()
    result = func(*args, **kwargs)
    print(time.time() - t)
    return result


def shuffle_arr(arr: List[Any]) -> List[Any]:
    """打乱数组"""
    arr = copy(arr)
    random.shuffle(arr)
    return arr


def test_sort(func):
    # test time
    import random

    a = list(range(5000))
    random.seed(0)
    a = shuffle_arr(a)

    result = get_runtime(func, a)
    result2 = get_runtime(func, a, key=lambda x: x % 10)
    print(result[:10])
    print(result2[:10])


def test_sort_std(func):
    # test time
    import random

    a = list(range(5000))
    random.seed(0)
    a = shuffle_arr(a)

    get_runtime(func, a)
    print(a[:10])


print("sorted")
test_sort(sorted)


# sorted
# 0.0
# 0.0009980201721191406
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [3550, 1500, 3310, 530, 2970, 490, 850, 650, 3690, 3480]


def bubble(arr: List[Any], lo: int, hi: int) -> None:
    """将arr[low:high]中最大的元素冒泡到arr[high - 1]处. 比较次数: hi - 1 - lo
        Ot(N) Os(1)
    """
    for i in range(lo, hi - 1):
        # 前比后大则置换，等于则不置换(for stable)
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]


def bubble_sort(arr: List[Any], *, key: Callable[[Any], Any] = None) -> List[Any]:
    """冒泡排序 stable. 从前往后冒泡. Ot(N^2) Os(N)

    :param arr: const
    :param key: func
    :return:
    """
    # 防止重复计算key造成的性能下降、引入i为了stable
    arr = [(key(x), i, x) for i, x in enumerate(arr)] if key is not None else copy(arr)
    for n in reversed(range(2, len(arr) + 1)):  # bubble()结束位置[len, 2], 每轮比较的次数[len - 1, 1]
        bubble(arr, 0, n)  # 最大的往后扔
    return [item[2] for item in arr] if key is not None else arr


def bubble_sort_std(arr: List[Any]) -> None:
    """冒泡排序 stable. 从前往后冒泡. Ot(N^2) Os(1)"""
    # 防止重复计算key造成的性能下降、引入i为了stable
    for n in reversed(range(2, len(arr) + 1)):  # bubble()结束位置[len, 2], 每轮比较的次数[len - 1, 1]
        bubble(arr, 0, n)  # 最大的往后扔


print("bubble_sort")
test_sort(bubble_sort)
print("-----------------------")
test_sort_std(bubble_sort_std)
# bubble_sort
# 1.6645495891571045
# 1.8520421981811523
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [3550, 1500, 3310, 530, 2970, 490, 850, 650, 3690, 3480]
# -----------------------
# 1.6525754928588867
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
https://www.bilibili.com/video/BV16D4y1d7d1

tim排序：用于python的sorted()和list.sort()中
  是 二分插入排序(二分查找+) + 归并排序. Ot(NLogN) Os(N)

基于一个事实：
  现实生活中，大多数真实的数据集中，已经有很多元素是排好序的

术语：
  run(分区)：一组数据的集合(严格的单调递增或递减)
  1. 元素个数 < 64_python(或32_java)，使用二分插入排序
  2. > 64，使用tim排序
  (tim排序自己内部做的判断)

tim排序的步骤：
1. 先遍历全表，查找严格递增/递减的区间（run）(长度的讲究)，
  严格递减的部分反转得到递增
2. 分区根据一定规则合并。维持合并效率
"""


def tim_sort():
    pass


def _min(arr: List[Any], lo: int = 0, hi: int = None) -> int:
    """返回最小元素的索引"""
    hi = len(arr) if hi is None else hi
    min_idx = lo
    for i in range(lo, hi):
        if arr[min_idx] > arr[i]:
            min_idx = i
    return min_idx


def select_sort(arr: List[Any], *, key: Callable[[Any], Any] = None) -> List[Any]:
    """选择排序 not stable. Ot(N^2) Os(N)

    :param arr: const
    :param key: func
    :return:
    """
    arr = [(key(x), x) for x in arr] if key is not None else copy(arr)
    for i in range(len(arr) - 1):  # 最后一轮不需要
        min_idx = _min(arr, i)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return [item[1] for item in arr] if key is not None else arr


def select_sort_std(arr: List[Any]) -> None:
    """选择排序 not stable. Ot(N^2) Os(1)"""
    for i in range(len(arr) - 1):  # 最后一轮不需要
        min_idx = _min(arr, i)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


print("select_sort")
test_sort(select_sort)
print("-----------------------")
test_sort_std(select_sort_std)

# select_sort not stable
# select_sort
# 0.6043496131896973
# 0.9325358867645264
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# -----------------------
# 0.6562752723693848
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

from my_bisect import bisect_right, sect_right


def insert_sort(arr: List[Any], *, key: Callable[[Any], Any] = None) -> List[Any]:
    """插入排序 stable. Ot(N^2) Os(N).

    :param arr: const
    :param key: func
    :return:
    """
    # i的引入为了stable. 可以不copy（不影响const).
    arr = [(key(x), i, x) for i, x in enumerate(arr)] if key is not None else copy(arr)  # 不重复计算key
    out = []
    for x in arr:  # 需要被插入的数字
        out.insert(sect_right(out, x), x)

    return [item[2] for item in out] if key is not None else out


def insert_sort_bi(arr: List[Any], *, key: Callable[[Any], Any] = None) -> List[Any]:
    """折半插入排序 stable. Ot(N^2) Os(N). Y

    :param arr: const
    :param key: func
    :return:
    """
    # i的引入为了stable. 可以不copy（不影响const).
    arr = [(key(x), i, x) for i, x in enumerate(arr)] if key is not None else copy(arr)  # 不重复计算key
    out = []
    for x in arr:  # 需要被插入的数字
        out.insert(bisect_right(out, x), x)

    return [item[2] for item in out] if key is not None else out


def insert_sort_std(arr: List[Any]) -> None:
    """插入排序 stable. Ot(N^2) Os(1)"""
    for i in range(1, len(arr)):  # 需要被插入的数字
        t = arr[i]
        idx = sect_right(arr, t, 0, i)
        # 往后平移
        for j in reversed(range(idx, i)):  # Ot(N)
            arr[j + 1] = arr[j]
        arr[idx] = t


def insert_sort_bi_std(arr: List[Any]) -> None:
    """折半插入排序 stable. Ot(N^2) Os(1)"""
    for i in range(1, len(arr)):  # 需要被插入的数字
        t = arr[i]
        idx = bisect_right(arr, t, 0, i)
        # 往后平移
        for j in reversed(range(idx, i)):  # Ot(N)
            arr[j + 1] = arr[j]
        arr[idx] = t


print("insert_sort")
test_sort(insert_sort)
print("-----------------------")
test_sort(insert_sort_bi)
print("-----------------------")
test_sort_std(insert_sort_std)
print("-----------------------")
test_sort_std(insert_sort_bi_std)


# insert_sort
# 0.2563166618347168
# 0.32114648818969727
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [3550, 1500, 3310, 530, 2970, 490, 850, 650, 3690, 3480]
# -----------------------
# 0.008975505828857422
# 0.01197052001953125
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [3550, 1500, 3310, 530, 2970, 490, 850, 650, 3690, 3480]
# -----------------------
# 0.628321647644043
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -----------------------
# 0.3849670886993408
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def partition(arr: List[Any], lo: int, hi: int) -> int:
    """Ot(N) Os(1). [lo, hi). 返回索引"""
    value = arr[lo]  # 取第一个
    hi -= 1  # [lo, hi]
    while lo < hi:
        while lo < hi and arr[hi] >= value:
            hi -= 1
        arr[lo] = arr[hi]
        while lo < hi and arr[lo] <= value:
            lo += 1
        arr[hi] = arr[lo]
    arr[lo] = value
    return lo


def _quick_sort(arr: List[Any], lo: int, hi: int) -> None:
    """快速排序 not stable. [lo, hi)"""
    if hi - lo <= 1:  # <= 1个元素时
        return
    pivot = partition(arr, lo, hi)
    _quick_sort(arr, lo, pivot)
    _quick_sort(arr, pivot + 1, hi)


def quick_sort(arr: List[Any], *, key: Callable[[Any], Any] = None) -> List[Any]:
    """快速排序 not stable. Ot(NLogN) Os(N)

    :param arr: const
    :param key: func
    :return:
    """
    arr = [(key(x), x) for x in arr] if key is not None else copy(arr)
    _quick_sort(arr, 0, len(arr))
    return [item[1] for item in arr] if key is not None else arr


def quick_sort_std(arr: List[Any]) -> None:
    """快速排序 not stable. Ot(NLogN) Os(LogN)"""
    _quick_sort(arr, 0, len(arr))


def mid_partition(arr: List[Any], lo: int, hi: int) -> int:
    """对中间元素partition. Ot(N) Os(1)"""
    mid = (lo + hi) // 2
    arr[lo], arr[mid] = arr[mid], arr[lo]
    return partition(arr, lo, hi)


def _quick_sort2(arr: List[Any], lo: int, hi: int) -> None:
    """快速排序 not stable. [lo, hi)"""
    if hi - lo <= 1:  # <= 1个元素时
        return
    pivot = mid_partition(arr, lo, hi)
    _quick_sort2(arr, lo, pivot)
    _quick_sort2(arr, pivot + 1, hi)


def quick_sort2(arr: List[Any], *, key: Callable[[Any], Any] = None) -> List[Any]:
    """快速排序 not stable. mid_partition为了避免最坏复杂度. Ot(NLogN) Os(N)

    :param arr: const
    :param key: func
    :return:
    """
    arr = [(key(x), x) for x in arr] if key is not None else copy(arr)
    _quick_sort2(arr, 0, len(arr))
    return [item[1] for item in arr] if key is not None else arr


def quick_sort_std2(arr: List[Any]) -> None:
    """快速排序 not stable. Ot(NLogN) Os(LogN)"""
    _quick_sort2(arr, 0, len(arr))


a = list(range(10000))
a.reverse()
get_runtime(quick_sort_std2, a)
get_runtime(quick_sort_std2, a)
print(a[:10])

print("quick_sort")
test_sort(quick_sort)
print("-----------------------")
test_sort_std(quick_sort_std)


# quick_sort
# 0.008977651596069336
# 0.010937929153442383
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# -----------------------
# 0.008971929550170898
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def merge(arr: List[Any], lo: int, mid: int, hi: int) -> None:
    """mid: 是两个有序序列的分割点[lo, mid), [mid, hi). Ot(N) Os(N)"""
    b_arr = copy(arr[lo:mid])  # 复制前半部分
    i, j, k = lo, mid, 0  # arr_front, arr_mid, b_arr_front
    while j < hi and k < len(b_arr):
        if b_arr[k] <= arr[j]:
            arr[i] = b_arr[k]
            k += 1
        else:
            arr[i] = arr[j]  # 含等于
            j += 1
        i += 1
    while k < len(b_arr):
        arr[i] = b_arr[k]
        i += 1
        k += 1
    # 是同一块地
    # while j < hi:
    #     arr[i] = arr[j]
    #     i += 1
    #     j += 1


def merge2(arr: List[Any], lo: int, mid: int, hi: int) -> None:
    """简化merge. mid: 是两个有序序列的分割点[lo, mid), [mid, hi). Ot(N) Os(N)"""
    b_arr = copy(arr[lo:mid])  # 复制前半部分
    i, j, k = lo, mid, 0  # arr_front, arr_mid, b_arr_front
    while j < hi or k < len(b_arr):
        if j >= hi or k < len(b_arr) and b_arr[k] <= arr[j]:  # 使不越界
            arr[i] = b_arr[k]
            k += 1
        else:
            arr[i] = arr[j]  # 含等于
            j += 1
        i += 1


def _merge_sort(arr: List[Any], lo: int, hi: int) -> None:
    """归并排序 stable. [lo, hi)"""
    if hi - lo < 2:  # length < 2
        return
    mid = (lo + hi) // 2
    _merge_sort(arr, lo, mid)
    _merge_sort(arr, mid, hi)
    merge(arr, lo, mid, hi)  # 或用merge2


def merge_sort(arr: List[Any], *, key: Callable[[Any], Any] = None) -> List[Any]:
    """归并排序 stable. Ot(NLogN) Os(N)

    :param arr: const
    :param key: func
    :return:
    """
    arr = [(key(x), i, x) for i, x in enumerate(arr)] if key is not None else copy(arr)
    _merge_sort(arr, 0, len(arr))
    return [item[2] for item in arr] if key is not None else arr


def merge_sort_std(arr: List[Any]) -> None:
    """归并排序 stable. Ot(NLogN) Os(N)"""
    _merge_sort(arr, 0, len(arr))


print("merge_sort")
test_sort(merge_sort)
print("-----------------------")
test_sort_std(merge_sort_std)


# merge_sort
# 0.014959573745727539
# 0.017950773239135742
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [3550, 1500, 3310, 530, 2970, 490, 850, 650, 3690, 3480]
# -----------------------
# 0.015954256057739258
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def _siftdown_max(heap: List[Any], pos: int, end_pos: int) -> None:
    """下滤. 在python中的函数是(_siftup()). Ot(LogN) Os(1)"""
    child_pos = (pos << 1) + 1  # left_child
    x = heap[pos]
    while child_pos < end_pos:
        rc_pos = child_pos + 1  # right_child
        if rc_pos < end_pos and heap[rc_pos] > heap[child_pos]:
            child_pos = rc_pos
        if heap[child_pos] > x:  # python实现中，没有break语句。使用先下滤后上滤的方法（个人觉得python实现不好）
            heap[pos] = heap[child_pos]
            pos = child_pos
            child_pos = (pos << 1) + 1
        else:
            break
    heap[pos] = x


def heapify_max(heap: List[Any]) -> None:
    """Ot(N) Os(1)"""
    n = len(heap)
    for i in reversed(range(n // 2)):
        _siftdown_max(heap, i, n)


def heapswap_max(heap: List[Any], end_pos: int) -> None:
    """Ot(LogN) Os(1)"""
    if end_pos <= 1:
        return
    heap[0], heap[end_pos - 1] = heap[end_pos - 1], heap[0]
    _siftdown_max(heap, 0, end_pos - 1)


def heap_sort_std(arr: List[Any]) -> None:
    """Ot(NLogN) Os(1)"""
    heapify_max(arr)
    n = len(arr)
    for i in range(len(arr) - 1):
        end_pos = n - i
        heapswap_max(arr, end_pos)


print("heap_sort")
test_sort_std(heap_sort_std)
# heap_sort
# 0.014955997467041016
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
