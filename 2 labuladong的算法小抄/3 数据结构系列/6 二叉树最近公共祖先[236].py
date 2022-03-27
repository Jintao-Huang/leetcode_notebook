# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from template.build.build_tree import TreeNode, build_tree


class Solution:
    def __init__(self):
        self.ans = None

    def _dfs(self, n: TreeNode, p: TreeNode, q: TreeNode) -> int:
        if n is None or self.ans is not None:
            return 0
        ans = self._dfs(n.left, p, q)
        ans += self._dfs(n.right, p, q)
        ans += (n.val == p.val or n.val == q.val)
        if ans == 2 and self.ans is None:
            self.ans = n
        return ans

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self._dfs(root, p, q)
        return self.ans


t = build_tree("[3,5,1,6,2,0,8,null,null,7,4]")
print(Solution().lowestCommonAncestor(t, TreeNode(5), TreeNode(1)))
