# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from template.build.build_tree import build_tree, TreeNode


class Solution:
    def __init__(self):
        self.prev = None

    def _dfs(self, n: TreeNode) -> bool:
        if n is None:
            return True
        if self._dfs(n.left) is False:
            return False
        if self.prev is not None and self.prev.val >= n.val:
            return False
        self.prev = n
        return self._dfs(n.right)

    def isValidBST(self, root: TreeNode) -> bool:
        return self._dfs(root)
