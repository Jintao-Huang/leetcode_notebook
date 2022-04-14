# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from bisect import bisect_right, insort_right, bisect_left
from typing import List


class SortedList:
    # 或进行分块处理.
    def __init__(self, nums=None):
        if nums is None:
            nums = []
        self.sl = nums  # type: List[int]
        self.sl.sort()

    def add(self, x: int):
        insort_right(self.sl, x)

    def remove(self, x):
        idx = bisect_right(self.sl, x) - 1
        if self.sl[idx] != x:
            raise ValueError("x not find")
        self.sl.pop(idx)

    def bisect_left(self, x) -> int:
        return bisect_left(self.sl, x)

    def bisect_right(self, x) -> int:
        return bisect_right(self.sl, x)

    def __len__(self):
        return len(self.sl)

    def __getitem__(self, i):
        return self.sl[i]

    def __str__(self):
        return str(self.sl)

    def copy(self):
        x = SortedList()
        x.sl = self.sl
        return x

    def pop(self, idx: int):
        return self.sl.pop(idx)

    def _insert(self, idx: int, x):
        return self.sl.insert(idx, x)
