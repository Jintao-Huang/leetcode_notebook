# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


# Boyer-Moore majority vote algorithm
from typing import List


# Boyer-Moore majority vote algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans, n = 0, 0
        for x in nums:
            # ans == x, n > 0
            # ans != x, n > 0
            # n == 0
            if n == 0:
                ans = x
                n = 1
            else:  # n > 0
                if ans == x:
                    n += 1
                else:
                    n -= 1
        return ans
