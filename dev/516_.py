# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/longest-palindromic-subsequence/
516. 最长回文子序列
- 中等
=
- 动态规划
"""
from functools import lru_cache


class Solution:
    """dfs"""

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        @lru_cache((n + 3) * (n + 3))
        def _dp(i: int, j: int) -> int:
            """s[i, j)"""
            nonlocal s
            #
            if j - i == 0:
                return 0
            if j - i == 1:
                return 1
            if s[i] == s[j - 1]:
                return _dp(i + 1, j - 1) + 2
            else:
                return max(_dp(i + 1, j), _dp(i, j - 1))

        return _dp(0, n)


s = "bbbab"
print(Solution().longestPalindromeSubseq(s))


class Solution2:
    """dfs. memo"""

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        memo = {}

        def _dp(i: int, j: int) -> int:
            """s[i, j)"""

            nonlocal s
            #
            if j - i == 0:
                return 0
            if j - i == 1:
                return 1
            #
            if (i, j) in memo:
                return memo[(i, j)]
            #
            if s[i] == s[j - 1]:
                ans = _dp(i + 1, j - 1) + 2
            else:
                ans = max(_dp(i + 1, j), _dp(i, j - 1))
            #
            memo[(i, j)] = ans
            return ans

        return _dp(0, n)

    def longestPalindromeSubseq2(self, s: str) -> int:
        n = len(s)
        memo = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]  # [i...j)

        def _dp(i: int, j: int) -> int:
            """s[i, j)"""

            nonlocal s
            #
            if j - i == 0:
                return 0
            if j - i == 1:
                return 1
            #
            if memo[i][j] != -1:
                return memo[i][j]
            #
            if s[i] == s[j - 1]:
                ans = _dp(i + 1, j - 1) + 2
            else:
                ans = max(_dp(i + 1, j), _dp(i, j - 1))
            #
            memo[i][j] = ans
            return ans

        return _dp(0, n)


s = "bbbab"
print(Solution2().longestPalindromeSubseq(s))
print(Solution2().longestPalindromeSubseq2(s))


class Solution3:
    """动态规划"""

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]  # [i...j)
        # base
        for i in range(n):
            dp[i][i + 1] = 1
        #
        for i in reversed(range(n)):
            for j in range(i + 2, n + 1):
                if s[i] == s[j - 1]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n]

    def longestPalindromeSubseq2(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]  # [i...j]
        # base
        for i in range(n):
            dp[i][i] = 1
        #
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


s = "bbbab"
print(Solution3().longestPalindromeSubseq(s))
print(Solution3().longestPalindromeSubseq2(s))
