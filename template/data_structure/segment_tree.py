# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from math import ceil, log2
from typing import List


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        h = int(ceil(log2(self.n) + 1))
        self.tree = [None] * (2 ** h - 1)  # type: List[int]
        # build tree
        self._build_tree(arr, 0, self.n - 1, 0)

    def _build_tree(self, arr, lo, hi, i) -> int:
        if lo == hi:
            self.tree[i] = arr[lo]
        else:
            mid = (lo + hi) // 2
            x1 = self._build_tree(arr, lo, mid, 2 * i + 1)
            x2 = self._build_tree(arr, mid + 1, hi, 2 * i + 2)
            self.tree[i] = x1 + x2
        return self.tree[i]

    def _dfs(self, lo, hi, lo2, hi2, i) -> int:
        if lo == lo2 and hi == hi2:
            return self.tree[i]
        mid = (lo + hi) // 2
        x = 0
        if lo2 <= mid:
            x += self._dfs(lo, mid, lo2, min(mid, hi2), 2 * i + 1)
        if hi2 >= mid + 1:
            x += self._dfs(mid + 1, hi, max(mid + 1, lo2), hi2, 2 * i + 2)
        return x

    def query(self, lo, hi):
        # [lo, hi]
        return self._dfs(0, self.n - 1, lo, hi, 0)

    def _dfs2(self, lo, hi, idx, value, i) -> int:
        # 返回diff
        if lo == hi:
            diff = value - self.tree[i]
        else:
            mid = (lo + hi) // 2
            if idx <= mid:
                diff = self._dfs2(lo, mid, idx, value, 2 * i + 1)
            else:
                diff = self._dfs2(mid + 1, hi, idx, value, 2 * i + 2)
        self.tree[i] += diff
        return diff

    def update(self, idx, value):
        self._dfs2(0, self.n - 1, idx, value, 0)


if __name__ == '__main__':
    x = [0, 1, 2, 3, 4, 5, 6]
    t = SegmentTree(x)
    print(t.query(0, 6))
    print(t.update(0, -100))
    print(t.query(0, 6))
    print(t.query(0, 1))
    print(t.query(0, 0))
    """
    21
    None
    -79
    -99
    -100
    """
