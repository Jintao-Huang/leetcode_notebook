# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from typing import List, Set, Dict


class Solution:
    """回溯"""

    def __init__(self):
        self.ans: List[List[int]]

    def _dfs(self, candidates: List[int], path: List[int], target: int, i: int) -> None:
        # path: 存索引
        if target == 0:
            self.ans.append([candidates[j] for j in path])
            return
        if target < 0:
            return

        for j in range(i, len(candidates)):
            if j > 0 and (candidates[j] == candidates[j - 1]):
                if (path[-1] if len(path) > 0 else -1) != j - 1:
                    continue
            x = candidates[j]
            path.append(j)
            self._dfs(candidates, path, target - x, j + 1)
            path.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        candidates.sort()
        self._dfs(candidates, [], target, 0)
        return self.ans


class Solution2:
    """回溯"""

    def __init__(self):
        self.ans: List[List[int]]

    def _dfs(self, candidates: List[int], path: List[int], visited: Set[int], target: int, i: int) -> None:
        # visited: 存索引
        if target == 0:
            self.ans.append(path.copy())
            return
        if target < 0:
            return

        for j in range(i, len(candidates)):
            if j > 0 and (candidates[j] == candidates[j - 1]) \
                    and j - 1 not in visited:
                continue
            x = candidates[j]
            visited.add(j)
            path.append(x)
            self._dfs(candidates, path, visited, target - x, j + 1)
            visited.remove(j)
            path.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        candidates.sort()
        self._dfs(candidates, [], set(), target, 0)
        return self.ans



candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(Solution().combinationSum2(candidates, target))
print(Solution2().combinationSum2(candidates, target))
