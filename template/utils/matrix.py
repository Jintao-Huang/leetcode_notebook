# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


def matrix_chain(matrices: List[List[int]]) -> int:
    n = len(matrices)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        dp[i][i + 1] = matrices[i][0] * matrices[i][1] * matrices[i + 1][1]

    for i in reversed(range(n - 1)):
        for j in range(i + 2, n):
            dp[i][j] = min(dp[i + 1][j] + matrices[i][0] * matrices[i][1] * matrices[j][1],
                           dp[i][j - 1] + matrices[i][0] * matrices[j][0] * matrices[j][1])

    return dp[0][n - 1]

if __name__ == '__main__':
    matrices = [[50, 10], [10, 40], [40, 30], [30, 5]]
    print(matrix_chain(matrices))
