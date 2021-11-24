# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
111. 二叉树的最小深度
- 简单
- 模板: bfs
=
- bfs
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
    """bfs. 模板1: deque"""

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        #
        q = deque([root])  # type: Deque[TreeNode]
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
            step += 1
        return step

    def minDepth2(self, root: TreeNode) -> int:
        """bfs. 模板2. cost + deque"""
        if root is None:
            return 0
        #
        cost = 0
        q = deque([(cost, root)])  # type: Deque[Tuple[int, TreeNode]]
        #
        while len(q) > 0:
            cost, node = q.popleft()  # type: int, TreeNode
            # node is target
            if node.left is None and node.right is None:
                return cost + 1
            #
            cost += 1
            if node.left is not None:
                q.append((cost, node.left))
            if node.right is not None:
                q.append((cost, node.right))
        return cost


tree = "[2,null,3,null,4,null,5,null,6]"
root = build_tree(tree)
print(Solution().minDepth(root))

tree = "[2,null,3,null,4,null,5,null,6]"
root = build_tree(tree)
print(Solution().minDepth2(root))

#
import heapq


class PriorityQueue:
    def __init__(self, initial_list=None):
        queue = initial_list if initial_list else []
        heapq.heapify(queue)
        #
        self._queue = queue

    def add(self, x):
        queue = self._queue
        heapq.heappush(queue, x)

    def pop(self):
        queue = self._queue
        return heapq.heappop(queue)

    def __len__(self):
        return len(self._queue)


class Solution2:
    """bfs. 模板3. cost + PriorityQueue

    cost扩充速度不同. 用 `PriorityQueue` 替代"""

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        #
        cost = 0
        q = PriorityQueue([(cost, id(root), root)])  # PriorityQueue[Tuple[int, int, TreeNode]]
        #
        while len(q) > 0:
            cost, _, node = q.pop()  # type: int, int, TreeNode
            # node is target
            if node.left is None and node.right is None:
                return cost + 1
            #
            cost += 1
            if node.left is not None:
                q.add((cost, id(node.left), node.left))
            if node.right is not None:
                q.add((cost, id(node.right), node.right))
        return cost


tree = "[2,null,3,null,4,null,5,null,6]"
root = build_tree(tree)
print(Solution2().minDepth(root))
