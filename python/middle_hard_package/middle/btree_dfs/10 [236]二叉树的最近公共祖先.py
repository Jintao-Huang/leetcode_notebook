# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from python.template.build.build_tree import TreeNode


class Solution:
    def dfs(self, n: TreeNode, p: TreeNode, q: TreeNode) -> bool:
        if n is None:
            return False

        b1 = self.dfs(n.left, p, q)
        b2 = self.dfs(n.right, p, q)
        b3 = n == p or n == q
        if self.ans is None and b1 + b2 + b3 >= 2:
            self.ans = n
        return b1 or b2 or b3

    def lowestCommonAncestor(
            self,
            root: 'TreeNode',
            p: 'TreeNode',
            q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        self.dfs(root, p, q)
        return self.ans


class Solution2:
    def dfs(self, n: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if n is None:
            return None
        if n == p or n == q:
            return n

        n1 = self.dfs(n.left, p, q)
        n2 = self.dfs(n.right, p, q)
        if n1 is not None and n2 is not None:
            return n

        return n1 if n1 is not None else n2

    def lowestCommonAncestor(
            self,
            root: 'TreeNode',
            p: 'TreeNode',
            q: 'TreeNode') -> 'TreeNode':

        return self.dfs(root, p, q)
