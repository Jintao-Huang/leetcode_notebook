# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List

"""
1. `(lo + hi) // 2` 在C++中可能溢出
"""


class Solution704:
    """二分查找"""

    def search(self, nums: List[int], target: int) -> int:
        """Ot(LogN) Os(1)"""
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if target > nums[mid]:
                lo = mid + 1
            elif target < nums[mid]:
                hi = mid
            else:
                return mid
        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(Solution704().search(nums, target))


class Solution35:
    """搜索插入位置"""

    def searchInsert(self, nums: List[int], target: int) -> int:
        """Ot(LogN) Os(1)"""
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if target > nums[mid]:
                lo = mid + 1
            elif target < nums[mid]:
                hi = mid
            else:
                return mid
        return lo

    def searchInsert2(self, nums: List[int], target: int) -> int:
        """Ot(LogN) Os(1)"""
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid  # 等于走左
        return lo


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(Solution35().searchInsert2(nums, target))
print(Solution35().searchInsert2(nums, 2))

"""
1. 首和尾可单独判断/立哨兵
2. 循环break/return条件, 后面执行的都一定不满足那个条件
*3. 二分查找夹逼法
"""


class Solution162:
    """寻找峰值"""

    def findPeakElement(self, nums: List[int]) -> int:
        """Ot(N) Os(1)"""
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                return i

    def findPeakElement2(self, nums: List[int]) -> int:
        """简化1. Ot(N) Os(1)"""
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1

    def findPeakElement3(self, nums: List[int]) -> int:
        """二分查找. Ot(LogN) Os(1)"""
        lo, hi = 0, len(nums)
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if nums[mid - 1] < nums[mid]:
                lo = mid  # 含mid
            else:
                hi = mid
        return lo


nums = [1, 2]
print(Solution162().findPeakElement2(nums))
print(Solution162().findPeakElement3(nums))

from typing import Any, Callable


class Solution74:
    """搜索二维矩阵. M * N"""

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """Ot(MN) Os(1)"""
        for m in matrix:
            for x in m:
                if x == target:
                    return True
        else:
            return False

    def bisect_right(self, arr: List[Any], x: Any, *, key: Callable[[Any], Any] = None) -> int:
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if x >= (key(arr[mid]) if key is not None else arr[mid]):
                lo = mid + 1
            else:
                hi = mid
        return lo

    def binary_search(self, arr: List[Any], x: Any) -> bool:
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if x > arr[mid]:
                lo = mid + 1
            elif x < arr[mid]:
                hi = mid
            else:
                return True
        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        """2次二分查找. Ot(LogMN) Os(1)"""
        i = self.bisect_right(matrix, target, key=lambda m: m[0])
        i -= 1
        if i == -1:
            return False
        return self.binary_search(matrix[i], target)

    def binary_search2(self, arr: List[List[int]], x: int) -> bool:
        r, c = len(arr), len(arr[0])
        lo, hi = 0, r * c
        while lo < hi:
            mid = (lo + hi) // 2
            mid0, mid1 = mid // c, mid % c
            if x > arr[mid0][mid1]:
                lo = mid + 1
            elif x < arr[mid0][mid1]:
                hi = mid
            else:
                return True
        return False

    def searchMatrix3(self, matrix: List[List[int]], target: int) -> bool:
        """1次二分查找（索引变换）. Ot(LogMN) Os(1)"""

        return self.binary_search2(matrix, target)


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 80
print(Solution74().searchMatrix(matrix, target))
print(Solution74().searchMatrix2(matrix, target))
print(Solution74().searchMatrix3(matrix, target))
