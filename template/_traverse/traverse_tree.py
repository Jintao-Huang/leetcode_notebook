# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # type: int
        self.left = left  # type: TreeNode
        self.right = right  # type: TreeNode


class NTreeNode:
    def __init__(self, val=0, children=None):
        self.val = val  # type: int
        self.children = children or []  # type: List[NTreeNode]


##

def traverse_tree(root: TreeNode):
    # base
    # [前序遍历]. preorder_traversal
    traverse_tree(root.left)
    # [中序遍历]. inorder_traversal
    traverse_tree(root.right)
    # [后序遍历]. postorder traversal


#
def traverse_n_tree(root: NTreeNode):
    # base
    for child in root.children:
        # [去边]
        traverse_n_tree(child)
        # [回边]


##
from collections import deque
from typing import Optional


def level_traverse_tree(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    #
    q = deque([root])
    step = 0
    #
    while len(q) > 0:
        sz = len(q)
        #
        for i in range(sz):
            node = q.popleft()  # type: TreeNode
            # [层次访问node]
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        #
        step += 1
    return step


def level_traverse_n_tree(root: Optional[NTreeNode]) -> int:
    if root is None:
        return 0
    #
    q = deque([root])
    step = 0
    #
    while len(q) > 0:
        sz = len(q)
        #
        for i in range(sz):
            node = q.popleft()  # type: NTreeNode
            # [层次访问node]
            for child in node.children:
                if child is not None:
                    q.append(child)
        #
        step += 1
    return step
