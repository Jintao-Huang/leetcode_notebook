# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Set


class Solution:
    def __init__(self):
        self.ans: List[List[int]]

    def _dfs(self, nums: Set[int], path: List[int]) -> None:
        if len(nums) == 0:
            self.ans.append(path.copy())
            return
        for x in list(nums):
            nums.remove(x)
            path.append(x)
            self._dfs(nums, path)
            nums.add(x)
            path.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self._dfs(set(nums), [])
        return self.ans


class Solution2:
    def __init__(self):
        self.ans: List[List[int]]

    def _dfs(self, nums: List[int], path: List[int], visited: Set[int]) -> None:
        # visited存索引
        if len(path) == len(nums):
            self.ans.append(path.copy())
            return
        for i in range(len(nums)):
            if i in visited:
                continue
            x = nums[i]
            visited.add(i)
            path.append(x)
            self._dfs(nums, path, visited)
            path.pop()
            visited.remove(i)

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self._dfs(nums, [], set())
        return self.ans


nums = [1, 2, 3]
print(Solution().permute(nums))
print(Solution2().permute(nums))
