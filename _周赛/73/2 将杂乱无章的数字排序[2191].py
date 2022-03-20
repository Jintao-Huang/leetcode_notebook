# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """数学"""

    @staticmethod
    def transfer(mapping: List[int], x: int):
        # 可用其他方法.
        return int("".join([str(mapping[int(c)]) for c in str(x)]))

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        nums2 = [(self.transfer(mapping, x), x) for x in nums]
        nums2.sort(key=lambda x: x[0])
        return [x[1] for x in nums2]


mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
nums = [991, 338, 38]
print(Solution().sortJumbled(mapping, nums))
mapping = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums = [789, 456, 123]
print(Solution().sortJumbled(mapping, nums))
mapping = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(Solution().sortJumbled(mapping, nums))
