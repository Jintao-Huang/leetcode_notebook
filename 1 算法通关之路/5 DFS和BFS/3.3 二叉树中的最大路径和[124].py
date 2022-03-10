# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from template.build.build_tree import TreeNode, build_tree
from typing import Optional, List


class Solution:
    """后序遍历. Ot(N) Os(树高)"""

    def __init__(self):
        self.ans: int

    def _dfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        m1 = self._dfs(root.left)
        m2 = self._dfs(root.right)
        self.ans = max(m1 + m2 + root.val, self.ans)
        return max(max(m1, m2) + root.val, 0)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = int(-1e8)
        self._dfs(root)
        return self.ans


root = "[-10,9,20,null,null,15,7]"
root = "[2,-1]"
root = build_tree(root)

print(Solution().maxPathSum(root))
