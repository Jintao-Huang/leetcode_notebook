# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from template.build.build_tree import build_tree, TreeNode
from typing import Tuple


class Solution:
    def _dfs(self, n: TreeNode) -> Tuple[int, int]:
        if n is None:
            return 0, 0
        dp1 = self._dfs(n.left)
        dp2 = self._dfs(n.right)
        dp = (max(dp1[0], dp1[1]) + max(dp2[0], dp2[1]), dp1[0] + dp2[0] + n.val)
        return dp

    def rob(self, root: TreeNode) -> int:
        return max(self._dfs(root))


root = build_tree("[3,2,3,null,3,null,1]")
print(Solution().rob(root))
