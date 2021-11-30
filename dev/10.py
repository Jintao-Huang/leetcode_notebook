# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/regular-expression-matching/
10. 正则表达式匹配
- 困难
=
- 动态规划
"""

from functools import lru_cache


class Solution:
    """dfs"""

    def isMatch(self, s: str, p: str) -> bool:
        n1 = len(s)
        n2 = len(p)

        @lru_cache((n1 + 3) * (n2 + 3))
        def _dp(i: int, j: int) -> bool:
            """[i...n1), [j...n2)"""
            # base
            if j == n2:
                return i == n1
            if i == n1:
                # 能否匹配空串
                if (n2 - j) % 2 != 0:
                    return False
                for k in range(j + 1, n2, 2):
                    if p[k] != "*":
                        return False
                return True
            #
            if s[i] == p[j] or p[j] == '.':
                if j + 1 < n2 and p[j + 1] == "*":
                    return _dp(i + 1, j) or _dp(i, j + 2)
                else:
                    return _dp(i + 1, j + 1)
            else:
                if j + 1 < n2 and p[j + 1] == "*":
                    return _dp(i, j + 2)
                else:
                    return False

        return _dp(0, 0)


s = "aab"
p = "c*a*b"

print(Solution().isMatch(s, p))


class Solution2:
    """动态规划"""

    def isMatch(self, s: str, p: str) -> bool:
        n1 = len(s)
        n2 = len(p)
        dp = [[False for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        for i in reversed(range(n1 + 1)):
            for j in reversed(range(n2 + 1)):
                # base
                if j == n2:
                    dp[i][j] = i == n1
                    continue
                if i == n1:
                    # 能否匹配空串
                    if (n2 - j) % 2 != 0:
                        dp[i][j] = False
                        continue
                    #
                    continue_for = False
                    for k in range(j + 1, n2, 2):
                        if p[k] != "*":
                            dp[i][j] = False
                            continue_for = True
                            break
                    if continue_for:
                        continue
                    #
                    dp[i][j] = True
                    continue
                #
                if s[i] == p[j] or p[j] == '.':
                    if j + 1 < n2 and p[j + 1] == "*":
                        dp[i][j] = dp[i + 1][j] or dp[i][j + 2]
                    else:
                        dp[i][j] = dp[i + 1][j + 1]
                else:
                    if j + 1 < n2 and p[j + 1] == "*":
                        dp[i][j] = dp[i][j + 2]
                    else:
                        dp[i][j] = False

        return dp[0][0]


s = "aab"
p = "c*a*b"
print(Solution2().isMatch(s, p))

