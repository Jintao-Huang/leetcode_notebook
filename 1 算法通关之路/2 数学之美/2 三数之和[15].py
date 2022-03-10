# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Dict, Tuple


class _Solution:
    """排序+双指针. 错误. [0, 0, 0]. """

    @staticmethod
    def unique(nums: List[int]) -> None:
        """条件: nums有序"""
        j = 1  # 写入指针
        for i in range(1, len(nums)):
            if nums[i] != nums[j - 1]:
                nums[j] = nums[i]
                j += 1
        for i in range(j, len(nums)):
            nums.pop()

    @staticmethod
    def twoSum(nums: List[int], target: int, lo: int, ans: List[List[int]]) -> None:
        hi = len(nums) - 1
        xm = nums[lo]
        while lo < hi:
            x = nums[lo] + nums[hi]
            if x == target:
                ans.append([xm, nums[lo], nums[hi]])
                lo += 1
                hi -= 1
            elif x < target:
                lo += 1
            else:
                hi -= 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.unique(nums)
        ans = []
        #
        for i in range(len(nums)):
            self.twoSum(nums, -nums[i], i, ans)
        return ans


class Solution:
    """排序+双指针. 也可使用哈希表去重. Ot(N^2), Os(排序)"""

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        #
        for i in range(len(nums) - 2):
            # 去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            #
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                x = nums[i] + nums[lo] + nums[hi]
                if x == 0:
                    ans.append([nums[i], nums[lo], nums[hi]])  # 在前在后都行.
                    # 去重
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    #
                    lo += 1
                    hi -= 1
                elif x < 0:
                    lo += 1
                else:
                    hi -= 1

        return ans


# nums = [-1, 0, 1, 2, -1, -4]
nums = [0, 0, 0]
print(Solution().threeSum(nums))
