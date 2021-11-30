# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/longest-palindromic-substring/
5. 最长回文子串
- 中等
- 推荐
- 相关题: 516
=
- 动态规划
"""
from functools import lru_cache
from typing import Optional, List


class Solution:
    """dfs"""

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # [i...j)
        dp = [[None for _ in range(n + 1)] for _ in range(n + 1)]  # type: List[List[Optional[bool]]]

        def _dp(i: int, j: int) -> bool:
            """s[i...j)"""
            nonlocal s
            #
            if dp[i][j] != None:
                return dp[i][j]
            #
            if j - i <= 1 or s[i] == s[j - 1] and _dp(i + 1, j - 1) is True:
                ans = True
            else:
                ans = False
            dp[i][j] = ans
            return dp[i][j]

        lo, hi = 0, 0  # [lo...hi)
        max_ = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if j - i > max_ and _dp(i, j) is True:
                    lo, hi = i, j
                    max_ = j - i
        return s[lo:hi]


s = "cbbd"
print(Solution().longestPalindrome(s))


class Solution2:
    """动态规划"""

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n + 1)] for _ in range(n + 1)]  # [i...j)
        # base
        for i in range(n):
            dp[i][i] = True
            dp[i][i + 1] = True
        #
        lo, hi = 0, 1  # [lo...hi)
        max_ = 1
        #
        for i in reversed(range(n)):
            for j in range(i + 2, n + 1):
                if s[i] == s[j - 1] and dp[i + 1][j - 1] is True:
                    dp[i][j] = True
                    #
                    if j - i > max_:
                        lo, hi = i, j
                        max_ = j - i
                    #
                else:
                    dp[i][j] = False
        return s[lo:hi]

    def longestPalindrome2(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n + 1)] for _ in range(n + 1)]  # [i...j)
        lo, hi = 0, 1  # [lo...hi)
        max_ = 1
        #
        for i in reversed(range(n)):
            for j in range(i, n + 1):
                if j - i <= 1 or s[i] == s[j - 1] and dp[i + 1][j - 1] is True:
                    dp[i][j] = True
                    #
                    if j - i > max_:
                        lo, hi = i, j
                        max_ = j - i
                    #
                else:
                    dp[i][j] = False
        return s[lo:hi]


s = "cbbd"
print(Solution2().longestPalindrome(s))
print(Solution2().longestPalindrome2(s))
