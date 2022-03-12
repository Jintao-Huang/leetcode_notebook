# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Tuple


def _siftup(heap: List[int], i: int) -> None:
    # 上滤
    x = heap[i]
    while i > 0:
        pi = (i - 2) >> 1
        p = heap[pi]
        if p <= x:
            break
        heap[i] = p
        i = p
    heap[i] = x


def _siftdown(heap: List[int], i: int, hi: int) -> None:
    # heap: [0, hi]. 下滤
    ci = (i << 1) + 1
    x = heap[i]
    while ci <= hi:
        cri = ci + 1
        if cri <= hi and heap[cri] < heap[ci]:
            ci = cri
        if x <= heap[ci]:
            break
        heap[i] = heap[ci]
        i = ci
        ci = (i << 1) + 1
    heap[i] = x


def _siftup_max(heap: List[int], i: int) -> None:
    # 上滤. 大根堆
    x = heap[i]
    while i > 0:
        pi = (i - 2) >> 1
        p = heap[pi]
        if p >= x:
            break
        heap[i] = p
        i = p
    heap[i] = x


def _siftdown_max(heap: List[int], i: int, hi: int) -> None:
    # heap: [0, hi]. 下滤. 大根堆
    ci = (i << 1) + 1
    x = heap[i]
    while ci <= hi:
        cri = ci + 1
        if cri <= hi and heap[cri] > heap[ci]:
            ci = cri
        if x >= heap[ci]:
            break
        heap[i] = heap[ci]
        i = ci
        ci = (i << 1) + 1
    heap[i] = x


def heapify(heap: List[int]):
    n = len(heap)
    for i in reversed(range(n // 2)):
        _siftdown(heap, i, n - 1)


def heapify_max(heap: List[int]):
    n = len(heap)
    for i in reversed(range(n // 2)):
        _siftdown_max(heap, i, n - 1)


def heappush(heap: List[int], x: int) -> None:
    heap.append(x)
    _siftup(heap, len(heap) - 1)


def heappop(heap: List[int]) -> int:
    x = heap.pop()
    if len(heap) > 0:
        x, heap[0] = heap[0], x
        _siftdown(heap, 0, len(heap) - 1)
    return x


def heappush_max(heap: List[int], x: int) -> None:
    heap.append(x)
    _siftup_max(heap, len(heap) - 1)


def heappop_max(heap: List[int]) -> int:
    x = heap.pop()
    if len(heap) > 0:
        x, heap[0] = heap[0], x
        _siftdown_max(heap, 0, len(heap) - 1)
    return x


def heapreplace(heap: List[int], x: int) -> int:
    # 相当于先pop, 后push. 不会返回x.
    if len(heap) > 0:
        x, heap[0] = heap[0], x
        _siftdown(heap, 0, len(heap) - 1)
    return x


def heappushpop(heap: List[int], x: int) -> int:
    """可能会返回x"""
    if len(heap) > 0 and x > heap[0]:
        x, heap[0] = heap[0], x
        _siftdown(heap, 0, len(heap) - 1)
    return x


def heapreplace_max(heap: List[int], x: int) -> int:
    # 相当于先pop, 后push. 不会返回x.
    if len(heap) > 0:
        x, heap[0] = heap[0], x
        _siftdown_max(heap, 0, len(heap) - 1)
    return x


def heappushpop_max(heap: List[int], x: int) -> int:
    """可能会返回x"""
    if len(heap) > 0 and x < heap[0]:
        x, heap[0] = heap[0], x
        _siftdown_max(heap, 0, len(heap) - 1)
    return x


def _merge(nums_list: List[List[int]]) -> List[int]:
    # 多路归并
    ans = []
    n = len(nums_list)
    heap = []  # type: List[Tuple[int, int, int]]
    for i in range(n):
        nums = nums_list[i]
        if len(nums) > 0:
            heap.append((nums[0], i, 0))
    if len(heap) == 0:
        return ans
    heapify(heap)
    while len(heap) > 1:
        val, i, j = heap[0]
        ans.append(val)
        nums = nums_list[i]
        j += 1
        if j < len(nums):
            heapreplace(heap, (nums[j], i, j))
        else:
            heappop(heap)
    val, i, j = heap[0]
    return ans + nums_list[i][j:]


def _nlargest(nums: List[int], k: int) -> List[int]:
    ans = nums[:k].copy()
    heapify(ans)
    for i in range(k, len(nums)):
        x = nums[i]
        if x > ans[0]:  # 替换最小的
            heapreplace(ans, x)
    return ans


def _nsmallest(nums: List[int], k: int) -> List[int]:
    ans = nums[:k].copy()
    heapify_max(ans)
    for i in range(k, len(nums)):
        x = nums[i]
        if x < ans[0]:  # 替换最小的
            heapreplace_max(ans, x)
    return ans


if __name__ == '__main__':
    nums_list = [
        [1, 3, 5, 7],
        [2, 4, 6],
        [0, 8],
        [],
        [4]
    ]
    print(_merge(nums_list))

    nums = [1, 5, 3, 8, 4, 10, 2]
    print(_nlargest(nums, 5))
    print(_nsmallest(nums, 5))
