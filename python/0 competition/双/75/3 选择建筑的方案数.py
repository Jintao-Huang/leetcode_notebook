# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from typing import List


class Solution:
    def numberOfWays(self, s: str) -> int:
        # C: 0, 1
        # S: [i][2][3]. i之前的方案数, 最后一个字母, 含几个
        # dp_N^2[i][j][k]; dp_N^2[i-1][j][k]; dp_N^2[i-1][~j][k-1]
        dp = [[0] * 2 for _ in range(3)]
        for i in range(len(s)):
            for j in reversed(range(3)):
                if j == 0:
                    if s[i] == '0':
                        dp[j][0] += 1
                    else:
                        dp[j][1] += 1
                    continue
                if s[i] == '0':
                    dp[j][0] = dp[j - 1][1] + dp[j][0]
                else:
                    dp[j][1] = dp[j - 1][0] + dp[j][1]
        return sum(dp[2])


from functools import lru_cache


class Solution:
    def numberOfWays(self, A: str) -> int:
        ans = n0 = n1 = n10 = n01 = 0
        for v in A:
            if v == '1':
                n01 += n0
                n1 += 1
                ans += n10
            else:
                n10 += n1
                n0 += 1
                ans += n01
        return ans


s = "001101"
print(Solution().numberOfWays(s))
