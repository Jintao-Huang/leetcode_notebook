# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Tuple

"""
1. [)包含2个mid; 不包含1个mid+1
"""


class Solution169:
    """多数元素"""

    def majorityElement(self, nums: List[int]) -> int:
        """哈希表. Ot(N) Os(N)"""
        d = {}
        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        # for k, v in d.items():
        #     if v > len(nums) // 2:
        #         return k
        return max(d.items(), key=lambda x: x[1])[0]

    def majorityElement2(self, nums: List[int]) -> int:
        """排序. Ot(NLogN) Os(N)"""
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement3(self, nums: List[int]) -> int:
        """分治法. Ot(NLogN) Os(LogN)"""

        def _majorityElement3(_nums: List[int], lo: int, hi: int) -> int:
            if hi - lo < 2:
                return _nums[lo]
            mid = (lo + hi) // 2
            n1 = _majorityElement3(_nums, lo, mid)
            n2 = _majorityElement3(_nums, mid, hi)
            if n1 == n2:
                return n1
            else:
                count1 = 0
                count2 = 0
                for i in range(lo, hi):
                    if _nums[i] == n1:
                        count1 += 1
                    elif _nums[i] == n2:
                        count2 += 1
                return n1 if count1 >= count2 else n2

        return _majorityElement3(nums, 0, len(nums))


n = [2, 2, 1, 1, 1, 2, 2]
n = [3, 3, 4]
print(Solution169().majorityElement(n))
print(Solution169().majorityElement2(n))
print(Solution169().majorityElement3(n))

"""
1. max_sum、min初始化时，等取第一个
"""


class Solution53:
    """最大子序和"""

    def maxSubArray(self, nums: List[int]) -> int:
        """动态规划. Ot(N) Os(1)"""
        # 以i结尾的最大子序列和
        prev_s = nums[0]
        max_sum = prev_s
        for i in range(1, len(nums)):
            prev_s = max(prev_s + nums[i], nums[i])
            max_sum = max(prev_s, max_sum)
        return max_sum

    def maxSubArray2(self, nums: List[int]) -> int:
        """分治法. Ot(N) Os(LogN)"""
        Status = Tuple[int, int, int, int]

        # left_sum, right_sum, max_sum, i_sum
        def push_up(status_l: Status, status_r: Status) -> Status:
            return (
                max(status_l[0], status_l[3] + status_r[0]),  # 必须以左端点
                max(status_r[1], status_r[3] + status_l[1]),  # 必须以右端点结束
                max([status_l[2], status_r[2], status_l[1] + status_r[0]]),  # 最大
                status_l[3] + status_r[3],  # 区间和
            )

        def _maxSubArray2(_nums: List[int], lo: int, hi: int) -> Status:
            """T(N) = 2T(N/2) + O(1). Ot(N) Os(LogN)"""
            if hi - lo < 2:
                return _nums[lo], _nums[lo], _nums[lo], _nums[lo]
            mid = (lo + hi) // 2  # >> 1
            status_l = _maxSubArray2(_nums, lo, mid)
            status_r = _maxSubArray2(_nums, mid, hi)
            return push_up(status_l, status_r)  # O(1)

        return _maxSubArray2(nums, 0, len(nums))[2]


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution53().maxSubArray(nums))
print(Solution53().maxSubArray2(nums))
