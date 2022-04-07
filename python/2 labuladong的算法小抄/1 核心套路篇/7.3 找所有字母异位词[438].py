# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # shrink: 长度==len(p)时
        need = {}
        for c in p:
            if c not in need:
                need[c] = 0
            need[c] += 1

        window = {}
        valid = 0
        lo = 0
        ans = []
        for hi in range(len(s)):
            c = s[hi]
            if c in need:
                if c not in window:
                    window[c] = 0
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            if hi - lo + 1 == len(p):
                if valid == len(need):
                    ans.append(lo)
                c2 = s[lo]
                if c2 in need:
                    if window[c2] == need[c2]:
                        valid -= 1
                    window[c2] -= 1
                lo += 1
        return ans
