# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import Optional, List, Tuple
from template.build.build_tree import build_tree, TreeNode


class Solution:
    """DFS递归(先序). Ot(N) Os(树高). 其中N为节点数"""

    def _dfs(self, n: TreeNode, targetSum: int) -> bool:
        if n.left is None and n.right is None:
            if targetSum == n.val:
                return True
            else:
                return False

        for c in [n.left, n.right]:
            if c is not None and self._dfs(c, targetSum - n.val):
                return True
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self._dfs(root, targetSum)


class Solution2:
    """DFS迭代(先序). Ot(N) Os(树高). 辅助栈时间开销比函数栈少
    注意存targetSum"""

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        stack = [(root, targetSum)]  # type: List[Tuple[TreeNode, int]]
        while len(stack) > 0:
            n, s = stack.pop()
            if n is None:
                continue
            s -= n.val
            if n.left is None and n.right is None:
                if s == 0:
                    return True
            stack.append((n.right, s))
            stack.append((n.left, s))
        return False


root = "[5,4,8,11,null,13,4,7,2,null,null,null,1]"
root = build_tree(root)
target = 22
print(Solution().hasPathSum(root, target))
print(Solution2().hasPathSum(root, target))
