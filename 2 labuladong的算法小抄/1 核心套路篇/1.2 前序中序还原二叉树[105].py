# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Dict, Optional
from template.build.build_tree import TreeNode, tree_to_str


class Solution:
    """dfs(后序遍历)"""

    def _dfs(self, preorder: List[int], inorder: List[int], d: Dict[int, int],
             pre_lo: int, pre_hi: int, in_lo: int, in_hi: int) -> Optional[TreeNode]:
        if pre_lo > pre_hi:
            return None
        val = preorder[pre_lo]
        in_mid = d[val]

        len1, len2 = in_mid - in_lo, in_hi - in_mid
        left = self._dfs(preorder, inorder, d, pre_lo + 1, pre_lo + len1,
                         in_lo, in_lo + len1 - 1)
        right = self._dfs(preorder, inorder, d, pre_hi + 1 - len2, pre_hi,
                          in_hi + 1 - len2, in_hi)
        return TreeNode(val, left, right)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        d = {v: i for i, v in enumerate(inorder)}  # type: Dict[int, int]  # 值, 索引
        return self._dfs(preorder, inorder, d, 0, len(preorder) - 1, 0, len(preorder) - 1)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
head = Solution().buildTree(preorder, inorder)
print(tree_to_str(head))
