# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from python.template.build.build_tree import TreeNode
from typing import Optional


class Solution:
    def dfs(self, n: TreeNode) -> int:
        if n is None:
            return 0
        x1 = self.dfs(n.left)
        x2 = self.dfs(n.right)
        self.ans += abs(x1) + abs(x2)
        v = n.val - 1 + x1 + x2
        return v

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
