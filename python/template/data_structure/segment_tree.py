# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from math import ceil, log2
from typing import List


# 区间树和线段树不同
#   区间树: 判断一个点是否属于某个区间
#   线段树: 求某段区间的和

class SegmentTree:
    # 也可以写成指针树形式.
    def __init__(self, nums):
        self.n = len(nums)
        h = int(ceil(log2(self.n) + 1))
        self.tree = [None] * (2 ** h - 1)  # type: List[int]
        # build tree
        self._build_tree(nums, 0, self.n - 1, 0)

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
        s = 0
        if lo2 <= mid:
            s += self._dfs(lo, mid, lo2, min(mid, hi2), 2 * i + 1)
        if hi2 >= mid + 1:
            s += self._dfs(mid + 1, hi, max(mid + 1, lo2), hi2, 2 * i + 2)
        return s

    def sumRange(self, lo, hi):
        # [lo, hi]
        if lo > hi:
            return 0
        return self._dfs(0, self.n - 1, lo, hi, 0)

    def _dfs2(self, lo, hi, idx, value, i, is_diff) -> int:
        # 返回diff
        if lo == hi:
            if is_diff:
                diff = value
            else:
                diff = value - self.tree[i]
        else:
            mid = (lo + hi) // 2
            if idx <= mid:
                diff = self._dfs2(lo, mid, idx, value, 2 * i + 1, is_diff)
            else:
                diff = self._dfs2(mid + 1, hi, idx, value, 2 * i + 2, is_diff)
        self.tree[i] += diff
        return diff

    def update(self, idx, value, is_diff=False):
        self._dfs2(0, self.n - 1, idx, value, 0, is_diff)


if __name__ == '__main__':
    x = [0, 1, 2, 3, 4, 5, 6]
    t = SegmentTree(x)
    print(t.sumRange(0, 6))
    print(t.update(0, -100))
    print(t.sumRange(0, 6))
    print(t.sumRange(0, 1))
    print(t.sumRange(0, 0))
    """
    21
    None
    -79
    -99
    -100
    """
