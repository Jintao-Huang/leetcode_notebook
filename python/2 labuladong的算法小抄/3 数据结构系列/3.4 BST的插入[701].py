# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from template.build.build_tree import TreeNode, build_tree, tree_to_str


class Solution:
    """二分法"""
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)

        n = root
        while True:
            if val <= n.val:
                if n.left is None:
                    n.left = TreeNode(val)
                    break
                n = n.left
            else:
                if n.right is None:
                    n.right = TreeNode(val)
                    break
                n = n.right
        return root


t = build_tree("[61,46,66,43,null,null,null,39,null,null,null]")
t2 = Solution().insertIntoBST(t, 88)
print(tree_to_str(t2))
