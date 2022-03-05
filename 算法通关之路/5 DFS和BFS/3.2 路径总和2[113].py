# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import Optional, List, Tuple
from template.build.build_tree import build_tree, TreeNode


class Solution:
    """DFS递归(先序). 回溯. Ot(N) Os(树高). 其中N为节点数
    思考: 为什么int不用回溯, List需要回溯"""

    def __init__(self):
        self.ans: List[List[int]]

    def _dfs(self, root: Optional[TreeNode], path: List[int], targetSum: int) -> None:
        if root is None:
            return
        #
        targetSum -= root.val
        path.append(root.val)

        #
        if root.left is None and root.right is None:
            if targetSum == 0:
                self.ans.append(path.copy())
        else:  # 非叶结点
            self._dfs(root.left, path, targetSum)
            self._dfs(root.right, path, targetSum)
        path.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        self._dfs(root, [], targetSum)
        return self.ans


class Solution2:
    """DFS迭代(先序). Ot(N) Os(树高).
    思考: 为什么这里不需要回溯."""

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []  # type: List[List[int]]
        stack = [(root, [], targetSum)]  # type: List[Tuple[TreeNode, List[int], int]]
        while len(stack) > 0:
            n, path, s = stack.pop()
            if n is None:
                continue
            #
            s -= n.val
            path.append(n.val)
            #
            if n.left is None and n.right is None:
                if s == 0:
                    ans.append(path)
            else:
                stack.append((n.left, path.copy(), s))
                stack.append((n.right, path.copy(), s))
        return ans


root = "[5,4,8,11,null,13,4,7,2,null,null,5,1]"
root = build_tree(root)
target = 22
print(Solution().pathSum(root, target))
print(Solution2().pathSum(root, target))
