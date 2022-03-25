# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from template.build.build_tree import TreeNode


class Solution:
    """二分法"""

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        n = root
        while True:
            if n is None:
                return None
            if n.val == val:
                return n
            elif val < n.val:
                n = n.left
            else:
                n = n.right


class Solution2:
    """dfs"""
