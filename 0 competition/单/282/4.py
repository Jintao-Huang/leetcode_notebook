# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List


class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:

        INF = int(1e10)
        ts = [INF] * 18  # [0, 16]
        ts[0] = 0
        for i in range(len(tires)):
            fi, ri = tires[i]
            s = 0
            t = fi
            for j in range(1, 18):
                s += t
                ts[j] = min(ts[j], s)
                t *= ri
                if t - fi >= changeTime:
                    break

        for i in range(ts.count(INF)):
            ts.pop()


        dp = [INF] * (numLaps + 1)
        dp[0] = -changeTime
        for i in range(1, numLaps + 1):
            for j in range(1, len(ts)):
                if i - j < 0:
                    break
                dp[i] = min(dp[i], dp[i - j] + ts[j] + changeTime)

        return dp[numLaps]


tires = [[1, 10], [2, 2], [3, 4]]
changeTime = 6
numLaps = 5
print(Solution().minimumFinishTime(tires, changeTime, numLaps))
tires = [[2, 3], [3, 4]]
changeTime = 5
numLaps = 4
print(Solution().minimumFinishTime(tires, changeTime, numLaps))
