# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        ans = []  # type: List[int]
        for i in range(len(nums)):
            ans.append(nums[(i - k) % len(nums)])
        nums[:] = ans


class Solution2:
    @staticmethod
    def reverse(nums: List[int], lo: int, hi: int) -> None:
        # [lo, hi]
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - k - 1)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution().rotate(nums, k)
print(nums)
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution2().rotate(nums, k)
print(nums)