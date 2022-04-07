# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Tuple
from math import log2, ceil


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        h = int(ceil(log2(self.n) + 1))
        self.tree = [None] * (2 ** h - 1)  # type: List[Tuple[int, int, int, str, str]]  # L, A, R, LC, RC
        # build tree
        self._build_tree(arr, 0, self.n - 1, 0)

    def _build_tree(self, arr, lo, hi, i) -> Tuple[int, int, int, str, str]:
        if lo == hi:
            self.tree[i] = 1, 1, 1, arr[lo], arr[lo]
        else:
            mid = (lo + hi) // 2
            l, a, r, lc, rc = self._build_tree(arr, lo, mid, 2 * i + 1)
            l2, a2, r2, lc2, rc2 = self._build_tree(arr, mid + 1, hi, 2 * i + 2)
            if rc == lc2:
                self.tree[i] = (
                    l + l2 if l == (mid + 1 - lo) else l,
                    max(r + l2, a, a2),
                    r2 + r if r2 == (hi - mid) else r2,
                    lc, rc2
                )
            else:
                self.tree[i] = (
                    l, max(a, a2), r2, lc, rc2
                )
        return self.tree[i]

    def _dfs(self, lo, hi, lo2, hi2, i) -> int:
        if lo == lo2 and hi == hi2:
            return self.tree[i][1]
        mid = (lo + hi) // 2
        x = 0
        if lo2 <= mid:
            x1 = self._dfs(lo, mid, lo2, min(mid, hi2), 2 * i + 1)
            x = max(x, x1)
        if hi2 >= mid + 1:
            x2 = self._dfs(mid + 1, hi, max(mid + 1, lo2), hi2, 2 * i + 2)
            x = max(x, x2)
        return x

    def query(self, lo, hi=None):
        # [lo, hi]
        if hi is None:
            hi = self.n - 1
        return self._dfs(0, self.n - 1, lo, hi, 0)

    def _dfs2(self, lo, hi, idx, value, i) -> Tuple[int, int, int, str, str]:
        if lo == hi:
            self.tree[i] = (1, 1, 1, value, value)
        else:
            mid = (lo + hi) // 2
            if idx <= mid:
                l, a, r, lc, rc = self._dfs2(lo, mid, idx, value, 2 * i + 1)
                l2, a2, r2, lc2, rc2 = self.tree[2 * i + 2]
            else:
                l, a, r, lc, rc = self.tree[2 * i + 1]
                l2, a2, r2, lc2, rc2 = self._dfs2(mid + 1, hi, idx, value, 2 * i + 2)
            if rc == lc2:
                self.tree[i] = (
                    l + l2 if l == (mid + 1 - lo) else l,
                    max(r + l2, a, a2),
                    r2 + r if r2 == (hi - mid) else r2,
                    lc, rc2
                )
            else:
                self.tree[i] = (
                    l, max(a, a2), r2, lc, rc2
                )
        return self.tree[i]

    def update(self, idx, value):
        self._dfs2(0, self.n - 1, idx, value, 0)


# union_find能连接, 但不能断开.
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        t = SegmentTree(s)
        ans = []
        for i in range(len(queryIndices)):
            c, idx = queryCharacters[i], queryIndices[i]
            t.update(idx, c)
            ans.append(t.query(0))
        return ans


s = "babacc"
queryCharacters = "bcb"
queryIndices = [1, 3, 3]
print(Solution().longestRepeating(s, queryCharacters, queryIndices))
