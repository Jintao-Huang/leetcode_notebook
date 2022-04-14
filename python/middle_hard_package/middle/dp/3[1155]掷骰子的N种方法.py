# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

class Solution:
    # 零钱问题: 选择: 有无; 该题: 1-k
    # 选择: 到达该状态的可能数
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = int(1e9) + 7
        # dp[i][j]. n=i个骰子. target=j的方法数
        # dp[i][j]; dp[i-1][j-{1..k}]
        # R: dp[n][target]
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(1, n + 1):
            for j in reversed(range(target + 1)):  # i只能投掷一次. 01背包
                dp[j] = 0
                for kk in range(1, k + 1):
                    if j - kk < 0:
                        continue
                    dp[j] += dp[j - kk]
                    dp[j] %=  MOD
        return dp[target]



print(Solution().numRollsToTarget(1, 6, 3))
print(Solution().numRollsToTarget(2, 6, 7))
print(Solution().numRollsToTarget(30, 30, 500))
