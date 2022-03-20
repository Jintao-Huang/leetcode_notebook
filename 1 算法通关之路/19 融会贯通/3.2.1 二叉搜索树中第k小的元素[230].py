# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Optional

from template.build.build_tree import TreeNode, build_tree


class Solution:
    def __init__(self):
        self.ans: int

    def _dfs(self, n: Optional[TreeNode], i: int) -> int:
        if n is None:
            return i

        i = self._dfs(n.left, i)
        if i == 1:
            self.ans = n.val
        return self._dfs(n.right, i - 1)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self._dfs(root, k)
        return self.ans


root = build_tree("[3,1,4,null,2]")
k = 1
print(Solution().kthSmallest(root, k))
