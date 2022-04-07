# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/open-the-lock/
752. 打开转盘锁
- 中等
- 推荐
=
- bfs
- 双向bfs
- 启发式搜索A*
"""

from typing import List, Deque, Tuple
from collections import deque


class Solution:
    """bfs"""

    def openLock(self, deadends: List[str], target: str) -> int:
        """使用模板1"""

        ord_9 = ord('9')
        ord_0 = ord('0')
        #
        start = "0000"
        #
        q = deque([start])
        deadends = set(deadends)
        visited = {start}
        #
        step = 0
        #
        while len(q) > 0:
            sz = len(q)
            #
            for i in range(sz):
                node = q.popleft()
                nd = list(node)
                #
                if node in deadends:
                    continue
                if node == target:
                    return step
                del node
                #
                for i in range(4):
                    x = nd[i]
                    ord_x = ord(x)
                    ##
                    nd[i] = ord_x + 1
                    if nd[i] > ord_9:
                        nd[i] -= 10
                    nd[i] = chr(nd[i])
                    #
                    node = "".join(nd)
                    if node not in visited:
                        q.append(node)
                        visited.add(node)
                    ##
                    nd[i] = ord_x - 1
                    if nd[i] < ord_0:
                        nd[i] += 10
                    nd[i] = chr(nd[i])
                    #
                    node = "".join(nd)
                    if node not in visited:
                        q.append(node)
                        visited.add(node)
                    #
                    nd[i] = x
            #
            step += 1
        return -1

    def openLock2(self, deadends: List[str], target: str) -> int:
        """使用模板2"""

        ord_9 = ord('9')
        ord_0 = ord('0')
        #
        start = "0000"
        #
        deadends = set(deadends)
        visited = {start}
        #
        cost = 0
        q = deque([(cost, start)])  # type: Deque[Tuple[int, str]]
        #
        while len(q) > 0:
            cost, node = q.popleft()
            nd = list(node)
            #
            if node in deadends:
                continue
            if node == target:
                return cost
            del node
            cost += 1
            #
            for i in range(4):
                x = nd[i]
                ord_x = ord(x)
                ##
                nd[i] = ord_x + 1
                if nd[i] > ord_9:
                    nd[i] -= 10
                nd[i] = chr(nd[i])
                #
                node = "".join(nd)
                if node not in visited:
                    q.append((cost, node))
                    visited.add(node)
                ##
                nd[i] = ord_x - 1
                if nd[i] < ord_0:
                    nd[i] += 10
                nd[i] = chr(nd[i])
                #
                node = "".join(nd)
                if node not in visited:
                    q.append((cost, node))
                    visited.add(node)
                #
                nd[i] = x
        return -1


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
print(Solution().openLock(deadends, target))
#
deadends = ["0000"]
target = "8888"
print(Solution().openLock(deadends, target))
#
deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
print(Solution().openLock2(deadends, target))
#
deadends = ["0000"]
target = "8888"
print(Solution().openLock2(deadends, target))


class Solution2:
    """双向bfs"""

    def openLock(self, deadends: List[str], target: str) -> int:

        ord_9 = ord('9')
        ord_0 = ord('0')
        #
        start = "0000"
        #
        q = {start}
        q2 = {target}
        deadends = set(deadends)
        visited = {start}
        visited2 = {target}
        #
        step = 0
        #
        while len(q) > 0 and len(q2) > 0:
            q3 = set()
            #
            for node in q:
                nd = list(node)
                #
                if node in deadends:
                    continue
                if node in q2:
                    return step
                del node
                #
                for i in range(4):
                    x = nd[i]
                    ord_x = ord(x)
                    ##
                    nd[i] = ord_x + 1
                    if nd[i] > ord_9:
                        nd[i] -= 10
                    nd[i] = chr(nd[i])
                    #
                    node = "".join(nd)
                    if node not in visited:
                        q3.add(node)
                        visited.add(node)
                    ##
                    nd[i] = ord_x - 1
                    if nd[i] < ord_0:
                        nd[i] += 10
                    nd[i] = chr(nd[i])
                    #
                    node = "".join(nd)
                    if node not in visited:
                        q3.add(node)
                        visited.add(node)
                    #
                    nd[i] = x
            q = q2
            q2 = q3
            visited, visited2 = visited2, visited
            #
            step += 1
        return -1


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
print(Solution2().openLock(deadends, target))
#
deadends = ["0000"]
target = "8888"
print(Solution2().openLock(deadends, target))

#

import heapq


class PriorityQueue:
    def __init__(self, initial_list=None):
        queue = initial_list if initial_list else []
        heapq.heapify(queue)
        #
        self._queue = queue

    def add(self, x):
        queue = self._queue
        heapq.heappush(queue, x)

    def pop(self):
        queue = self._queue
        return heapq.heappop(queue)

    def __len__(self):
        return len(self._queue)


class Solution3:
    """启发式搜索. A*"""

    def openLock(self, deadends: List[str], target: str) -> int:
        ord_ti_memo = [ord(target[i]) for i in range(4)]

        def f(cur: str, target: str, cost: int):
            """启发式函数"""
            f_cost = cost
            for i in range(4):
                ord_ci = ord(cur[i])
                ord_ti = ord_ti_memo[i]
                max_, min_ = max(ord_ci, ord_ti), min(ord_ci, ord_ti)
                f_cost += min(max_ - min_, min_ + 10 - max_)
            return f_cost

        ord_9 = ord('9')
        ord_0 = ord('0')
        #
        start = "0000"
        #
        cost = 0
        f_cost = f(start, target, cost)
        q = PriorityQueue([(f_cost, cost, start)])  # PriorityQueue[Tuple[int, int, str]]
        deadends = set(deadends)
        visited = {start}
        #
        while len(q) > 0:
            _, cost, node = q.pop()
            nd = list(node)
            #
            if node in deadends:
                continue
            if node == target:
                return cost
            del node
            #
            cost += 1
            for i in range(4):
                x = nd[i]
                ord_x = ord(x)
                ##
                nd[i] = ord_x + 1
                if nd[i] > ord_9:
                    nd[i] -= 10
                nd[i] = chr(nd[i])
                #
                node = "".join(nd)
                f_cost = f(node, target, cost)
                if node not in visited:
                    q.add((f_cost, cost, node))
                    visited.add(node)
                ##
                nd[i] = ord_x - 1
                if nd[i] < ord_0:
                    nd[i] += 10
                nd[i] = chr(nd[i])
                #
                node = "".join(nd)
                f_cost = f(node, target, cost)
                if node not in visited:
                    q.add((f_cost, cost, node))
                    visited.add(node)
                #
                nd[i] = x
        return -1


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
print(Solution3().openLock(deadends, target))
#
deadends = ["0000"]
target = "8888"
print(Solution3().openLock(deadends, target))
