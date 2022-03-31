# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List


class Solution:
    def __init__(self):
        self.ans = [], 0

    def dfs(self, path, n_arrows, aliceArrows, i, s) -> None:
        if n_arrows >= 0 and s > self.ans[1]:
            self.ans = path.copy(), s
            self.ans[0][0] += n_arrows
        for i in range(i, len(aliceArrows)):
            nums = aliceArrows[i] + 1
            path[i] = nums
            self.dfs(path, n_arrows - nums, aliceArrows, i + 1, s + i)
            path[i] = 0

    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        path = [0] * len(aliceArrows)
        self.dfs(path, numArrows, aliceArrows, 0, 0)
        return self.ans[0]


# numArrows = 9
# aliceArrows = [1, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0]
# print(Solution().maximumBobPoints(numArrows, aliceArrows))
#
# numArrows = 3
# aliceArrows = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2]
# print(Solution().maximumBobPoints(numArrows, aliceArrows))

numArrows = 89
aliceArrows = [3, 2, 28, 1, 7, 1, 16, 7, 3, 13, 3, 5]
print(Solution().maximumBobPoints(numArrows, aliceArrows))
