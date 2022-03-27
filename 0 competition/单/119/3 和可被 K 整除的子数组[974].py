# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """前缀和+哈希表"""

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        s = [0]
        for x in nums:
            s.append(s[-1] + x)
        d = {}
        ans = 0
        for x in s:
            x %= k
            if x not in d:
                d[x] = 0
            ans += d[x]
            d[x] += 1
        return ans


nums = [4, 5, 0, -2, -3, 1]
k = 5

print(Solution().subarraysDivByK(nums, k))
