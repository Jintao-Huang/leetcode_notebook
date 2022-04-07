# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from template.data_structure.string_hasher import StringHasher


def bifind(lo, sh, s):
    a = lo
    hi = len(s)
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2
        if sh.get_hash(a, mid) == sh.get_hash(0, mid - a):
            lo = mid
        else:
            hi = mid - 1
    return lo - a


class Solution:
    def sumScores(self, s: str) -> int:
        sh = StringHasher(s)
        ans = 0
        for i in reversed(range(len(s))):
            if s[0] != s[i]:
                continue
            ans += bifind(i, sh, s)
        return ans


import random

s = "babab"
print(Solution().sumScores(s))
