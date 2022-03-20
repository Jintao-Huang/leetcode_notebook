# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Dict


class Solution:
    """拓扑排序. 检测无回边"""

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
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        es = {}  # type: Dict[int, List[int]]  # 出边
        # 0: 未访问
        # 1: 正访问
        # 2: 访问完
        visited = [0] * numCourses

        for cur, prev in prerequisites:
            if prev not in es:
                es[prev] = []
            es[prev].append(cur)

        for i in range(numCourses):
            if visited[i] == 0:
                visited[i] = 1
                if not self._dfs(i, es, visited):
                    return False

        return True


numCourses = 4
prerequisites = [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]
print(Solution().canFinish(numCourses, prerequisites))
