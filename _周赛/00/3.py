# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums) == 1 and k % 2 == 1:
            return -1
        ans = -1
        if k > 1:
            ans = max(nums[:k - 1])
        if k <= len(nums) - 1:
            ans = max(ans, nums[k])

        return ans


nums = [91, 98, 17, 79, 15, 55, 47, 86, 4, 5, 17, 79, 68, 60, 60, 31, 72, 85, 25, 77, 8, 78, 40, 96, 76, 69, 95, 2, 42,
        87, 48, 72, 45, 25, 40, 60, 21, 91, 32, 79, 2, 87, 80, 97, 82, 94, 69, 43, 18, 19, 21, 36, 44, 81, 99]
k = 2
print(Solution().maximumTop(nums, k))

nums = [68,76,53,73,85,87,58,24,48,59,38,80,38,65,90,38,45,22,3,28,11]
k = 1
print(Solution().maximumTop(nums, k))

nums = [68]
k = 1
print(Solution().maximumTop(nums, k))
