# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
import heapq

heappop_max = heapq._heappop_max
heapreplace_max = heapq._heapreplace_max
heapify_max = heapq._heapify_max


def heappush_max(heap, x):
    heap.append(x)
    heapq._siftdown_max(heap, 0, len(heap) - 1)


def heappushpop(heap, item):
    if heap and heap[0] < item:
        item, heap[0] = heap[0], item
        heapq._siftup_max(heap, 0)
    return item


class PriorityQueue:
    def __init__(self, nums=None, max_heap=False):
        self._queue = nums or []
        if max_heap:
            self._heapify = heapify_max
            self._heappush = heappush_max
            self._heappop = heappop_max
        else:
            self._heapify = heapq.heapify
            self._heappush = heapq.heappush
            self._heappop = heapq.heappop

        self._heapify(self._queue)

    def add(self, x):
        self._heappush(self._queue, x)

    def pop(self):
        return self._heappop(self._queue)

    def peek(self):
        return self._queue[0]

    def __len__(self):
        return len(self._queue)
