# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Deque
from collections import deque
import copy


class Solution:
    """bfs"""

    def __init__(self):
        self.mapper = {1: 0, 0: 1}

    def flip(self, mat: List[List[int]], i: int, j: int) -> List[List[int]]:
        m = copy.deepcopy(mat)
        m[i][j] = self.mapper[m[i][j]]
        if i > 0:
            m[i - 1][j] = self.mapper[m[i - 1][j]]
        if j > 0:
            m[i][j - 1] = self.mapper[m[i][j - 1]]
        if i < len(mat) - 1:
            m[i + 1][j] = self.mapper[m[i + 1][j]]
        if j < len(mat[0]) - 1:
            m[i][j + 1] = self.mapper[m[i][j + 1]]
        return m

    def hash(self, mat: List[List[int]]) -> int:

        ans = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ans *= 10
                ans += mat[i][j]

        return ans

    def is_zero(self, mat) -> bool:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != 0:
                    return False
        return True

    def minFlips(self, mat: List[List[int]]) -> int:

        q = deque([mat])  # type: Deque[List[List[int]]]
        visited = set()
        ans = 0
        while len(q) > 0:
            for _ in range(len(q)):
                #
                m = q.popleft()
                if self.is_zero(m):
                    return ans

                for i in range(len(m)):
                    for j in range(len(m[0])):
                        m2 = self.flip(m, i, j)
                        h = self.hash(m2)
                        if h not in visited:
                            visited.add(h)
                            q.append(m2)
            ans += 1
        return -1


mat = [[1, 0, 0], [1, 0, 0]]
s = Solution()
print(s.flip(mat, 0, 0))
print(s.hash(mat))
print(Solution().minFlips(mat))
