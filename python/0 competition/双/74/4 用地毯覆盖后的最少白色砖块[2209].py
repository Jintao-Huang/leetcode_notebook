# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        if numCarpets * carpetLen >= len(floor):
            return 0
        # C: 盖, 不盖
        # S: [i][j]: 前i块, j块毯子, 最少白块
        dp = [[0] * (numCarpets + 1) for _ in range(len(floor) + 1)]
        for i in range(1, len(floor) + 1):
            for j in range(numCarpets + 1):
                dp[i][j] = min(dp[i - 1][j] + (1 if floor[i - 1] == '1' else 0),
                               dp[i - carpetLen][j - 1] if i - carpetLen >= 0 and j - 1 >= 0 else 1e8)
        return dp[len(floor)][numCarpets]


floor = "10000"

numCarpets = 1
carpetLen = 2
print(Solution().minimumWhiteTiles(floor, numCarpets, carpetLen))
