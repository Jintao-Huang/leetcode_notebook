# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/longest-common-subsequence/
1143. 最长公共子序列
- 中等
- 推荐
=
- 动态规划
"""

from functools import lru_cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """dfs"""
        n1, n2 = len(text1), len(text2)

        @lru_cache((n1 + 3) * (n2 + 3))
        def _dp(i, j):
            """text1[0...i)与text2[0...j)的LCS"""
            nonlocal text1, text2
            # base
            if i == 0 or j == 0:
                return 0
            #
            if text1[i - 1] == text2[j - 1]:
                return 1 + _dp(i - 1, j - 1)
            else:
                return max(_dp(i, j - 1), _dp(i - 1, j))

        return _dp(n1, n2)


text1 = "abcde"
text2 = "ace"
print(Solution().longestCommonSubsequence(text1, text2))


class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """dfs"""
        n1, n2 = len(text1), len(text2)
        dp = [[0 for _ in range(n2 + 1)].copy() for _ in range(n1 + 1)]  # 含base
        #
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                #
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[n1][n2]


text1 = "abcde"
text2 = "ace"
print(Solution2().longestCommonSubsequence(text1, text2))
