# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
class Solution:
    """动态规划"""

    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j]: s[:i], p[:j], 是否匹配
        # dp[i][j]; dp[i][j-2], dp[i-1][j]

        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            for j in range(len(p) + 1):
                if j == 0:
                    dp[i][j] = i == 0
                    continue
                if i == 0:
                    if p[j - 1] == '*':
                        dp[i][j] = dp[i][j - 2]
                    else:
                        dp[i][j] = False
                    continue

                if p[j - 1] == '*':
                    if p[j - 2] == '.' or s[i - 1] == p[j - 2]:
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2]  # 0次/n次
                    else:
                        dp[i][j] = dp[i][j - 2]
                    continue
                    # 不含 * 匹配 *的情况.

                if p[j - 1] == '.' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = False
        return dp[len(s)][len(p)]


# s = "mississippi"
# p = "mis*is*ip*."
# print(Solution().isMatch(s, p))
#
# s = "aaa"
# p = "aaaa"
# print(Solution().isMatch(s, p))
# s = "aab"
# p = "c*a*b"
# print(Solution().isMatch(s, p))
#
#
# s = "aa"
# p = "a"
# s = "aa"
# p = "a*"
# print(Solution().isMatch(s, p))

s = "a*"
p = "a*"
print(Solution().isMatch(s, p))
