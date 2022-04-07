# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from template.data_structure.priority_queue import PriorityQueue


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        s = sum(nums)
        pq = PriorityQueue(nums, max_heap=True)
        diff = 0
        ans = 0
        while diff * 2 < s:
            x = pq.pop()
            x = x / 2
            pq.add(x)
            diff += x
            ans += 1
        return ans


print(Solution().halveArray([5, 19, 8, 1]))
