# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


class Solution:
    def minInsertions(self, s: str) -> int:
        # dp_N^2[i][j]: s[i:j+1]回文串, 最小插入次数
        # dp_N^2[i][j]; dp_N^2[i+1][j-1]; dp_N^2[i+1][j], dp_N^2[i][j-1]
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = 0
                    continue
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
        return dp[0][len(s) - 1]


s = "leetcode"
print(Solution().minInsertions(s))
