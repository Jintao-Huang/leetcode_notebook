# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_arr = [int(1e8)]
        for i in range(len(prices) - 1):
            min_arr.append(min(min_arr[-1], prices[i]))

        ans = 0  # 卖出
        for i in range(1, len(prices)):
            ans = max(ans, prices[i] - min_arr[i])
        return ans


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))


class Solution2:
    """状态压缩"""

    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_ = prices[0]
        for i in range(1, len(prices)):
            ans = max(ans, prices[i] - min_)
            min_ = min(min_, prices[i])
        return ans


print(Solution2().maxProfit([7, 1, 5, 3, 6, 4]))
