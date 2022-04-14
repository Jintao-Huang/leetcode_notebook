# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
# Union Find需要是无向图
# 后序DFS, 不能处理双向图情况
from typing import List


class Solution:
    # DFS逆向思维
    def dfs(self, heights, i, j, visited, n, m, dp):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dp[i][j] = True
        for d in directions:
            pi, pj = i + d[0], j + d[1]
            if pi < 0 or pj < 0 or pi >= n or pj >= m:
                continue
            if heights[pi][pj] < heights[i][j]:
                continue
            if visited[pi][pj]:
                continue
            visited[pi][pj] = True
            self.dfs(heights, pi, pj, visited, n, m, dp)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        dp_p = [[False] * m for _ in range(n)]
        dp_a = [[False] * m for _ in range(n)]
        v1 = [[False] * m for _ in range(n)]
        v2 = [[False] * m for _ in range(n)]

        for i in range(n):
            v1[i][0] = True
            self.dfs(heights, i, 0, v1, n, m, dp_p)
            v2[i][m - 1] = True
            self.dfs(heights, i, m - 1, v2, n, m, dp_a)
        for j in range(m):
            v1[0][j] = True
            self.dfs(heights, 0, j, v1, n, m, dp_p)
            v2[n - 1][j] = True
            self.dfs(heights, n - 1, j, v2, n, m, dp_a)
        ans = []
        for i in range(n):
            for j in range(m):
                if dp_p[i][j] and dp_a[i][j]:
                    ans.append([i, j])

        return ans


# heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
# print(Solution().pacificAtlantic(heights))
heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print(Solution().pacificAtlantic(heights))
