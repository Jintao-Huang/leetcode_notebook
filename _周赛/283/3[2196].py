# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Optional, Dict, Set
from template.build.build_tree import tree_to_str


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """二叉树"""
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        if len(descriptions) == 0:
            return None

        d = {}  # type: Dict[int, TreeNode]
        h = set()  # type: Set[TreeNode]
        nh = set()  # type: Set[TreeNode]
        for p, c, is_left in descriptions:


            if c in d:
                c_node = d[c]
            else:
                c_node = TreeNode(c, None, None)
                d[c] = c_node
            l, r = None, None
            if is_left:
                l = c_node
            else:
                r = c_node
            if p in d:
                p_node = d[p]
                if is_left:
                    p_node.left = l
                else:
                    p_node.right = r
            else:
                p_node = TreeNode(p, l, r)
                d[p] = p_node
            #
            h.add(p_node)
            nh.add(c_node)
            if p_node in nh:
                h.remove(p_node)
            if c_node in h:
                h.remove(c_node)
        return h.pop()

descriptions = [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]]
tree = Solution().createBinaryTree(descriptions)
print(tree_to_str(tree))
