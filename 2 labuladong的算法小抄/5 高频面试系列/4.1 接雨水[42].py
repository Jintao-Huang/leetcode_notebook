# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n  # 最高
        right = [0] * n
        left[0] = height[0]
        right[n - 1] = height[n - 1]
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
        for i in reversed(range(0, n - 1)):
            right[i] = max(right[i + 1], height[i])
        ans = 0
        for i in range(n):
            ans += min(left[i], right[i]) - height[i]
        return ans


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(height))
