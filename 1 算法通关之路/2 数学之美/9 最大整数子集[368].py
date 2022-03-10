# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Dict, Set


class Solution:
    """类似于动态规划. Ot(N^2) Os(N^2)"""
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        ans = []  # type: List[Set[int]]
        nums.sort()
        for i in range(len(nums)):
            temp = []  # type: List[Set[int]]  # 索引
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    temp.append(ans[j])
            if len(temp) > 0:
                m = max(temp, key=len).copy()
            else:
                m = set()
            m.add(nums[i])
            ans.append(m)
        #
        return list(max(ans, key=len))


print(Solution().largestDivisibleSubset([1,2,3]))
