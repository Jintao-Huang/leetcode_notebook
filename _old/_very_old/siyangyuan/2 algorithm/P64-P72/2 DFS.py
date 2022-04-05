# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution938:
    """二叉搜索树的范围和"""

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        """DFS. Ot(N) Os(N)"""
        stack = [root]
        res = 0
        while len(stack) > 0:
            x = stack.pop()
            if x is None:
                continue
            if low <= x.val <= high:
                res += x.val
            stack += [x.right, x.left]
        return res

    def rangeSumBST2(self, root: TreeNode, low: int, high: int) -> int:
        """BFS. Ot(N) Os(N)"""
        queue = deque([root])
        res = 0
        while len(queue) > 0:
            x = queue.popleft()
            if x is None:
                continue
            if low <= x.val <= high:
                res += x.val
            queue += [x.right, x.left]
        return res

    def rangeSumBST3(self, root: TreeNode, low: int, high: int) -> int:
        """DFS剪枝. Ot(N) Os(N)"""
        stack = [root]
        res = 0
        while len(stack) > 0:
            x = stack.pop()
            if x is None:
                continue
            if low <= x.val <= high:
                res += x.val
            if x.val < high:
                stack.append(x.right)
            if low < x.val:
                stack.append(x.left)
        return res

    def rangeSumBST4(self, root: TreeNode, low: int, high: int) -> int:
        """BFS剪枝. Ot(N) Os(N)"""
        queue = deque([root])
        res = 0
        while len(queue) > 0:
            x = queue.popleft()
            if x is None:
                continue
            if low <= x.val <= high:
                res += x.val
            if x.val < high:
                queue.append(x.right)
            if low < x.val:
                queue.append(x.left)
        return res


root = TreeNode(10)

print(Solution938().rangeSumBST(root, 7, 15))
print(Solution938().rangeSumBST2(root, 7, 15))
print(Solution938().rangeSumBST3(root, 7, 15))
print(Solution938().rangeSumBST4(root, 7, 15))

"""减少类的数组. 尽量用数组的类。空间利用会提高"""


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


class Solution200:
    """岛屿数量"""

    def numIslands(self, grid: List[List[str]]) -> int:
        """深搜. Ot(MN)"""
        len_g = len(grid)
        len_g0 = len(grid[0])
        res = 0

        def dfs():
            while len(stack) > 0:
                i, j = stack.pop()
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < len_g and 0 <= y < len_g0 and grid[x][y] == '1':
                        grid[x][y] = '0'  # 和递归不同
                        stack.append((x, y))

        for i in range(len_g):
            for j in range(len_g0):
                if grid[i][j] == '1':
                    res += 1
                    grid[i][j] = '0'
                    stack = [(i, j)]  # pos: i, j
                    dfs()

        return res

    def numIslands2(self, grid: List[List[str]]) -> int:
        """深搜. Ot(MN)"""
        len_g = len(grid)
        len_g0 = len(grid[0])
        res = 0

        def dfs(i, j):
            grid[i][j] = '0'
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < len_g and 0 <= y < len_g0 and grid[x][y] == '1':
                    dfs(x, y)

        for i in range(len_g):
            for j in range(len_g0):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)

        return res

    def numIslands3(self, grid: List[List[str]]) -> int:
        """广搜. Ot(MN)"""
        len_g = len(grid)
        len_g0 = len(grid[0])
        res = 0

        def bfs():
            while len(queue) > 0:
                i, j = queue.popleft()
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < len_g and 0 <= y < len_g0 and grid[x][y] == "1":
                        grid[x][y] = '0'
                        queue.append((x, y))

        for i in range(len_g):
            for j in range(len_g0):
                if grid[i][j] == '1':
                    res += 1
                    grid[i][j] = '0'
                    queue = deque([(i, j)])  # pos: i, j
                    bfs()
        return res

    def numIslands4(self, grid: List[List[str]]) -> int:
        res = 0
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    res += 1

        uf_set = UnionFind(r * c)
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':  # 两次 == '1' 的比较 说明互联
                    grid[i][j] = '0'
                    for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                        if 0 <= x < r and 0 <= y < c and grid[x][y] == '1':
                            a = i * c + j
                            b = x * c + y
                            if uf_set.union(a, b):
                                res -= 1
        return res


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
grid1 = [g.copy() for g in grid]
grid2 = [g.copy() for g in grid]
grid3 = [g.copy() for g in grid]
print(Solution200().numIslands(grid))
print(Solution200().numIslands2(grid1))
print(Solution200().numIslands3(grid2))
print(Solution200().numIslands4(grid3))
