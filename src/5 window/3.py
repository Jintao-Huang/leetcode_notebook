# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
3. 无重复字符的最长子串
- 中等
- 推荐
=
- 滑动窗口
"""

from typing import List, Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        window = {}  # type: Dict[str, int]  # 计数
        # 初始化
        for sc in s:  # 可用defaultdict
            if sc not in window:
                window[sc] = 0
        #
        ans = 0
        #
        lo, hi = 0, 0
        while hi < len(s):  # [lo, hi]
            s_hi = s[hi]
            window[s_hi] += 1
            hi += 1
            # 不满足条件 -> 满足条件
            while window[s_hi] > 1:
                # 对称
                s_lo = s[lo]
                window[s_lo] -= 1
                #
                lo += 1
            # update ans
            ans = max(ans, hi - lo)
        #
        return ans


s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
