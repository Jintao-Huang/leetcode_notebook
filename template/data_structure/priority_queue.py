# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
import heapq


class PriorityQueue:
    def __init__(self, nums=None):
        self._queue = nums or []
        heapq.heapify(self._queue)

    def add(self, x):
        heapq.heappush(self._queue, x)

    def pop(self):
        return heapq.heappop(self._queue)

    def __len__(self):
        return len(self._queue)
