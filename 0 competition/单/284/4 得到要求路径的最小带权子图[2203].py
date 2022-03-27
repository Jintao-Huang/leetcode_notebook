# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Dict, Tuple

from template.utils.graph import dijkstra



class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        es = [[] for _ in range(n)]  # type: List[List[Tuple[int, int]]]
        es_r = [[] for _ in range(n)]  # type: List[List[Tuple[int, int]]]
        for e in edges:
            f, t, w = e
            es[f].append((t, w))
            es_r[t].append((f, w))


        d1, d2, d3 = dijkstra(es, src1), dijkstra(es, src2), dijkstra(es_r, dest)

        ans = -1
        for i in range(n):
            if d1[i] != -1 and d2[i] != -1 and d3[i] != -1:
                d = d1[i] + d2[i] + d3[i]
                if ans == -1 or d < ans:
                    ans = d
        return ans


n = 6
edges = [[0, 2, 2], [0, 5, 6], [1, 0, 3], [1, 4, 5], [2, 1, 1], [2, 3, 3], [2, 3, 4], [3, 4, 2], [4, 5, 1]]
src1 = 0
src2 = 1
dest = 5

print(Solution().minimumWeight(n, edges, src1, src2, dest))
