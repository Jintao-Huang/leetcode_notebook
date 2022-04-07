# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List

from template.data_structure.priority_queue import PriorityQueue
from sortedcontainers import SortedList


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:

        q = PriorityQueue()
        sl = SortedList(range(k))
        req = [0] * k
        for i in range(len(arrival)):
            t = arrival[i]
            # q -> sl
            while len(q) > 0 and q.peek()[0] <= t:
                _, m = q.pop()
                sl.add(m)
            # sl -> q
            l = load[i]
            if len(sl) > 0:
                i = i % k
                idx = sl.bisect_left(i)
                if idx >= len(sl):
                    idx = sl.bisect_left(0)
                m = sl.pop(idx)
                req[m] += 1
                q.add((t + l, m))
        max_ = max(req)
        ans = []
        for i in range(k):
            if req[i] == max_:
                ans.append(i)

        return ans


k = 3
arrival = [1, 2, 3, 4, 5]
load = [5, 2, 3, 3, 3]

print(Solution().busiestServers(k, arrival, load))


class Solution2:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:

        q = PriorityQueue()
        q2 = PriorityQueue([(i, i) for i in range(k)])
        req = [0] * k
        for i in range(len(arrival)):
            t = arrival[i]
            # q -> sl
            while len(q) > 0 and q.peek()[0] <= t:
                _, m = q.pop()
                q2.add((i + (m - i) % k, m))
            # sl -> q
            l = load[i]
            if len(q2) > 0:
                idx, m = q2.pop()
                req[m] += 1
                q.add((t + l, m))
        max_ = max(req)
        ans = []
        for i in range(k):
            if req[i] == max_:
                ans.append(i)

        return ans


k = 3
arrival = [1, 2, 3, 4, 5]
load = [5, 2, 3, 3, 3]

print(Solution2().busiestServers(k, arrival, load))
