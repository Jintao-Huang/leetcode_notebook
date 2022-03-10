# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List, Dict, Optional
from template.build.build_tree import TreeNode, tree_to_str, build_tree


class Solution:
    """dfs(中序). """

    def __init__(self):
        self.lo: TreeNode
        self.hi: TreeNode
        self.prev: TreeNode

    def _dfs(self, n: Optional[TreeNode]) -> None:
        if n is None:
            return
        self._dfs(n.left)
        if self.prev is None:
            self.prev = n
        elif self.prev.val > n.val:
            if self.lo is None:
                self.lo = self.prev
            self.hi = n
        self.prev = n
        self._dfs(n.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # 不需要找出交换的两个结点, 本质是重新排序
        self.lo, self.hi = None, None
        self.prev = None
        self._dfs(root)
        self.lo.val, self.hi.val = self.hi.val, self.lo.val


t = build_tree("[3,1,4,null,null,2]")
print(tree_to_str(t))
print(Solution().recoverTree(t))
print(tree_to_str(t))


# 方便理解
def find2num(nums: List[int]) -> List[int]:
    # 找最左逆序, 最右逆序
    xi, yi = -1, -1
    for i in range(0, len(nums) - 1):
        if nums[i] > nums[i + 1]:
            if xi == -1:
                xi = i
            yi = i + 1
    return [xi, yi]
