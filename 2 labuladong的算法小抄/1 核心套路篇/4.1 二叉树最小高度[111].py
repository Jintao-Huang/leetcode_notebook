# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from template.build.build_tree import TreeNode, build_tree
from typing import List, Deque
from collections import deque


class Solution:
    """bfs."""

    def _bfs(self, n: TreeNode):
        # 选择: 左右结点
        q = deque([n])  # type: Deque[TreeNode]
        ans = 1
        while len(q) > 0:
            for _ in range(len(q)):
                n = q.popleft()
                if n.left is None and n.right is None:
                    return ans
                for c in [n.left, n.right]:
                    if c is not None:
                        q.append(c)
            ans += 1

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self._bfs(root)


class _Solution:
    """bfs. 深度含义改变."""

    def __init__(self):
        self.ans: List[int]

    def _bfs(self, n: TreeNode):
        # 选择: 左右结点
        if n is None:
            return

        q = deque([n])  # type: Deque[TreeNode]
        while len(q) > 0:
            n = q.popleft()
            if n.left is None and n.right is None:
                self.ans.append(n.val)
            for c in [n.left, n.right]:
                if c is not None:
                    c.val += n.val
                    q.append(c)

    def minDepth(self, root: TreeNode) -> int:
        self.ans = [int(1e8), ]
        self._bfs(root)
        return min(self.ans)


tree = "[3,9,20,null,null,15,7]"
tree = build_tree(tree)
print(_Solution().minDepth(tree))
print(Solution().minDepth(tree))
