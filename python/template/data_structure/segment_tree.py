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
    def __init__(self, nums, is_diff=False):
        self.n = len(nums)
        self.is_diff = is_diff
        h = int(ceil(log2(self.n) + 1))
        nn = 2 ** h - 1
        self.tree = [None] * nn  # type: List[int]
        self.lazy_tag = [None] * nn
        # build tree
        self._build_tree(nums, 0, self.n - 1, 0)

    def _build_tree(self, nums, lo, hi, i) -> int:
        if lo == hi:
            self.tree[i] = nums[lo]
        else:
            mid = (lo + hi) // 2
            x1 = self._build_tree(nums, lo, mid, 2 * i + 1)
            x2 = self._build_tree(nums, mid + 1, hi, 2 * i + 2)
            self.tree[i] = x1 + x2
        return self.tree[i]

    def _dfs_sum(self, lo, hi, lo2, hi2, i) -> int:
        # find [lo2, hi2] in [lo, hi]. 返回sumRange.
        if lo == lo2 and hi == hi2:
            return self.tree[i]
        # lo < hi
        mid = (lo + hi) // 2
        cl, cr = 2 * i + 1, 2 * i + 2
        if self.lazy_tag[i] is not None:
            self.lazy_tag[cl] = self.lazy_tag[i]
            self.lazy_tag[cr] = self.lazy_tag[i]
            if self.is_diff:
                diff = self.lazy_tag[i]
                self.tree[cl] += (mid - lo + 1) * diff
                self.tree[cr] += (hi - mid) * diff
            else:
                v = self.lazy_tag[i]
                self.tree[cl] = (mid - lo + 1) * v
                self.tree[cr] = (hi - mid) * v
            self.lazy_tag[i] = None
        s = 0
        if lo2 <= mid:
            s += self._dfs_sum(lo, mid, lo2, min(mid, hi2), 2 * i + 1)
        if hi2 >= mid + 1:
            s += self._dfs_sum(mid + 1, hi, max(mid + 1, lo2), hi2, 2 * i + 2)
        return s

    def sumRange(self, lo, hi):
        # [lo, hi]
        if lo > hi:
            return 0
        return self._dfs_sum(0, self.n - 1, lo, hi, 0)

    def _dfs_update(self, lo, hi, lo2, hi2, value, i) -> None:
        # 返回diff
        if lo == lo2 and hi == hi2:
            self.lazy_tag[i] = value
            if self.is_diff:
                diff = value
                self.tree[i] += diff * (hi - lo + 1)
            else:
                self.tree[i] = value * (hi - lo + 1)
            return
        # lo < hi
        mid = (lo + hi) // 2
        cl, cr = 2 * i + 1, 2 * i + 2
        if self.lazy_tag[i] is not None:
            self.lazy_tag[cl] = self.lazy_tag[i]
            self.lazy_tag[cr] = self.lazy_tag[i]
            if self.is_diff:
                diff = self.lazy_tag[i]
                self.tree[cl] += (mid - lo + 1) * diff
                self.tree[cr] += (hi - mid) * diff
            else:
                v = self.lazy_tag[i]
                self.tree[cl] = (mid - lo + 1) * v
                self.tree[cr] = (hi - mid) * v
            self.lazy_tag[i] = None
        if lo2 <= mid:
            self._dfs_update(lo, mid, lo2, min(mid, hi2), value, 2 * i + 1)
        if hi2 >= mid + 1:
            self._dfs_update(mid + 1, hi, max(mid + 1, lo2), hi2, value, 2 * i + 2)
        self.tree[i] = self.tree[2 * i + 1] + self.tree[2 * i + 2]

    def update(self, lo, hi, value):
        self._dfs_update(0, self.n - 1, lo, hi, value, 0)


if __name__ == '__main__':
    x = [0, 1, 2, 3, 4, 5, 6]
    t = SegmentTree(x, is_diff=True)
    print(t.tree, t.lazy_tag)
    print(t.update(0, 6, -100))
    print(t.tree, t.lazy_tag)

    print(t.sumRange(0, 6))
    print(t.sumRange(0, 1))
    print(t.sumRange(0, 0))
