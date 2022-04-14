# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class UnionFind:
    # 这里使用每个集合的大小count作为重量平衡指标, 而不是树高height.
    def __init__(self, n: int):
        self._parent = [-1 for _ in range(n)]  # type: List[int]
        self._count = [1] * n  # type: List[int]  # 节点数
        self.cnt = n

    def find(self, a: int) -> int:
        if self._parent[a] == -1:
            return a
        self._parent[a] = self.find(self._parent[a])
        return self._parent[a]

    def count(self, a) -> int:
        return self._count[self.find(a)]

    def union(self, a: int, b: int) -> bool:
        """返回是否union成功. """
        root_a, root_b = self.find(a), self.find(b)
        if root_a == root_b:
            return False
        if self._count[root_a] >= self._count[root_b]:
            self._parent[root_b] = root_a
            self._count[root_a] += self._count[root_b]
        else:
            self._parent[root_a] = root_b
            self._count[root_b] += self._count[root_a]
        self.cnt -= 1
        return True


if __name__ == '__main__':
    uf = UnionFind(10)
    print(uf.union(0, 1))
    print(uf.union(0, 1))
    print(uf.union(2, 3))
    print(uf.union(1, 5))
    print(uf.union(1, 2))
    print(uf.count(1))

# 通常实现
# class UnionFind:
#     def __init__(self, n: int):
#         self.parent = [i for i in range(n)]  # type: List[int]
#         self.rank = [0] * n  # type: List[int]
#
#     def find(self, a: int) -> int:
#         if self.parent[a] != a:
#             self.parent[a] = self.find(self.parent[a])
#         return self.parent[a]
#
#     def union(self, a: int, b: int) -> bool:
#         """返回是否union成功. """
#         root_a, root_b = self.find(a), self.find(b)
#         if root_a == root_b:
#             return False
#         if self.rank[root_a] > self.rank[root_b]:
#             self.parent[root_b] = root_a
#         elif self.rank[root_a] < self.rank[root_b]:
#             self.parent[root_a] = root_b
#         else:
#             self.parent[root_b] = root_a
#             self.rank[root_a] += 1
#         return True
