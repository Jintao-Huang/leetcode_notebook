# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import Set, Dict


class Solution:
    """滑动窗口. Ot(N) Os(min(N, M)). 其中N=len(s), M为字符集大小
    shrink条件: 出现重复字符串
    shrink=False: ans"""

    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()  # type: Set[str]
        ans = 0
        lo = 0

        for hi in range(len(s)):
            c = s[hi]
            while c in window:
                # shrink
                c2 = s[lo]
                window.remove(c2)
                lo += 1
            window.add(c)
            #
            ans = max(ans, hi - lo + 1)
        return ans


class Solution2:
    """滑动窗口. Ot(N) Os(min(N, M)). 其中N=len(s), M为字符集大小
    优化: window存索引.
    shrink条件: 出现重复字符串
    shrink=False: ans"""

    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}  # type: Dict[str, int]  # 值, 索引
        ans = 0
        lo = 0

        for hi in range(len(s)):
            c = s[hi]
            if c in window:
                # shrink
                lo = max(lo, window[c] + 1)
            window[c] = hi
            #
            ans = max(ans, hi - lo + 1)
        return ans


s = "abba"
print(Solution().lengthOfLongestSubstring(s))
print(Solution2().lengthOfLongestSubstring(s))
