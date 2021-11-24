# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/permutation-in-string/
567. 字符串的排列
- 中等
- 推荐
- 模板: 滑动窗口
=
- 滑动窗口
"""

from typing import Dict


class Solution:
    """滑动窗口"""

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """s1: tgt, s2: src"""

        need, window = {}, {}  # type: Dict[str, int]  # 计数
        # 初始化
        for tc in s1:
            if tc not in need:
                need[tc] = 0
            need[tc] += 1
        for sc in s2:  # 可用defaultdict
            if sc not in window:
                window[sc] = 0
        #
        valid = 0  # 窗口中 满足/不满足 need条件的 "字符个数"
        #
        lo, hi = 0, 0
        while hi < len(s2):  # [lo, hi]
            sc = s2[hi]
            if sc in need:
                window[sc] += 1
                if window[sc] == need[sc]:
                    valid += 1

            hi += 1
            # debug:
            # print(s2[lo: hi])  # [lo, hi)
            # 满足条件 -> 不满足条件
            while valid == len(need):
                # update ans
                if hi - lo == len(s1):
                    return True
                # 对称
                sc = s2[lo]
                if sc in need:
                    if window[sc] == need[sc]:
                        valid -= 1
                    window[sc] -= 1
                #
                lo += 1
            # debug2:
            # print(s2[lo: hi])  # [lo, hi)
        #
        return False


s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1, s2))
#
s1 = "ab"
s2 = "eidboaoo"
print(Solution().checkInclusion(s1, s2))
