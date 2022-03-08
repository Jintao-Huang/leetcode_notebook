# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """回溯"""
    def __init__(self):
        self.ans: List[List[int]]

    def _dfs(self, nums: List[int], path: List[int], i: int) -> None:
        # 选择: 选/不选
        if i >= len(nums):
            self.ans.append(path.copy())
            return

        x = nums[i]
        path.append(x)
        self._dfs(nums, path, i + 1)
        path.pop()
        self._dfs(nums, path, i + 1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self._dfs(nums, [], 0)
        return self.ans


print(Solution().subsets([1, 2, 3]))
