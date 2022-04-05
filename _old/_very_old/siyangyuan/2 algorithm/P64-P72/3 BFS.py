# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from collections import deque
from typing import List


class Solution102:
    """二叉树的层次遍历. 见树"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution107:
    """二叉树的层次遍历2"""

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        out = []
        if root is None:
            return out
        queue = deque([root])
        while len(queue) > 0:
            t = []
            for _ in range(len(queue)):  # 一层一个for循环
                x = queue.popleft()
                t.append(x.val)
                if x.left is not None:
                    queue.append(x.left)
                if x.right is not None:
                    queue.append(x.right)
            out.append(t)
        out.reverse()
        return out


class Solution200:
    """岛屿数量. 见DFS"""
