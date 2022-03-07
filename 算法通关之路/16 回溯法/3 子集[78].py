# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    def __init__(self):
        self.ans: List[List[int]]

    def _dfs(self, nums: List[int], path: List[int], i: int) -> None:
        self.ans.append(path.copy())
        if i == len(nums):
            return
        for j in range(i, len(nums)):
            path.append(nums[j])
            self._dfs(nums, path, j + 1)
            path.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self._dfs(nums, [], 0)
        return self.ans
