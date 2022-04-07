# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from typing import List


class Solution:
    """回溯. """

    def __init__(self):
        self.ans: List[List[int]]

    def _dfs(self, candidates: List[int], path: List[int], target: int, i: int) -> None:
        # 选择: 选/不选
        if target == 0:
            self.ans.append(path.copy())
            return
        if target < 0 or i >= len(candidates):
            return
        # 选
        x = candidates[i]
        path.append(x)
        self._dfs(candidates, path, target - x, i)
        # 不选
        path.pop()
        self._dfs(candidates, path, target, i + 1)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self._dfs(candidates, [], target, 0)
        return self.ans


candidates = [2, 3, 6, 7]
target = 7
print(Solution().combinationSum(candidates, target))
