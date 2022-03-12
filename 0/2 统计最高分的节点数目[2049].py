# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Dict


class TreeNode:
    def __init__(self, val=0, children=None):
        self.val = val  # type: int
        self.children = []  # type: List[TreeNode]


def build_tree2(parents: List[int]) -> TreeNode:
    if len(parents) == 0:
        return None
    # 可改用数组
    d = {i: TreeNode(i, None) for i in range(len(parents))}  # type: Dict[int, TreeNode]
    for c in range(1, len(parents)):
        p = parents[c]
        cn, pn = d[c], d[p]
        pn.children.append(cn)
    return d[0]


class Solution:
    """建树+dfs"""

    def __init__(self):
        self.ans: List[int]  # 值, 数目
        self.n: int

    def _dfs(self, tn: TreeNode) -> int:
        """后序遍历"""
        if tn is None:
            return 0
        s = 1
        p = 1
        for cn in tn.children:
            x = self._dfs(cn)
            s += x
            p *= x
        if self.n - s > 0:
            p *= self.n - s
        if p > self.ans[0]:
            self.ans = [p, 1]
        elif p == self.ans[0]:
            self.ans[1] += 1
        return s

    def countHighestScoreNodes(self, parents: List[int]) -> int:
        tn = build_tree2(parents)
        self.ans, self.n = [0, 0], len(parents)
        self._dfs(tn)

        return self.ans[1]


parents = [-1, 2, 0, 2, 0]
print(Solution().countHighestScoreNodes(parents))
