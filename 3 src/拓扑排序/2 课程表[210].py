# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List, Dict


# 拓扑排序 A->B: B依赖A
class Solution:
    """dfs"""

    def __init__(self):
        self.ans: List[int]

    def _dfs(self, v: int, es: Dict[int, List[int]], visited: List[int]) -> bool:
        vs = es[v] if v in es else []
        for v2 in vs:
            if visited[v2] == 1:
                return False
            elif visited[v2] == 2:
                continue
            visited[v2] = 1
            if not self._dfs(v2, es, visited):
                return False
        visited[v] = 2
        self.ans.append(v)
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        es = {}  # type: Dict[int, List[int]]  # 出边
        # 0: 未访问
        # 1: 正访问
        # 2: 访问完
        visited = [0] * numCourses
        self.ans = []

        for cur, prev in prerequisites:
            if prev not in es:
                es[prev] = []
            es[prev].append(cur)

        for i in range(numCourses):
            if visited[i] == 0:
                visited[i] = 1
                if not self._dfs(i, es, visited):
                    return []

        return self.ans[::-1]


print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))

from collections import deque


class Solution2:
    """bfs"""

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        es = [[] for _ in range(numCourses)]  # type: List[List[int]]  # 出边
        de = [0] * numCourses  # 入度
        for to, from_ in prerequisites:
            es[from_].append(to)
            de[to] += 1

        q = deque([])
        for i, d in enumerate(de):
            if d == 0:
                q.append(i)
        ans = []
        while len(q) > 0:
            v = q.popleft()  # type: int
            ans.append(v)
            for e in es[v]:
                de[e] -= 1
                if de[e] == 0:
                    q.append(e)
        if len(ans) != numCourses:
            return []
        return ans


print(Solution2().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
print(Solution2().findOrder(3, [[1, 0], [1, 2], [0, 1]]))
