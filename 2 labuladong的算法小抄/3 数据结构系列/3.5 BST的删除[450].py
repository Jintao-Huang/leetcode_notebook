# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from template.build.build_tree import TreeNode, build_tree, tree_to_str
from typing import Optional


class Solution:
    def delete(self, n: TreeNode) -> TreeNode:
        if n.left is None and n.right is None:
            return None
        if n.left is None:
            return n.right
        if n.right is None:
            return n.left
        # find_next
        nn = n.right
        p, left = n, False
        while nn.left is not None:
            p = nn
            left = True
            nn = nn.left
        nn.val, n.val = n.val, nn.val
        if left:
            p.left = self.delete(nn)
        else:
            p.right = self.delete(nn)
        return n

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        root = TreeNode(int(1e8), root, None)  #
        n = root
        while True:
            if key < n.val:
                if n.left is None:
                    break
                if n.left.val == key:
                    n.left = self.delete(n.left)
                    break
                n = n.left
            else:
                if n.right is None:
                    break
                if n.right.val == key:
                    n.right = self.delete(n.right)
                    break
                n = n.right
        return root.left


t1 = build_tree("[5,3,6,2,4,null,7]")
print(tree_to_str(Solution().deleteNode(t1, 3)))
t1 = build_tree("[5,3,6,2,4,null,7]")
print(tree_to_str(Solution().deleteNode(t1, 0)))
