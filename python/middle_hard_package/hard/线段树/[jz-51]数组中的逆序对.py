# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from typing import List

# from python.template.data_structure.sorted_list import SortedList
from python.template.data_structure.segment_tree import SegmentTree


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sl = SortedList()
        n = len(nums)
        ans = 0
        for i in reversed(range(n)):
            x = nums[i]
            ans += sl.bisect_left(x)
            sl.add(x)
        return ans


from python.template.data_structure.rb_tree import SortedList
class Solution5:
    def reversePairs(self, nums: List[int]) -> int:
        sl = SortedList()
        n = len(nums)
        ans = 0
        for i in reversed(range(n)):
            x = nums[i]
            ans += sl.bisect_left(x)
            sl.add(x)
        return ans

from python.template.utils.list import unique


class Solution2:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        # 离散化
        tmp = sorted(nums)
        unique(tmp)
        d = {x: i for i, x in enumerate(tmp)}
        for i in range(n):
            nums[i] = d[nums[i]]
        #
        st = SegmentTree([0] * len(tmp))
        ans = 0
        for i in reversed(range(n)):
            x = nums[i]
            ans += st.sumRange(0, x - 1)
            st.update(x, 1, True)
        return ans


def merge(nums: List[int], lo: int, mid: int, hi: int) -> int:
    """mid: 是两个有序序列的分割点[lo, mid), [mid, hi]. Ot(N) Os(N)"""
    b = nums[lo:mid + 1].copy()
    i, j = 0, mid + 1
    k = lo
    inv = 0
    while i < len(b) and j <= hi:
        if b[i] <= nums[j]:
            nums[k] = b[i]
            i += 1
        else:
            nums[k] = nums[j]
            j += 1
            inv += mid - lo - i + 1
        k += 1
    while i < len(b):
        nums[k] = b[i]
        i += 1
        k += 1
    return inv


class Solution3:
    def merge_sort(self, nums, lo, hi, ans) -> None:
        if lo == hi:
            return
        mid = (lo + hi) // 2
        self.merge_sort(nums, lo, mid, ans)
        self.merge_sort(nums, mid + 1, hi, ans)
        inv = merge(nums, lo, mid, hi)
        ans[0] += inv

    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ans = [0]
        self.merge_sort(nums, 0, len(nums) - 1, ans)
        return ans[0]

from python.template.data_structure.binary_indexed_tree import BinaryIndexedTree
class Solution4:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        # 离散化
        tmp = sorted(nums)
        unique(tmp)
        d = {x: i for i, x in enumerate(tmp)}
        for i in range(n):
            nums[i] = d[nums[i]]
        #
        st = BinaryIndexedTree([0] * len(tmp))
        ans = 0
        for i in reversed(range(n)):
            x = nums[i]
            ans += st.prefix_sum(x - 1)
            st.update(x, 1)
        return ans

print(Solution().reversePairs([7, 5, 6, 4]))
print(Solution2().reversePairs([7, 5, 6, 4]))
print(Solution3().reversePairs([7, 5, 6, 4]))
print(Solution4().reversePairs([7, 5, 6, 4]))
print(Solution5().reversePairs([7, 5, 6, 4]))
