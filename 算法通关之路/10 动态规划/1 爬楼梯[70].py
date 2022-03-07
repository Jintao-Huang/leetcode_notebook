# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
class Solution:
    """动态规划. Ot(N) Os(N). """

    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        for i in range(2, n):
            dp.append(dp[i - 2] + dp[i - 1])
        return dp[n - 1]


class Solution2:
    """动态规划-空间优化. Ot(N) Os(1). """

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        x, y = 1, 2
        for i in range(2, n):
            x, y = y, x + y
        return y


print(Solution().climbStairs(2))
print(Solution2().climbStairs(2))
