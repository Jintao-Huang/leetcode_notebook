# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import Dict


class Solution:
    """滑动窗口. Ot(N) Os(1)"""
    def characterReplacement(self, s: str, k: int) -> int:
        lo = 0
        window = {}  # type: Dict[str, int]
        max_n = 0
        for hi in range(len(s)):
            c = s[hi]
            if c not in window:
                window[c] = 0
            window[c] += 1
            max_n = max(max_n, window[c])
            if hi - lo + 1 > k + max_n:
                c2 = s[lo]
                window[c2] -= 1
                lo += 1
        return hi - lo + 1



s = "BAAAB"
k = 2
print(Solution().characterReplacement(s, k))
