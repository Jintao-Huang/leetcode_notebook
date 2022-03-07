# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import Dict


class Solution:
    """滑动窗口. Ot(N) Os(1)"""

    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}  # type: Dict[str, int]
        need = {}  # type: Dict[str, int]
        for i in range(len(s1)):
            c = s1[i]
            if c not in need:
                need[c] = 0
            need[c] += 1

        lo = 0
        satisfied = 0
        for hi in range(len(s2)):
            c = s2[hi]

            if c in need:
                if c not in window:
                    window[c] = 0
                window[c] += 1
                if window[c] == need[c]:
                    satisfied += 1
            #
            while satisfied == len(need):
                if len(s1) == hi - lo + 1:
                    return True
                c2 = s2[lo]
                if c2 in need:
                    if window[c2] == need[c2]:
                        satisfied -= 1
                    window[c2] -= 1
                lo += 1
        return False


class Solution2:
    """滑动窗口2. Ot(N) Os(1)"""

    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}  # type: Dict[str, int]
        need = {}  # type: Dict[str, int]
        for i in range(len(s1)):
            c = s1[i]
            if c not in need:
                need[c] = 0
            need[c] += 1

        satisfied = 0
        for hi in range(len(s2)):
            c = s2[hi]
            if c in need:
                if c not in window:
                    window[c] = 0
                window[c] += 1
                if window[c] == need[c]:
                    satisfied += 1
            #
            lo = hi - len(s1) + 1
            if lo >= 0:
                if satisfied == len(need):
                    return True
                c2 = s2[lo]
                if c2 in need:
                    if window[c2] == need[c2]:
                        satisfied -= 1
                    window[c2] -= 1

        return False


s = "trinitrophenylmethylnitramine"
t = "dinitrophenylhydrazinetrinitrophenylmethylnitramine"

print(Solution().checkInclusion(s, t))
print(Solution2().checkInclusion(s, t))
