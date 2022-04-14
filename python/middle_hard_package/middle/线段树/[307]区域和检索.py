# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from python.template.data_structure.segment_tree import SegmentTree


# 其他解法:
#   分块处理
#   树状数组
class NumArray:
    def __init__(self, nums: List[int]):
        self.t = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.t.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.t.sumRange(left, right)


from python.template.build.call_func import call_func

print(call_func(
    ["NumArray", "sumRange", "sumRange", "sumRange", "update", "update", "update", "sumRange", "update", "sumRange",
     "update"]
    , [[[0, 9, 5, 7, 3]], [4, 4], [2, 4], [3, 3], [4, 5], [1, 7], [0, 8], [1, 2], [1, 9], [4, 4], [3, 4]]
    , globals()))
