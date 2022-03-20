# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from typing import List
from heapq import heapify, heappushpop, heapreplace


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heap = nums[:k].copy()
        if len(heap) < k:
            heap.append(int(-1e8))

        heapify(heap)
        for i in range(k, len(nums)):
            x = nums[i]
            heappushpop(heap, x)
        self.heap = heap

    def add(self, val: int) -> int:
        heap = self.heap
        heappushpop(heap, val)
        return heap[0]
