# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from typing import List

"""8 线性时间排序"""

"""
1. p108. 比较排序下界. n!个叶节点, 树高O(nlogn)
"""


def counting_sort(A: List[int], B: List[int], k: int) -> None:
    # p109
    # A: 输入数组, B: 存放排序的输出
    # 假设n个输入元素中的每一个都是在0到K区间内的一个整数. [0..K]
    C = [0] * (k + 1)  # 临时数组. 作用: A_val -> B_idx
    for j in range(len(A)):
        C[A[j]] += 1
    # 对每一个输入元素x, 确定小于x 的元素个数
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    # 稳定
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        # 相同元素, 不能放在同一个输出位置上
        C[A[j]] -= 1


# if __name__ == '__main__':
#     A = [2, 5, 3, 0, 2, 3, 0, 3]
#     B = [0] * len(A)
#     k = max(A)
#     counting_sort(A, B, k)
#     print(B)

def _counting_sort(A: List[str], B: List[str], idx: int, lo: int, hi: int) -> None:
    # 专门为radix sort设计的计数排序
    k = hi - lo  # [lo..hi]
    C = [0] * (k + 1)  # 临时数组. 作用: A_val -> B_idx
    for j in range(len(A)):
        C[ord(A[j][idx]) - lo] += 1
    # 对每一个输入元素x, 确定小于x 的元素个数
    for i in range(1, len(C)):
        C[i] += C[i - 1]
    # 稳定
    for j in range(len(A) - 1, -1, -1):
        B[C[ord(A[j][idx]) - lo] - 1] = A[j]
        # 相同元素, 不能放在同一个输出位置上
        C[ord(A[j][idx]) - lo] -= 1


def radix_sort(A: List[str], d: int) -> None:
    # p111, 这里进行了部分修改, 将抽象语义转为具体业务
    # B: 用于输出
    # 基数排序应用: 身份证排序
    # 此函数功能: 用于字符串字典序排序. only a-z
    # 稳定
    B = ['0' * d for _ in range(len(A))]
    C = A
    for i in reversed(range(d)):
        _counting_sort(C, B, i, ord('a'), ord('z'))
        C, B = B, C
    if id(A) != id(C):
        for i in range(len(C)):
            A[i] = C[i]


# if __name__ == '__main__':
#     d = 3
#     A = ['aaa', 'bac', 'bbd', 'abd', 'zda', 'daf', 'dcc', 'aab', 'zdb', 'abf', 'ddd']
#     radix_sort(A, d)
#     print(A)

# 桶排序
def COPY_insertion_sort(A: List[int]) -> None:
    # p10
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


def bucket_sort(A: List[float]) -> None:
    # p112
    # B: 用于输出
    # 桶排序假设输入数据服从均匀分布, 且分布在[0, 1)区间上
    # 稳定
    # 桶排序用于浮点数排序. 计数排序不能用于浮点数. 思想是类似的
    n = len(A)
    B = [[] for _ in range(n)]
    for i in range(n):
        # 相当于计数排序的范围[0..n-1]
        B[int(n * A[i])].append(A[i])
    for i in range(n):
        COPY_insertion_sort(B[i])

    i = 0
    j = 0
    while i < n:
        for k in range(len(B[j])):
            A[i] = B[j][k]
            i += 1
        j += 1


# if __name__ == '__main__':
#     A = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
#     bucket_sort(A)
#     print(A)


"""9 中位数和顺序统计量"""


def minimum(A: List[int]) -> int:
    # p120
    min_ = A[0]
    for i in range(1, len(A)):
        if min_ > A[i]:
            min_ = A[i]
    return min_


# if __name__ == '__main__':
#     A = [5, 3, 2, 7]
#     print(minimum(A))


def COPY_partition(A: List[int], p: int, r: int) -> int:
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


from random import randint


def COPY_randomized_partition(A: List[int], p: int, r: int) -> int:
    # p100
    # A[p..r]
    i = randint(p, r)
    A[i], A[r] = A[r], A[i]
    return COPY_partition(A, p, r)


def random_select(A: List[int], p: int, r: int, i: int) -> int:
    # p121
    # 功能: 返回第i小的元素, >=1
    if p == r:
        return A[p]
    q = COPY_randomized_partition(A, p, r)
    k = q - p + 1
    if k == i:
        return A[q]
    elif i < k:
        return random_select(A, p, q - 1, i)
    else:
        return random_select(A, q + 1, r, i - k)

# if __name__ == '__main__':
#     A = [1, 3, 5, 7, 9, 8, 6, 4, 2]
#     print(random_select(A, 0, len(A) - 1, 5))
