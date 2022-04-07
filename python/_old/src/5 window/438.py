# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/
438. 找到字符串中所有字母异位词
- 中等
=
- 滑动窗口
"""

from typing import List, Dict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """s: src, p: tgt"""

        need, window = {}, {}  # type: Dict[str, int]  # 计数
        # 初始化
        for tc in p:
            if tc not in need:
                need[tc] = 0
            need[tc] += 1
        for sc in s:  # 可用defaultdict
            if sc not in window:
                window[sc] = 0
        #
        valid = 0  # 窗口中 满足/不满足 need条件的 "字符个数"
        ans = []
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
                if hi - lo == len(p):
                    ans.append(lo)
                # 对称
                sc = s[lo]
                if sc in need:
                    if window[sc] == need[sc]:
                        valid -= 1
                    window[sc] -= 1
                #
                lo += 1
        #
        return ans


s = "cbaebabacd"
p = "abc"
print(Solution().findAnagrams(s, p))
