# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from template.build.build_tree import TreeNode
from typing import Tuple


class Solution:
    """naive"""

    def __init__(self):
        self.ans = 0

    def _dfs(self, n):
        if n is None:
            return
        self._dfs(n.left)
        self._dfs(n.right)
        self.ans += 1

    def countNodes(self, root: TreeNode) -> int:
        self._dfs(root)
        return self.ans


class Solution2:
    """naive"""

    def _dfs(self, n: TreeNode) -> int:
        if n is None:
            return 0
        return self._dfs(n.left) + self._dfs(n.right) + 1

    def countNodes(self, root: TreeNode) -> int:
        return self._dfs(root)


class Solution3:
    """利用完全二叉树性质"""

    def test_lr(self, n: TreeNode) -> Tuple[bool, int]:
        l = r = n
        ans = 0
        while True:
            if r is None:
                if l is None:
                    return True, ans
                return False, ans
            l = l.left
            r = r.right
            ans += 1

    def _dfs(self, n: TreeNode) -> int:

        b, h = self.test_lr(n)
        if b:
            return 2 ** h - 1

        return self._dfs(n.left) + self._dfs(n.right) + 1

    def countNodes(self, root: TreeNode) -> int:
        return self._dfs(root)
