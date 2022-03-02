# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from typing import List, Dict, Tuple


class Solution:
    """排序+双指针. Ot(NlogN) Os(排序)"""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = list(zip(nums, range(len(nums))))  # type: List[Tuple[int, int]]  # 值, 索引
        nums.sort()
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            x = nums[lo][0] + nums[hi][0]
            if x == target:
                return [nums[lo][1], nums[hi][1]]
            elif x < target:
                lo += 1
            else:
                hi -= 1


print(Solution().twoSum([3, 2, 4], 6))


class Solution2:
    """哈希表. Ot(N) Os(N)"""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}  # type: Dict[int, int]  # 值: 索引
        for i in range(len(nums)):
            if nums[i] not in d:
                d[target - nums[i]] = i
            else:
                return [d[nums[i]], i]


print(Solution2().twoSum([3, 2, 4], 6))
