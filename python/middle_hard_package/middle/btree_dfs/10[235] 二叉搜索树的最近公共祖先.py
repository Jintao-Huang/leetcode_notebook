# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from python.template.build.build_tree import TreeNode


class Solution:
    def lowestCommonAncestor(
            self,
            n: 'TreeNode',
            p: 'TreeNode',
            q: 'TreeNode'
    ) -> 'TreeNode':
        if n is None or n == p or n == q:
            return n
        if p.val > n.val and q.val > n.val:
            return self.lowestCommonAncestor(n.right, p, q)
        if p.val < n.val and q.val < n.val:
            return self.lowestCommonAncestor(n.left, p, q)

        return n
