# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List
from python.template.data_structure.priority_queue import PriorityQueue

import heapq

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = int(1e9) + 7
        heapq.heapify(nums)
        for i in range(k):
            heapq.heapreplace(nums, nums[0] +1)
        ans = 1

        for i in range(len(nums)):
            ans *= nums[i]
            ans %= MOD
        return ans


print(Solution().maximumProduct([0, 4], 5))
print(Solution().maximumProduct([6, 3, 3, 2], 2))

