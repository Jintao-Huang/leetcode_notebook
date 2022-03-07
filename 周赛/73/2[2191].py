# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """数学"""
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        a = []
        for i in range(len(nums)):
            x = nums[i]
            x2 = 0
            i = 0
            if x == 0:
                a.append(mapping[x])
            else:
                while x > 0:
                    x2 += mapping[x % 10] * 10 ** i
                    x //= 10
                    i += 1
                a.append(x2)
        a = list(zip(nums, a))
        a.sort(key=lambda item: item[1])
        return [x[0] for x in a]


mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
nums = [991, 338, 38]
print(Solution().sortJumbled(mapping, nums))
mapping = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums = [789, 456, 123]
print(Solution().sortJumbled(mapping, nums))
mapping =[9,8,7,6,5,4,3,2,1,0]
nums =[0,1,2,3,4,5,6,7,8,9]
print(Solution().sortJumbled(mapping, nums))