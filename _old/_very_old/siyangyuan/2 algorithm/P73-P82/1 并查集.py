# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

class Solution200:
    """岛屿数量. 见DFS"""


from typing import List


class UnionFind:
    def __init__(self, length: int):
        self.father: List[int] = [-1] * length
        self.rank: List[int] = [0] * length

    def find(self, x: int) -> int:
        """O(1)"""
        if self.father[x] == -1:
            return x
        else:
            self.father[x] = self.find(self.father[x])
            return self.father[x]

    def union(self, a: int, b: int) -> bool:
        """O(1)"""
        root_a: int = self.find(a)
        root_b: int = self.find(b)
        if root_a == root_b:
            return False
        if self.rank[root_a] > self.rank[root_b]:
            self.father[root_b] = root_a
        elif self.rank[root_a] < self.rank[root_b]:
            self.father[root_a] = root_b
        else:
            self.father[root_b] = root_a
            self.rank[root_a] += 1
        return True


class Solution547:
    """省份数量"""

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """并查集. Ot(N^2LogN) Os(N)"""
        length = len(isConnected)
        uf_set = UnionFind(length)
        res = length
        for i in range(length):
            for j in range(i + 1, length):
                if isConnected[i][j] and uf_set.union(i, j):
                    res -= 1
        return res

    def findCircleNum2(self, isConnected: List[List[int]]) -> int:
        """深搜(python中递归比迭代快). Ot(N^2) Os(N)"""
        is_visited = [False] * len(isConnected)
        res = 0

        def dfs(idx: int) -> None:
            is_visited[idx] = True
            for i in range(len(isConnected)):
                if not is_visited[i] and isConnected[idx][i] == 1:
                    dfs(i)

        for i in range(len(isConnected)):
            if not is_visited[i]:
                dfs(i)
                res += 1
        return res


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(Solution547().findCircleNum(isConnected))
print(Solution547().findCircleNum2(isConnected))
