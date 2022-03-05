# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from template.build.build_tree import TreeNode, build_tree
from typing import Optional, List


class Solution:
    """后序遍历. Ot(N) Os(树高)"""

    def __init__(self):
        self.ans: int

    def _maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        m1 = max(self._maxPathSum(root.left), 0)
        m2 = max(self._maxPathSum(root.right), 0)
        self.ans = max(m1 + m2 + root.val, self.ans)
        return max(m1, m2) + root.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = int(-1e10)
        self._maxPathSum(root)
        return self.ans


root = "[-10,9,20,null,null,15,7]"
root = "[2,-1]"
root = build_tree(root)

print(Solution().maxPathSum(root))
