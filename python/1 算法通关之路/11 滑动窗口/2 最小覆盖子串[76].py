# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import Dict


class Solution:
    """滑动窗口. Ot(N) Os(1). 其中N=len(s)"""
    def minWindow(self, s: str, t: str) -> str:
        window = {}  # type: Dict[str, int]
        need = {}  # type: Dict[str, int]
        for i in range(len(t)):
            c = t[i]
            if c not in need:
                need[c] = 0
            need[c] += 1

        ans = 0, int(1e8)  # min_lo, min_hi
        lo = 0
        satisfied = 0
        for hi in range(len(s)):
            c = s[hi]
            if c in need:
                if c not in window:
                    window[c] = 0
                window[c] += 1
                if window[c] == need[c]:
                    satisfied += 1
            #
            while satisfied == len(need):
                if hi - lo <= ans[1] - ans[0]:
                    ans = lo, hi
                c2 = s[lo]
                if c2 in need:
                    if window[c2] == need[c2]:
                        satisfied -= 1
                    window[c2] -= 1
                lo += 1
        if ans[1] == int(1e8):
            return ""
        return s[ans[0]:ans[1] + 1]


s = "ADOBECODEBANC"
t = "ABC"

print(Solution().minWindow(s, t))
