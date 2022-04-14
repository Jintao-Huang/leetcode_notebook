# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from python.template.data_structure.segment_tree import SegmentTree


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        min_, max_ = min(nums), max(nums)
        n = max_ - min_ + 1
        arr = [0] * n
        st = SegmentTree(arr)
        ans = [0] * len(nums)
        for i in reversed(range(len(nums))):
            x = nums[i]
            ans[i] = st.sumRange(0, x - min_ - 1)
            st.update(x - min_, 1, True)
        return ans


from python.template.data_structure.sorted_list import SortedList


class Solution2:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sl = SortedList()
        ans = [0] * len(nums)
        for i in reversed(range(len(nums))):
            x = nums[i]
            idx = sl.bisect_left(x)
            ans[i] = idx
            sl.add(x)
        return ans


print(Solution().countSmaller([5, 2, 6, 1]))
