# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/minimum-window-substring/
76. 最小覆盖子串
- 困难
- 推荐
=
- 滑动窗口
"""

from collections import defaultdict
from typing import Dict

# test basic function
x = defaultdict(int)
x2 = defaultdict(lambda: 0)
print(x[0], x2[0])  # 0 0
del x, x2


#
class Solution:
    """滑动窗口"""

    def minWindow(self, s: str, t: str) -> str:
        """s: src, t: tgt"""

        need, window = {}, {}  # type: Dict[str, int]  # 计数
        for tc in t:
            if tc not in need:
                need[tc] = 0
                window[tc] = 0
            need[tc] += 1
        #
        valid = 0  # 窗口中满足need条件的 "字符个数"
        # ans = s[start:start + length]
        start = 0
        INT_MAX = 1e9
        length = INT_MAX
        #
        lo, hi = 0, 0
        while hi < len(s):  # [lo, hi]
            sc = s[hi]
            if sc in need:
                window[sc] += 1
                if window[sc] == need[sc]:
                    valid += 1
            hi += 1
            # 满足条件 -> 不满足条件
            while valid == len(need):
                # update ans
                if hi - lo < length:
                    start = lo
                    length = hi - lo
                # 对称
                sc = s[lo]
                if sc in need:
                    if window[sc] == need[sc]:
                        valid -= 1
                    window[sc] -= 1
                #
                lo += 1
        #
        ans = "" if length == INT_MAX else s[start:start + length]
        return ans

    def minWindow2(self, s: str, t: str) -> str:
        """使用 defaultdict()实现"""
        pass


s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s, t))
