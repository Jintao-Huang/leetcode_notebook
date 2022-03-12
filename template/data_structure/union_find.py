# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]  # type: List[int]
        self.rank = [0] * n  # type: List[int]

    def find(self, a: int) -> int:
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a: int, b: int) -> bool:
        """返回是否union成功. """
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        if self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        elif self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1
        return True
