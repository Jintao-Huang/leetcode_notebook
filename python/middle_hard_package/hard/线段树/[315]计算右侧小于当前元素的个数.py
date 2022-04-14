# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from python.template.data_structure.segment_tree import SegmentTree
from python.template.utils.list import unique


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # 离散化
        tmp = sorted(nums)
        unique(tmp)
        d = {x: i for i, x in enumerate(tmp)}
        for i in range(n):
            nums[i] = d[nums[i]]
        #
        st = SegmentTree([0] * len(tmp))
        ans = [0] * n
        for i in reversed(range(n)):
            x = nums[i]
            ans[i] = st.sumRange(0, x - 1)
            st.update(x, 1, True)
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
print(Solution2().countSmaller([5, 2, 6, 1]))
