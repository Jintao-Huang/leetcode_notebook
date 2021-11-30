# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
1312. 让字符串成为回文串的最少插入次数
- 困难
=
- 动态规划
"""

from functools import lru_cache


class Solution:
    """dfs"""

    def minInsertions(self, s: str) -> int:
        n = len(s)

        @lru_cache((n + 3) * (n + 3))
        def _dp(i: int, j: int) -> int:
            """[i...j)"""
            nonlocal s
            # base
            if j - i <= 1:
                return 0

            #
            if s[i] == s[j - 1]:
                return _dp(i + 1, j - 1)
            else:
                return min(_dp(i + 1, j), _dp(i, j - 1)) + 1

        return _dp(0, n)


s = "leetcode"
print(Solution().minInsertions(s))


class Solution2:
    """动态规划"""

    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n + 1)] for _ in range(n)]  # [i...j)
        #
        for i in reversed(range(n - 1)):
            for j in range(i + 2, n + 1):
                #
                if s[i] == s[j - 1]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
        return dp[0][n]

    def minInsertions2(self, s: str) -> int:
        """状态压缩"""
        n = len(s)
        dp = [0 for _ in range(n + 1)]  # [i...j). 省略i
        #
        for i in reversed(range(n - 1)):
            prev = 0
            for j in range(i + 2, n + 1):
                #
                temp = dp[j]
                if s[i] == s[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + 1
                prev = temp
        return dp[n]


s = "zzazz"
print(Solution2().minInsertions(s))
print(Solution2().minInsertions2(s))
