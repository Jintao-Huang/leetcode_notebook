# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Dict, Tuple
from collections import deque

from template.data_structure.priority_queue import PriorityQueue


class Solution:

    def bfs(self, v: int, es, dest: List, n: int):
        q = PriorityQueue([(0, v)])  # Tuple[int, int]  #
        visited = [False] * n
        ds = [1e8] * len(dest)
        visited[v] = True
        find = 0
        while len(q) > 0:
            d, v = q.pop()
            for i in range(len(dest)):
                if v == dest[i] and ds[i] == 1e8:
                    find += 1
                    ds[i] = d
                    break
            if find == len(dest):
                return ds
            if v not in es:
                continue
            now_visited = []
            for f, w in es[v]:
                if visited[f] is True:
                    continue
                now_visited.append(f)
                q.add((d + w, f))
            for f in now_visited:
                visited[f] = True

        return ds

    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        es = {}  # type: Dict[int, List[Tuple[int, int]]]
        for e in edges:
            f, t, w = e
            if t not in es:
                es[t] = []
            es[t].append((f, w))

        d1, d2 = self.bfs(dest, es, [src1, src2], n)
        if d1 <= d2:
            d2 = min(d2, self.bfs(src1, es, [src2], n)[0])
        else:
            d1 = min(d1, self.bfs(src2, es, [src1], n)[0])
        ans = d1 + d2

        return -1 if ans >= 1e8 else ans


n = 81
edges = [[9,63,69],[9,1,65],[9,72,82],[9,70,65],[9,28,33],[35,64,49],[9,44,41],[35,43,98],[9,17,55],[35,74,54],[9,48,24],[9,53,50],[9,29,54],[9,38,10],[9,39,7],[35,76,28],[35,60,1],[9,49,87],[9,40,23],[9,0,56],[35,50,14],[35,79,90],[9,3,68],[9,6,8],[9,31,61],[35,34,87],[9,42,87],[9,4,81],[9,26,75],[9,46,43],[9,19,24],[35,45,69],[35,10,72],[35,57,72],[35,51,42],[9,58,53],[9,52,53],[9,30,80],[35,75,84],[9,18,46],[9,21,23],[35,2,6],[9,68,70],[9,16,25],[35,77,60],[9,71,17],[35,41,76],[35,66,11],[35,14,2],[35,7,98],[9,24,26],[9,69,25],[35,55,35],[9,23,44],[9,32,60],[35,59,43],[9,62,94],[35,56,11],[9,13,74],[35,67,83],[35,15,18],[35,54,91],[35,33,49],[9,80,57],[35,20,86],[35,11,39],[35,73,58],[35,8,58],[35,22,70],[35,12,83],[35,61,79],[35,78,38],[35,47,41],[35,25,67],[35,65,11],[9,27,55],[9,36,65],[35,37,96],[9,5,90],[65,5,56],[79,5,42],[3,5,77]]
src1 = 35
src2 = 9
dest = 5
print(Solution().minimumWeight(n, edges, src1, src2, dest))

# n = 3
# edges = [[0,1,1],[2,1,1]]
# src1 = 0
# src2 = 1
# dest = 2
# print(Solution().minimumWeight(n, edges, src1, src2, dest))

# n = 8
# edges = [[4, 7, 24], [1, 3, 30], [4, 0, 31], [1, 2, 31], [1, 5, 18], [1, 6, 19], [4, 6, 25], [5, 6, 32], [0, 6, 50]]
# src1 = 4
# src2 = 1
# dest = 6
# print(Solution().minimumWeight(n, edges, src1, src2, dest))
# # 32
#
# n =  6
# edges = [[0,1,22],[0,5,11],[0,2,7],[4,3,4],[5,3,48],[5,3,17],[4,3,45]]
# src1 =4
# src2 = 0
# dest =3
#
# print(Solution().minimumWeight(n, edges, src1, src2, dest))

# n = 5
# edges = [[4,2,20],[4,3,46],[0,1,15],[0,1,43],[0,1,32],[3,1,13]]
# src1 =0
# src2 =4
# dest =1
# print(Solution().minimumWeight(n, edges, src1, src2, dest))
#

