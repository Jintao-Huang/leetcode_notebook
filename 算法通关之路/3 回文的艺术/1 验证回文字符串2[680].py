# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import Tuple


class Solution:
    """双指针. Ot(N) Os(1)"""
    def valid(self, s: str, lo: int, hi: int) -> Tuple[bool, int, int]:
        while lo < hi:
            if s[lo] != s[hi]:
                return False, lo, hi
            lo += 1
            hi -= 1
        return True, lo, hi

    def validPalindrome(self, s: str) -> bool:
        flag, lo, hi = self.valid(s, 0, len(s) - 1)
        if flag:
            return True
        v1 = self.valid(s, lo + 1, hi)
        v2 = self.valid(s, lo, hi - 1)
        return v1[0] or v2[0]


print(Solution().validPalindrome("abca"))
