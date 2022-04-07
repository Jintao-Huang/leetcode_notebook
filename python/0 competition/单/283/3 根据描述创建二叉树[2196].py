# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Optional, Dict, Set
from template.build.build_tree import tree_to_str

from template.build.build_tree import TreeNode


class Solution:
    """二叉树"""

    @staticmethod
    def build_tree(descriptions: List[List[int]]) -> TreeNode:
        """建树(哈希表)+找根"""
        n = {c: TreeNode(c, None, None) for _, c, _ in descriptions}  # type: Dict[int, TreeNode]
        for p, c, is_left in descriptions:
            if p not in n:
                n[p] = TreeNode(p, None, None)
                root = n[p]
            if is_left:
                n[p].left = n[c]
            else:
                n[p].right = n[c]
        return root

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        return self.build_tree(descriptions)


descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
tree = Solution().createBinaryTree(descriptions)
print(tree_to_str(tree))
