# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from sortedcontainers import SortedList


class ExamRoom:
    def _remove_interval(self, itv, remove_sl=True):
        if remove_sl:
            self.sl.remove(itv)
        del self.lo_map_hi[itv[0]]
        del self.hi_map_lo[itv[1]]

    def _add_interval(self, itv):
        self.sl.add(itv)
        self.lo_map_hi[itv[0]] = itv[1]
        self.hi_map_lo[itv[1]] = itv[0]

    def __init__(self, n: int):
        # [lo, hi]
        def key(x):
            if x[0] == 0 or x[1] == n - 1:
                return x[1] - x[0], -x[0]
            else:
                return (x[1] - x[0]) // 2, -x[0]

        self.n = n
        itv = (0, n - 1)
        self.sl = SortedList([], key)  # start, end. 最大的在最后
        self.lo_map_hi = {}
        self.hi_map_lo = {}
        self._add_interval(itv)

    def seat(self) -> int:
        x = self.sl.pop()
        if x[0] == 0:
            self._remove_interval(x, False)
            self._add_interval((x[0] + 1, x[1]))
            return 0
        elif x[1] == self.n - 1:
            self._remove_interval(x, False)
            self._add_interval((x[0], x[1] - 1))
            return self.n - 1
        else:
            mid = (x[0] + x[1]) // 2
            self._remove_interval(x, False)
            if x[0] <= mid - 1:
                self._add_interval((x[0], mid - 1))
            if x[1] >= mid + 1:
                self._add_interval((mid + 1, x[1]))
            return mid

    def leave(self, p: int) -> None:
        lo, hi = p, p
        if p - 1 in self.hi_map_lo:
            lo = self.hi_map_lo[p - 1]
            self._remove_interval((lo, p - 1))

        if p + 1 in self.lo_map_hi:
            hi = self.lo_map_hi[p + 1]
            self._remove_interval((p + 1, hi))
        self._add_interval((lo, hi))


from template.build.call_func import call_func

print(call_func(
    ["ExamRoom", "seat", "seat", "seat", "leave", "leave", "seat", "seat", "seat", "seat", "seat", "seat", "seat",
     "seat", "seat", "leave"],
    [[10], [], [], [], [0], [4], [], [], [], [], [], [], [], [], [], [0]], globals()))
