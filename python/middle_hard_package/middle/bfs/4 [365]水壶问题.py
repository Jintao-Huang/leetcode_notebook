# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from collections import deque
class Solution:
    def canMeasureWater(self, x: int,
                        y: int,
                        z: int) -> bool:
        q = deque([0])
        visited = {0}
        directions = {x, -x, y, -y}
        while len(q) > 0:
            a = q.popleft()
            for d in directions:
                a2 = a + d
                if a2 < 0 or a2 > x + y or a2 in visited:
                    continue
                if a2 == z:
                    return True
                visited.add(a2)
                q.append(a2)

        return False


jug1Capacity = 3
jug2Capacity = 5
targetCapacity = 4
print(Solution().canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity))



import math


class Solution2:
    # Bezout's identity
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # ax+by=z, a,b时整数
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0
