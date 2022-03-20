# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


class Solution:
    """动态规划. Ot(N^2) Os(N^2). 空间复杂度可降"""

    def longestPalindromeSubseq(self, s: str) -> int:
        # dp[i][j]: s[i:j+1]
        # dp[i][j]; s[i+1][j-1]; s[i+1][j],s[i][j-1]
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        #
        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = 1
                    continue
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2  # i+1不会越界
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][len(s) - 1]


s = "bbbab"
print(Solution().longestPalindromeSubseq(s))
