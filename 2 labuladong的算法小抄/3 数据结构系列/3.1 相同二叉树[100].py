# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from template.build.build_tree import TreeNode, build_tree
from typing import List


class Solution:

    def _dfs(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None:
            return q is None
        if q is None:
            return False
        #
        return p.val == q.val and \
               self._dfs(p.left, q.left) and \
               self._dfs(p.right, q.right)


    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self._dfs(p, q)


t1 = build_tree("[10,5,15]")
t2 = build_tree("[10,5,null,null,15]")
print(Solution().isSameTree(t1, t2))
