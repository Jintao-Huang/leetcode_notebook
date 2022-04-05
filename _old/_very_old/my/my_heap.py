# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
import heapq
import random
from typing import List, Any, Iterable, Callable, Generator
from copy import copy
import time

"""
heapq._heappop_max()
heapq._heapify_max()
heapq._heapreplace_max()
heapq._siftdown_max()
heapq._siftup_max()
"""


def shuffle_arr(arr: List[Any]) -> List[Any]:
    """打乱数组"""
    arr = copy(arr)
    random.seed(0)
    random.shuffle(arr)
    return arr


def test_time(func):
    a = list(range(100000))
    a2 = shuffle_arr(a)
    a3 = [(-x, x) for x in a2]
    t = time.time()
    func(a2)
    print(time.time() - t)
    print(a2[:100])
    t = time.time()
    func(a3)
    print(time.time() - t)
    print([x[1] for x in a3][:100])


# 0.003996372222900391
# 0.005984306335449219

def _siftup(heap: List[Any], start_pos: int, pos: int) -> None:
    """上滤. 在python中的函数是(_siftdown()). Ot(LogN) Os(1)"""
    x = heap[pos]
    while pos > start_pos:
        parent_pos = (pos - 1) >> 1
        parent = heap[parent_pos]
        if parent > x:
            heap[pos] = parent
            pos = parent_pos
        else:
            break
    heap[pos] = x


def _siftdown(heap: List[Any], pos: int) -> None:
    """下滤. 在python中的函数是(_siftup()). Ot(LogN) Os(1)"""
    end_pos = len(heap)
    child_pos = (pos << 1) + 1
    x = heap[pos]
    while child_pos < end_pos:
        child_right_pos = child_pos + 1
        if child_right_pos < end_pos and heap[child_right_pos] < heap[child_pos]:
            child_pos = child_right_pos
        if heap[child_pos] < x:  # python实现中，没有break语句。使用先下滤后上滤的方法（个人觉得python实现不好）
            heap[pos] = heap[child_pos]
            pos = child_pos
            child_pos = (pos << 1) + 1
        else:
            break
    heap[pos] = x


def heapify(heap: List[Any]) -> None:
    """Ot(N) Os(1)"""
    n = len(heap)
    for i in reversed(range(n // 2)):
        _siftdown(heap, i)


test_time(heapify)
test_time(heapq.heapify)


# 0.033911705017089844
# 0.03886008262634277
# 0.003958225250244141
# 0.006015300750732422

def heappush(heap: List[Any], x: Any) -> None:
    """Ot(LogN) Os(1)"""
    heap.append(x)
    _siftup(heap, 0, len(heap) - 1)  # 上滤


def heappop(heap: List[Any]) -> Any:
    """Ot(LogN) Os(1)"""
    x = heap.pop()
    if heap:  # heap is not None or len(heap) != 0
        return_x = heap[0]
        heap[0] = x
        _siftdown(heap, 0)
        return return_x
    return x


def heappushpop(heap: List[Any], x: Any) -> Any:
    """Ot(LogN) Os(1)"""
    if heap and heap[0] < x:
        x, heap[0] = heap[0], x
        _siftdown(heap, 0)
    return x


def heapreplace(heap: List[Any], x: Any) -> Any:
    """Ot(LogN) Os(1)"""
    if heap:  # 除非heap[0] < x，不然与heappushpop()一致
        x, heap[0] = heap[0], x
        _siftdown(heap, 0)
    return x


def merge(*iterables: Iterable[Any], key: Callable[[Any], Any] = None, reverse: bool = False) -> Generator:
    """适用于多路merge的情况. Ot(K + NLogK) Os(K), 其中N为总元素个数, K为路数"""
    heap = []
    # 将所有迭代器的第一个元素 放入堆中
    for it in iterables:
        try:
            it = iter(it)
            heap.append((next(it), it))
        except StopIteration:
            pass
    heapify(heap)  # O(K), K路
    # 一直取最小(剩下最后一个元素)
    while len(heap) > 1:
        try:
            while True:
                value, it = heap[0]  # 取最小
                yield value
                heapreplace(heap, (next(it), it))  # Log(K)
        except StopIteration:
            heappop(heap)  # 有it空了
    # heap最后一个元素
    if heap:
        value, it = heap[0]
        yield value
        yield from it  # 不需要heapreplace()了，效率更高
    return


def nsmallest(n: int, iterable: Iterable[Any], key: Callable[[Any], Any] = None) -> List[Any]:
    """Ot(K + NLogK) Os(K)"""
    it = iter(iterable)
    out = [x for _, x in zip(range(n), it)]
    if len(out) == 0:
        return out
    heapq._heapify_max(out)  # O(K), K = n
    # 不断替换小根堆中的元素
    for x in it:  # O(N)
        if x < out[0]:
            heapq._heapreplace_max(out, x)  # heappushpop()也行. O(LogK)
    out.sort()
    return out


a = list(range(10))
a2 = shuffle_arr(a)
print(nsmallest(5, a2))
print(nsmallest(5, [1, 2, 3]))
print(nsmallest(0, []))


def nlargest(n: int, iterable: Iterable[Any], key: Callable[[Any], Any] = None) -> List[Any]:
    """Ot(K + NLogK) Os(K)

    方法1: 直接sorted排序(tim sort). Ot(NLogN) Os(N). 一般用于K = N时
    方法2: 冒泡、选择. Ot(NK) Os(K). 一般用于K = 1时
    方法3: 最小堆(剩下的为最大的n个. python官方实现). Ot(K + NLogK) Os(K). 一般用于K !<< N, K < N时（K较大）
    方法4: 最大堆. Ot(N + KLogN) Os(K). 一般用于K较小时
    """
    # 建立小根堆
    it = iter(iterable)
    out = [x for _, x in zip(range(n), it)]
    if len(out) == 0:
        return out
    heapify(out)  # O(K), K = n
    # 不断替换小根堆中的元素
    for x in it:  # O(N)
        if x > out[0]:
            heapreplace(out, x)  # heappushpop()也行. O(LogK)
    out.sort(reverse=True)
    return out


a = list(range(10))
a2 = shuffle_arr(a)
print(nlargest(5, a2))
print(nlargest(5, [1, 2, 3]))
print(nlargest(0, []))

a = list(range(7))
a2 = shuffle_arr(a)
heapify(a2)
print(a2)
a3 = a2.copy()
x = -3
print(heappushpop(a2, x))
print(heapreplace(a3, x))
print(a2, a3)


def test_correct():
    a = list(range(7))
    a2 = shuffle_arr(a)
    print(a2)
    heapify(a2)
    print(a2)
    heappush(a2, -1)
    print(a2)
    print(heappop(a2))
    print(a2)
    # [4, 2, 1, 0, 5, 3, 6]
    # [0, 2, 1, 4, 5, 3, 6]
    # [-1, 0, 1, 2, 5, 3, 6, 4]
    # -1
    # [0, 2, 1, 4, 5, 3, 6]

    a = list(range(7))
    a2 = shuffle_arr(a)
    print(a2)
    heapq.heapify(a2)
    print(a2)
    heapq.heappush(a2, -1)
    print(a2)
    print(heapq.heappop(a2))
    print(a2)
    # [4, 2, 1, 0, 5, 3, 6]
    # [0, 2, 1, 4, 5, 3, 6]
    # [-1, 0, 1, 2, 5, 3, 6, 4]
    # -1
    # [0, 2, 1, 4, 5, 3, 6]


print(list(heapq.merge([1, 3, 5, 7], [2, 4, 6, 8], [0, 10])))
print(list(merge([1, 3, 5, 7], [2, 4, 6, 8], [0, 10])))
print(list(merge()))
