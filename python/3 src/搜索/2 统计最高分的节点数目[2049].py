# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Dict


class Solution:
    """隐式建树+dfs"""

    def __init__(self):
        self.ans = [0, 0]

    def _dfs(self, n: int, children: List[List[int]]) -> int:
        """后序遍历"""
        s = 1  # 总结点数
        p = 1

        for cn in children[n]:
            x = self._dfs(cn, children)
            s += x
            p *= x
        n_p = len(children) - s
        if n_p > 0:
            p *= n_p
        if p > self.ans[0]:
            self.ans = [p, 1]
        elif p == self.ans[0]:
            self.ans[1] += 1
        return s

    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # build tree
        children = [[] for _ in range(len(parents))]
        for i in range(1, len(parents)):
            p = parents[i]
            children[p].append(i)

        self._dfs(0, children)
        return self.ans[1]


parents = [-1, 2, 0, 2, 0]
print(Solution().countHighestScoreNodes(parents))
