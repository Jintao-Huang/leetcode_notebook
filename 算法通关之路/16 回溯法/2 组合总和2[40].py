# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from typing import List, Set, Dict, Union, Tuple


def counter(nums: List[int], need_sorted: bool = False) -> Union[Dict, List[List[int]]]:
    """返回 按字典序."""
    d = {}
    for x in nums:
        if x not in d:
            d[x] = 0
        d[x] += 1
    #
    if need_sorted:
        keys = sorted(d.keys())
        return [[k, d[k]] for k in keys]
    else:
        return d


class Solution:
    """回溯"""

    def __init__(self):
        self.ans: List[List[int]]

    def _dfs(self, candidates: List[List[int]], path: List[int], target: int, i: int) -> None:
        # 选择: 选/不选
        if target == 0:
            self.ans.append(path.copy())
            return
        if target < 0 or i >= len(candidates):
            return
        if candidates[i][1] == 0:
            i += 1
        if i >= len(candidates):
            return

        candidates[i][1] -= 1
        x = candidates[i][0]
        path.append(x)
        self._dfs(candidates, path, target - x, i)
        candidates[i][1] += 1
        path.pop()
        self._dfs(candidates, path, target, i + 1)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        candidates = counter(candidates, need_sorted=True)
        self._dfs(candidates, [], target, 0)
        return self.ans


class _Solution:
    """回溯. 超时"""

    def __init__(self):
        self.ans: Set[Tuple[int]]

    def _dfs(self, candidates: List[int], path: List[int], target: int, i: int) -> None:
        if target == 0:
            self.ans.add(tuple(path))
            return
        if target < 0 or i >= len(candidates):
            return

        x = candidates[i]
        path.append(x)
        self._dfs(candidates, path, target - x, i + 1)
        path.pop()
        self._dfs(candidates, path, target, i + 1)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = set()
        candidates.sort()
        self._dfs(candidates, [], target, 0)
        return [list(a) for a in self.ans]


candidates = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
target = 27
print(Solution().combinationSum2(candidates, target))
print(_Solution().combinationSum2(candidates, target))
