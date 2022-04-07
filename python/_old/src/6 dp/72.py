# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/edit-distance/
72. 编辑距离
- 困难
- 推荐
=
- 动态规划
"""
from functools import lru_cache


class Solution:
    """dfs"""

    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)

        @lru_cache((n1 + 3) * (n2 + 3))
        def _dp(i: int, j: int) -> int:
            """word1[0...i) word2[0...j) 最小编辑次数"""
            nonlocal word1, word2
            # base
            if i == 0:
                return j
            if j == 0:
                return i
            #
            if word1[i - 1] == word2[j - 1]:
                return _dp(i - 1, j - 1)
            else:
                return min([
                    _dp(i - 1, j) + 1,  # 删
                    _dp(i, j - 1) + 1,  # 插
                    _dp(i - 1, j - 1) + 1  # 换
                ])

        return _dp(n1, n2)


word1 = "horse"
word2 = "ros"
print(Solution().minDistance(word1, word2))


class Solution2:
    """动态规划"""

    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]  # 初始化
        #
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                # base
                if i == 0:
                    dp[i][j] = j
                    continue
                if j == 0:
                    dp[i][j] = i
                    continue
                #
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min([
                        dp[i - 1][j] + 1,  # 删
                        dp[i][j - 1] + 1,  # 插
                        dp[i - 1][j - 1] + 1  # 换
                    ])
        return dp[n1][n2]


word1 = "horse"
word2 = "ros"
print(Solution2().minDistance(word1, word2))
