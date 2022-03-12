# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """一次二分搜索. Ot(LogMN) Os(1)"""

    @staticmethod
    def _lower_bound(matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            x = matrix[mid // n][mid % n]
            if x == target:
                return True
            elif x > target:
                hi = mid - 1
            else:
                lo = mid + 1
        x = matrix[lo // n][lo % n]
        return x == target

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self._lower_bound(matrix, target)


class Solution2:
    """两次二分搜索. Ot(LogMN) Os(1)"""

    @staticmethod
    def _lower_bound_c(matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        lo, hi = 0, m
        while lo < hi:
            mid = lo + (hi - lo) // 2
            x = matrix[mid][0]
            if x >= target:
                hi = mid
            else:
                lo = mid + 1
        return lo

    @staticmethod
    def binary_search(nums: List[int], target: int) -> bool:
        """Ot(LogN) Os(1)"""
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2  # 偶数时: 中点偏左
            if target == nums[mid]:
                return True
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return target == nums[lo]

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = self._lower_bound_c(matrix, target + 1) - 1
        return self.binary_search(matrix[i], target)


matrix = [[1], [3]]
target = 1

print(Solution().searchMatrix(matrix, target))
print(Solution2().searchMatrix(matrix, target))
