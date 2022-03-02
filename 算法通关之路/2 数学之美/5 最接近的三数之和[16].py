# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from typing import List, Tuple, Dict


class Solution:
    """排序+双指针. 去重. Ot(N^2) Os(排序)"""

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float("inf")
        for i in range(len(nums)):
            # 去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            #
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                x = nums[i] + nums[lo] + nums[hi]
                if x == target:
                    return x
                elif x < target:
                    lo += 1
                else:
                    hi -= 1

                if abs(x - target) < abs(ans - target):
                    ans = x

        return ans


nums = [0, 2, 1, -3]
target = 1
print(Solution().threeSumClosest(nums, target))
