# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


def MCS(nums: List[int]) -> int:
    """最大连续子序列. Ot(N)"""
    dp = nums.copy()  # 初始状态
    for i in range(1, len(nums)):
        dp[i] += max(dp[i - 1], 0)  # 转义方程
    return max(dp)


nums = [10, -2, -7, 4, -5, 4]
print(MCS(nums))  # 10

"""
注意子串(连续)与子序列(可不连续)的区别
"""


def LIS(nums: List[int]) -> int:
    """最长递增子序列. Ot(N^2)"""
    # 初始状态
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(0, i):
            if nums[i] > nums[i - 1]:  # 转移方程
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


nums = [10, -2, -9, 4, -5, 4]
print(LIS(nums))  # 3


def LCS(s1: str, s2: str) -> int:
    """最长公共子序列. Ot(Len(S1)Len(S2))"""
    dp = [[-1] * len(s2) for _ in range(len(s1))]  # S1 * S2
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[i][j] = (dp[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0) + 1
            else:
                dp[i][j] = max(dp[i - 1][j] if i - 1 >= 0 else 0, dp[i][j - 1] if j - 1 >= 0 else 0)
    return dp[len(s1) - 1][len(s2) - 1]


s1 = "abbccadd"
s2 = "abacd"
print(LCS(s1, s2))  # 4

"""最多一个"""
def backpack_01(v: List[int], w: List[int], C: int) -> int:
    """C: 容量. N: 数量. v: 价值. w: 重量.
    v含负数时，不需要把背包C全部填满. Ot(Len(V)C)"""
    dp = [0] * C
    for i in range(len(v)):
        for j in reversed(range(w[i] - 1, C)):
            k = j - w[i]
            dp[j] = max(dp[j], (dp[k] if k >= 0 else 0) + v[i])  # !!!
        print(dp)
    return dp[C - 1]


def backpack_01_all_min(v: List[int], w: List[int], C: int) -> int:
    """C: 容量. N: 数量. v: 价值. w: 重量. 需要把背包C全部填满. Ot(Len(V)C)"""
    INF = 0x7fffffff // 10
    dp = [INF] * C
    for i in range(len(v)):
        for j in reversed(range(w[i] - 1, C)):
            k = j - w[i]
            dp[j] = min(dp[j], (dp[k] if k >= 0 else 0) + v[i])  # !!!
    return dp[C - 1] if dp[C - 1] != INF else 0


def backpack_01_all_max(v: List[int], w: List[int], C: int) -> int:
    """C: 容量. N: 数量. v: 价值. w: 重量. 需要把背包C全部填满. Ot(Len(V)C)"""
    INF = -0x7fffffff // 10
    dp = [INF] * C
    for i in range(len(v)):
        for j in reversed(range(w[i] - 1, C)):
            k = j - w[i]
            if k < 0 or dp[k] != INF:  # !!!
                dp[j] = max(dp[j], (dp[k] if k >= 0 else 0) + v[i])
    return dp[C - 1] if dp[C - 1] != INF else 0


v = [-1, -2, -4, -6]
w = [1, 2, 3, 4]
C = 5
print(backpack_01(v, w, C))  # 0
print(backpack_01_all_min(v, w, C))  # -7
print(backpack_01_all_max(v, w, C))  # -6

v = [1, 2, 4, 6]
w = [1, 2, 3, 4]
C = 11
print(backpack_01(v, w, C))  # 13
print(backpack_01_all_min(v, w, C))  # 0
print(backpack_01_all_max(v, w, C))  # 0


"""无限量"""
def backpack_c(v: List[int], w: List[int], C: int) -> int:
    """Ot(Len(V)C)"""
    dp = [0] * C
    for i in range(len(v)):
        for j in range(w[i] - 1, C):  # !!!
            k = j - w[i]
            dp[j] = max(dp[j], (dp[k] if k >= 0 else 0) + v[i])
    return dp[C - 1]


def backpack_c_all_min(v: List[int], w: List[int], C: int) -> int:
    """Ot(Len(V)C)"""
    INF = 0x7fffffff // 10
    dp = [INF] * C
    for i in range(len(v)):
        for j in range(w[i] - 1, C):
            k = j - w[i]
            dp[j] = min(dp[j], (dp[k] if k >= 0 else 0) + v[i])
    return dp[C - 1] if dp[C - 1] != INF else 0


def backpack_c_all_max(v: List[int], w: List[int], C: int) -> int:
    """Ot(Len(V)C)"""
    INF = -0x7fffffff // 10
    dp = [INF] * C
    for i in range(len(v)):
        for j in range(w[i] - 1, C):
            k = j - w[i]
            if k < 0 or dp[k] != INF:
                dp[j] = max(dp[j], (dp[k] if k >= 0 else 0) + v[i])
    return dp[C - 1] if dp[C - 1] != INF else 0


v = [-1, -2, -4, -6]
w = [1, 2, 3, 4]
C = 5
print(backpack_c(v, w, C))  # 0
print(backpack_c_all_min(v, w, C))  # -7
print(backpack_c_all_max(v, w, C))  # -5

v = [1, 2, 4, 6]
w = [1, 2, 3, 4]
C = 11
print(backpack_c(v, w, C))  # 16
print(backpack_c_all_min(v, w, C))  # 11
print(backpack_c_all_max(v, w, C))  # 16

"""多重背包问题略. 思想时转化成01背包"""
