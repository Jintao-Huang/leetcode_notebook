# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


class Solution:
    """动态规划. 注意: n+1. """

    def minDistance(self, word1: str, word2: str) -> int:
        # 选择: 匹配/不匹配
        # dp_N^2[i][j]: i结尾. 匹配完word2中第j个
        # dp_N^2[i][j]; dp_N^2[i-1][j-1];dp_N^2[i-1][j-1], dp_N^2[i-1][j], dp_N^2[i][j-1]
        dp = [[0] * (len(word2)+ 1) for _ in range(len(word1) + 1)]
        # base解决越界情况
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0:
                    dp[i][j] = j
                    continue
                if j == 0:
                    dp[i][j] = i
                    continue
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j - 1],
                        dp[i - 1][j],
                        dp[i][j - 1]
                    ) + 1
        return dp[len(word1)][len(word2)]


word1 = "horse"
word2 = "ros"
print(Solution().minDistance(word1, word2))
