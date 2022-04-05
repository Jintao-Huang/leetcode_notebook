# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List

"""6 堆排序"""


def parent(i):
    # p84
    return (i - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heapify(A: List[int], i: int, heap_size: int) -> None:
    # p86
    # 假设A[i]左右节点都满足最大堆, 算法使A[i]也满足
    l = left(i)
    r = right(i)
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)


# if __name__ == '__main__':
#     A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
#     max_heapify(A, 1)
#     print(A)

def build_max_heap(A: List[int]) -> None:
    # p87
    n = len(A)
    for i in range(parent(n - 1), -1, -1):
        max_heapify(A, i, n)


# if __name__ == '__main__':
#     A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
#     build_max_heap(A)
#     print(A)


def heap_sort(A: List[int]) -> None:
    # p89
    build_max_heap(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        max_heapify(A, 0, i)


# if __name__ == '__main__':
#     A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
#     heap_sort(A)
#     print(A)

# 优先队列
def heap_maximum(A: List[int]) -> int:
    # p91
    return A[0]


def heap_extract_max(A: List[int]) -> int:
    # p91
    n = len(A)
    if n < 1:
        raise ValueError("heap underflow")
    max_ = A[0]
    A[0] = A[n - 1]
    A.pop()
    max_heapify(A, 0, n - 1)
    return max_


# if __name__ == '__main__':
#     A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
#     print(heap_extract_max(A))
#     print(A)

def heap_increase_key(A: List[int], i: int, key: int) -> None:
    # p92
    if key < A[i]:
        raise ValueError("new key is smaller than current key")
    A[i] = key
    p = parent(i)
    while i > 0 and A[p] < A[i]:
        A[i], A[p] = A[p], A[i]
        i = p
        p = parent(i)


# if __name__ == '__main__':
#     A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
#     heap_increase_key(A, len(A) - 2, 15)
#     print(A)

def max_heap_insert(A: List[int], key: int) -> None:
    # p92
    INF = int(1e9)
    A.append(-INF)
    heap_increase_key(A, len(A) - 1, key)


# if __name__ == '__main__':
#     A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
#     max_heap_insert(A, 100)
#     print(A)


"""7 快速排序"""


def quick_sort(A: List[int], p: int, r: int) -> None:
    # p95
    # A[p..r]
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def partition(A: List[int], p: int, r: int) -> int:
    # p95
    # A[p..r]
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


# if __name__ == '__main__':
#     A = [2, 8, 7, 1, 3, 5, 6, 4]
#     print(partition(A, 0, len(A) - 1))
#     print(A)
#     quick_sort(A, 0, len(A) - 1)
#     print(A)

from random import randint


def randomized_partition(A: List[int], p: int, r: int) -> int:
    # p100
    # A[p..r]
    i = randint(p, r)
    A[i], A[r] = A[r], A[i]
    return partition(A, p, r)


def randomized_quick_sort(A: List[int], p: int, r: int) -> None:
    # p100
    # A[p..r]
    if p < r:
        q = randomized_partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

# if __name__ == '__main__':
#     A = [2, 8, 7, 1, 3, 5, 6, 4]
#     print(randomized_partition(A, 0, len(A) - 1))
#     print(A)
#     randomized_quick_sort(A, 0, len(A) - 1)
#     print(A)
