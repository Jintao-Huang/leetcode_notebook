# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
124. 二叉树中的最大路径和
- 困难
- 推荐
=
- 二叉树的后序遍历
- 动态规划
"""
import json
from typing import List, Union, Optional, Deque, Tuple, Sequence
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(tree: Union[str, List]) -> Optional[TreeNode]:
    if isinstance(tree, str):
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


#
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        INT_MIN = -0x7fffffff
        ans = INT_MIN

        #
        def _dfs(root: Optional[TreeNode]) -> int:
            """返回的是root到某结点的最大路径和.
                使用后续遍历框架
            """
            nonlocal ans
            #
            if root is None:
                return 0
            #
            left = max(0, _dfs(root.left))
            right = max(0, _dfs(root.right))
            #
            ans = max(ans, left + right + root.val)
            return max(left, right) + root.val

        #
        _dfs(root)
        return ans


tree = "[-10, 9, 20, null, null, 15, 7]"
tree = build_tree(tree)
print(Solution().maxPathSum(tree))
