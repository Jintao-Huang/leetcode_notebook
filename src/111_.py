# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
111. 二叉树的最小深度
- 简单
- 模板: bfs
"""

from typing import Union, List, Optional, Deque, Tuple
import json


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(tree: Union[str]) -> Optional[TreeNode]:
    tree = json.loads(tree)  # type: List[int]
    #
    if not len(tree):
        return
    #
    root = TreeNode(tree[0])
    q = deque([(root, "left"), (root, "right")])  # type: Deque[Tuple[TreeNode, str]]
    for node in tree[1:]:
        if node is None:
            q.popleft()
            continue
        #
        node = TreeNode(node)
        setattr(*q.popleft(), node)
        #
        q.append((node, "left"))
        q.append((node, "right"))
    return root


from collections import deque


class Solution:
    def minDepth(self, root: TreeNode) -> int:
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
                # node is target
                if node.left is None and node.right is None:
                    return step + 1
                #
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            #
            step += 1
        return step


tree = "[2,null,3,null,4,null,5,null,6]"
root = build_tree(tree)
print(Solution().minDepth(root))
