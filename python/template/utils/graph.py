# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List, Tuple
from python.template.data_structure.priority_queue import PriorityQueue


def dijkstra(es: List[List[Tuple[int, int]]], start: int) -> List[int]:
    # e: Tuple[v, d]
    #
    ans = [-1] * len(es)  # 距离
    ans[start] = 0
    q = PriorityQueue([(0, start)])
    visited = set()
    while len(q) > 0:
        d, v = q.pop()
        if v in visited:
            continue
        visited.add(v)
        for v2, d2 in es[v]:
            d2 = d + d2
            if ans[v2] == -1 or d2 < ans[v2]:
                ans[v2] = d2
                q.add((d2, v2))
    return ans
