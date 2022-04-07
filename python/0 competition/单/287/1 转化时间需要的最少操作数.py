# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from typing import List

# @lru_cache(amount + 3)  # 有少量空余

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        h1, m1 = int(current[:2]), int(current[3:])
        h2, m2 = int(correct[:2]), int(correct[3:])
        m = (h2 - h1) * 60 + m2 - m1

        ans = m // 60
        m %= 60
        ans += m // 15
        m %= 15
        ans += m // 5
        m %= 5
        ans += m
        return ans
