# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Tuple, Dict

"""2 算法基础"""


def insertion_sort(A: List[int]) -> None:
    # p10
    # 稳定
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


# if __name__ == '__main__':
#     A = [5, 2, 4, 6, 1, 3]
#     insertion_sort(A)
#     print(A)


# 归并排序
def merge(A: List[int], p: int, q: int, r: int) -> None:
    # p17
    # A[p..q], A[q+1..r]
    INF = int(1e9)
    n1 = q - p + 1
    n2 = r - q
    L, R = [0] * (n1 + 1), [0] * (n2 + 1)
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j + 1]
    L[n1] = INF
    R[n2] = INF
    i, j = 0, 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


# if __name__ == '__main__':
#     A = [100, 2, 4, 5, 7, 1, 2, 3, 6, 100]
#     merge(A, 1, 4, 8)
#     print(A)

def merge_sort(A: List[int], p: int, r: int) -> None:
    # p19
    # A[p..r]
    # 稳定
    if p < r:
        q = ((p + r) // 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)


# if __name__ == '__main__':
#     A = [5, 2, 4, 7, 1, 3, 2, 6]
#     merge_sort(A, 0, len(A) - 1)
#     print(A)

"""4 分治策略"""


# 最大子数组问题
def find_max_crossing_subarray(A: List[int], low: int, mid: int, high: int) \
        -> Tuple[int, int, int]:
    # p40
    # A[lo..mid], A[mid+1..hi]
    INF = int(1e9)
    left_sum = -INF
    sum_ = 0
    for i in range(mid, low - 1, -1):
        sum_ += A[i]
        if sum_ > left_sum:
            left_sum = sum_
            max_left = i
    right_sum = -INF
    sum_ = 0
    for j in range(mid + 1, high + 1):
        sum_ += A[j]
        if sum_ > right_sum:
            right_sum = sum_
            max_right = j
    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray(A: List[int], low: int, high: int) \
        -> Tuple[int, int, int]:
    # p41
    # A[low..high]
    if high == low:
        return low, high, A[low]
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


# if __name__ == '__main__':
#     A = [13, -3, -25, -20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
#     print(find_max_crossing_subarray(A, 0, 8, len(A) - 1))
#     print(find_maximum_subarray(A, 0, len(A) - 1))


# naive矩阵乘法
def square_matrix_multiply(A: List[List[int]], B: List[List[int]]) \
        -> List[List[int]]:
    # p43
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


# if __name__ == '__main__':
#     A = [[1, 2], [3, 4]]
#     B = [[4, 3], [2, 1]]
#     print(square_matrix_multiply(A, B))


"""
1. p44. square_matrix_multiply_recursive(A, B). 略
2. p45. Strassen 方法
3. p54. 主定理
"""

"""5 概率分析和随机算法"""

"""
1. p64 hire_assistant(n). 略
2. p70 randomized_hire_assistant(n). 略
"""

from random import randint, seed


# permute
def permute_by_sorting(A: List[int]) -> None:
    # p70
    n = len(A)
    P = [0] * n
    for i in range(n):
        P[i] = randint(1, n ** 3)  # a <= N <= b
    idxs = sorted(range(n), key=lambda i: P[i])
    B = A.copy()
    for i in range(n):
        A[i] = B[idxs[i]]


def randomize_in_place(A: List[int]) -> None:
    # p70
    # A顺序不变的概率: 1/n!
    n = len(A)
    for i in range(n):
        x = randint(i, n - 1)
        A[i], A[x] = A[x], A[i]


# if __name__ == '__main__':
#     A = [1, 2, 3, 4]
#     permute_by_sorting(A)
#     print(A)
#     #
#     randomize_in_place(A)
#     print(A)

def on_line_maximum(scores: List[int], k: int) -> int:
    # p78
    # 每次面试后, 或者我们必须马上提供职位给应聘者, 或者马上拒绝该应聘者
    # k: 超参数, 前k个都拒绝
    INF = int(1e9)
    n = len(scores)
    best_score = -INF
    for i in range(k):
        if scores[i] > best_score:
            best_score = scores[i]
    for i in range(k, n):
        if scores[i] > best_score:
            return i
    return n - 1

# if __name__ == '__main__':
#     scores = list(range(10000))
#     randomize_in_place(scores)
#     idx = on_line_maximum(scores, 100)
#     print(scores[idx])
