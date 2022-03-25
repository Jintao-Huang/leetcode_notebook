# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List

"""
C: 容量
W: 每个物品的重量
V: 每个物品的价值
目标: 使价值最大, 并返回
"""


def _k(W: List[int], V: List[int], C: int) -> int:
    # dp[i][j]: 只装[0, i)个物品, 背包容量为j, 最大价值
    # 选择: 装, 不装
    # dp[i][j]; dp[i-1][j-w[i]]; dp[i-1][j]

    dp = [[0] * (C + 1) for _ in range(len(W) + 1)]
    for i in range(1, len(W) + 1):
        for j in range(C + 1):
            # dp[0][:] = 0
            if j - W[i - 1] < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W[i - 1]] + V[i - 1])
    return dp[len(W)][C]


# 装满
def _k_full(W: List[int], V: List[int], C: int) -> int:
    # dp[i][j]: 只装[0, i)个物品, 装满背包容量j, 最大价值
    # 选择: 装, 不装
    # dp[i][j]; dp[i-1][j-w[i]]; dp[i-1][j]
    N_INF = int(-1e8)
    dp = [[N_INF] * (C + 1) for _ in range(len(W) + 1)]
    for i in range(len(W) + 1):
        for j in range(C + 1):
            if i == 0 and j == 0:
                dp[i][j] = 0
                continue
            if j - W[i - 1] < 0 or dp[i - 1][j - W[i - 1]] == N_INF:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W[i - 1]] + V[i - 1])
    return dp[len(W)][C]


def k(W: List[int], V: List[int], C: int) -> int:
    # 状态压缩
    dp = [0] * (C + 1)
    for i in range(len(W)):
        for j in reversed(range(1, C + 1)):  # 从1开始, 因为不会有W[i] <= 0
            if j - W[i] >= 0:
                dp[j] = max(dp[j], dp[j - W[i]] + V[i])  # min
    return dp[C]


# 方法数
def n_k(W: List[int], C: int) -> int:
    dp = [0] * (C + 1)
    dp[0] = 1
    for i in range(len(W)):
        for j in reversed(range(1, C + 1)):
            if j - W[i] >= 0:
                dp[j] += dp[j - W[i]]
    return dp[C]


def k_full(W: List[int], V: List[int], C: int) -> int:
    N_INF = int(-1e8)
    dp = [N_INF] * (C + 1)
    dp[0] = 0
    for i in range(len(W)):
        for j in reversed(range(1, C + 1)):
            if j - W[i] >= 0 and dp[j - W[i]] != N_INF:
                dp[j] = max(dp[j], dp[j - W[i]] + V[i])
    return dp[C]


def k_full_min(W: List[int], V: List[int], C: int) -> int:
    INF = int(1e8)
    dp = [INF] * (C + 1)  # !
    dp[0] = 0  # !
    for i in range(len(W)):
        for j in reversed(range(1, C + 1)):
            if j - W[i] >= 0 and dp[j - W[i]] != INF:  # !
                dp[j] = min(dp[j], dp[j - W[i]] + V[i])
    return dp[C]


def k_c(W: List[int], V: List[int], C: int) -> int:
    dp = [0] * (C + 1)
    for i in range(len(W)):
        for j in range(1, C + 1):  # !
            if j - W[i] >= 0:
                dp[j] = max(dp[j], dp[j - W[i]] + V[i])  # min
    return dp[C]


if __name__ == '__main__':
    W = [1, 2, 3, 4]
    V = [-1, -2, -4, -6]
    C = 5
    print(k(W, V, C))
    print(k_full(W, V, C))
    print(k_full_min(W, V, C))
    print(k_c(W, V, C))
    #
    W = [1, 2, 3, 4]
    V = [1, 2, 4, 6]
    C = 11
    print(k(W, V, C))
    print(k_full(W, V, C))
    print(k_full_min(W, V, C))
    print(k_c(W, V, C))
    """
    0
    -6
    -7
    0
    13
    -100000000
    100000000
    16
    """
