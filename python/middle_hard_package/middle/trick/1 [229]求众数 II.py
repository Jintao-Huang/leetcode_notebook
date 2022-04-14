# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List

# Boyer-Moore majority vote algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans1, ans2, n, n2 = 0, 0, 0, 0
        for x in nums:
            if ans1 == x and n > 0:
                n += 1
            elif ans2 == x and n2 > 0:
                n2 += 1
            elif n == 0:
                ans1 = x
                n = 1
            elif n2 == 0:
                ans2 = x
                n2 = 1
            else:
                n -= 1
                n2 -= 1
        cnt1, cnt2 = 0, 0
        for x in nums:
            if x == ans1:
                cnt1 += 1
            elif x == ans2:
                cnt2 += 1
        ans = []
        if cnt1 > len(nums) // 3:
            ans.append(ans1)
        if cnt2 > len(nums) // 3:
            ans.append(ans2)
        return ans


print(Solution().majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))
