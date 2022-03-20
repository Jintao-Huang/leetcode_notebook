# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = [0]
        for i in range(len(nums)):
            s.append(s[-1] + nums[i])
        # 两数差
        d = {}
        ans = 0
        for i in range(len(s)):
            x = s[i]
            if x in d:
                ans += d[x]
            x += k
            if x not in d:
                d[x] = 0
            d[x] += 1
        return ans


nums = [1, -1, 0]
k = 0
print(Solution().subarraySum(nums, k))
