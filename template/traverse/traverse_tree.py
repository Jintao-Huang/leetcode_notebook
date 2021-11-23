# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # type: int
        self.left = left  # type: TreeNode
        self.right = right  # type: TreeNode


def traverse_tree(root: TreeNode):
    # [前序遍历]. preorder_traversal
    traverse_tree(root.left)
    # [中序遍历]. inorder_traversal
    traverse_tree(root.right)
    # [后序遍历]. postorder traversal


from collections import deque
from typing import Optional


def level_traverse(root: Optional[TreeNode]) -> int:
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
            # [if node is None:
            #     continue]
            # [层次访问node]
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            #
        step += 1
    return step


#
from typing import List


class NTreeNode:
    def __init__(self, val=0, children=None):
        self.val = val  # type: int
        self.children = children or []  # type: List[NTreeNode]


def traverse_n_tree(root: NTreeNode):
    for child in root.children:
        # [去边]
        traverse_n_tree(child)
        # [回边]
#
