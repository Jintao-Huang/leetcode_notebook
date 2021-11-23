# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
105. 从前序与中序遍历序列构造二叉树
- 中等
- 推荐
=
- 二叉树的前序遍历
"""
import json
from typing import List, Union, Optional, Deque, Tuple, Dict, Sequence
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_tree(root: Optional[TreeNode]) -> str:
    ans = []
    if root is None:
        return json.dumps(ans)

    #
    def _all_None(x: Sequence[Optional[TreeNode]], start: int, end: int) -> bool:
        ans = True
        x = list(x)
        for i in range(start, end):
            node = x[i]
            if node is not None:
                ans = False
        return ans

    #
    q = deque([root])  # type: Deque[Optional[TreeNode]]
    #
    while len(q):
        sz = len(q)
        #
        if _all_None(q, 0, sz):
            break
        #
        for i in range(sz):
            node = q.popleft()  # type: TreeNode
            if node is None:
                ans.append(None)
                q.append(None)
                q.append(None)
            else:
                ans.append(node.val)
                q.append(node.left)
                q.append(node.right)
            #
    return json.dumps(ans)


#
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        pre_lo, pre_hi = 0, len(preorder)  # [)
        in_lo, in_hi = 0, len(inorder)
        in_map = {val: i for i, val in enumerate(inorder)}  # type: Dict[int, int]

        #
        def _dfs(pre_lo: int, pre_hi: int, in_lo: int, in_hi: int) -> Optional[TreeNode]:
            """使用前序遍历框架"""
            nonlocal preorder, inorder, in_map
            #
            if pre_lo >= pre_hi or in_lo >= in_hi:
                return None
            #
            root = TreeNode(preorder[pre_lo])
            root_idx = in_map[root.val]  # 在中序遍历中的索引
            num_left, num_right = root_idx - in_lo, in_hi - root_idx - 1  # root的左右子树个数
            #
            root.left = _dfs(
                pre_lo + 1, pre_lo + 1 + num_left, in_lo, in_lo + num_left
            )
            root.right = _dfs(
                pre_hi - num_right, pre_hi,
                in_hi - num_right, in_hi
            )
            return root

        return _dfs(pre_lo, pre_hi, in_lo, in_hi)


# test
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root = Solution().buildTree(preorder, inorder)
print(level_tree(root))
