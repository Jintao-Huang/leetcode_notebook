# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        s = []
        for i in range(len(nums)):
            x = nums[i]
            if x == key:
                s.append(i)
        ans = []
        j = 0
        for i in range(len(nums)):
            if j >= len(s):
                break
            x = s[j]
            if abs(x - i) <= k:
                ans.append(i)
            if i - x == k:
                j += 1
        return ans
nums = [3,4,9,1,3,9,5]
key = 9
k = 1
print(Solution().findKDistantIndices(nums, key, k))
nums = [2,2,2,2,2]
key = 2
k = 2
print(Solution().findKDistantIndices(nums, key, k))
