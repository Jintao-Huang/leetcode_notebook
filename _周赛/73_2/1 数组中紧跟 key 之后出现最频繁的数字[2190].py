# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """哈希表"""

    def mostFrequent(self, nums: List[int], key: int) -> int:
        d = {}
        for i in range(len(nums) - 1):
            x = nums[i]
            if x == key:
                x2 = nums[i + 1]
                if x2 not in d:
                    d[x2] = 0
                d[x2] += 1
        return max(d, key=lambda x: d[x])


nums = [2, 2, 2, 2, 3]
key = 2
print(Solution().mostFrequent(nums, key))
