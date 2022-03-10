# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """双指针-头尾. Ot(N) Os(1)"""

    def maxArea(self, height: List[int]) -> int:
        lo, hi = 0, len(height) - 1
        ans = 0
        while lo < hi:
            area = (hi - lo) * min(height[lo], height[hi])
            ans = max(ans, area)
            if height[lo] > height[hi]:
                hi -= 1
            else:
                lo += 1
        return ans
