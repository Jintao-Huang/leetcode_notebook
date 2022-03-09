# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:


from typing import Dict


class Solution:
    """滑动窗口. Ot(N) Os(1)"""

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        ans = {}  # type: Dict[str, int]
        window = {}
        lo = 0
        for hi in range(len(s)):
            c = s[hi]
            if c not in window:
                window[c] = 0
            window[c] += 1

            #
            while len(window) > maxLetters or hi - lo + 1 > minSize:
                c2 = s[lo]
                window[c2] -= 1
                if window[c2] == 0:
                    window.pop(c2)
                lo += 1

            if hi - lo + 1 == minSize:
                s2 = s[lo: hi + 1]
                if s2 not in ans:
                    ans[s2] = 0
                ans[s2] += 1

        if len(ans) == 0:
            return 0
        return max(ans.values())


s = "aababcaab"
maxLetters = 2
minSize = 3
maxSize = 4

print(Solution().maxFreq(s, maxLetters, minSize, maxSize))
