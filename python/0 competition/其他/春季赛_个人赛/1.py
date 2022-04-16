# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from typing import List
class Solution:
    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:

        for from_, to in operations:
            g = gem[from_] // 2
            gem[from_] -= g
            gem[to] += g
        return max(gem) - min(gem)

gem = [3,1,2]
operations = [[0,2],[2,1],[2,0]]
print(Solution().giveGem(gem, operations))
gem = [100,0,50,100]
operations = [[0,2],[0,1],[3,0],[3,0]]
print(Solution().giveGem(gem, operations))

gem = [0,0,0,0]
operations = [[1,2],[3,1],[1,2]]
print(Solution().giveGem(gem, operations))
gem = [1]
operations = []
print(Solution().giveGem(gem, operations))

