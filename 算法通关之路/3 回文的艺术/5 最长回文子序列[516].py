# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

class Solution:
    """记忆库. Ot(N^2) Os(N^2)"""

    def __init__(self):
        self.dp = None
        self.s = None

    def _dp(self, i: int, j: int) -> int:

        if self.dp[i][j] != -1:
            return self.dp[i][j]
        if i == j:
            self.dp[i][j] = 1
        elif i > j:
            self.dp[i][j] = 0
        else:
            if self.s[i] == self.s[j]:
                self.dp[i][j] = self._dp(i + 1, j - 1) + 2
            else:
                self.dp[i][j] = max(self._dp(i, j - 1), self._dp(i + 1, j))
        return self.dp[i][j]

    def longestPalindromeSubseq(self, s: str) -> int:
        self.s = s
        self.dp = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        #
        return self._dp(0, len(s) - 1)


class Solution2:
    """动态规划. Ot(N^2) Os(N^2). 空间复杂度可降"""

    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        #
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return dp[0][len(s) - 1]


print(Solution().longestPalindromeSubseq("cbbd"))
print(Solution2().longestPalindromeSubseq("cbbd"))
