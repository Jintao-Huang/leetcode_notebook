# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Dict, Tuple, Set


class Solution:
    """排序+双指针. 用哈希表去重. """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 去重
        ans = set()  # type: Set[Tuple[int, int, int, int]]
        #
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                lo, hi = j + 1, len(nums) - 1
                while lo < hi:
                    x = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if x == target:
                        ans.add((nums[i], nums[j], nums[lo], nums[hi]))
                        lo += 1
                        hi -= 1
                    elif x < target:
                        lo += 1
                    else:
                        hi -= 1
        return [list(a) for a in ans]


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(Solution().fourSum(nums, target))
