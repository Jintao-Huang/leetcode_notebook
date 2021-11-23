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
"""

from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

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
                    node = "".join(nd)
                    #
                    if node not in visited:
                        q.append(node)
                        visited.add(node)
                    #
                    nd[i] = x
            #
            step += 1
        return -1


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
print(Solution().openLock(deadends, target))
#
deadends = ["0000"]
target = "8888"
print(Solution().openLock(deadends, target))


class Solution2:
    """双向bfs"""
    pass
