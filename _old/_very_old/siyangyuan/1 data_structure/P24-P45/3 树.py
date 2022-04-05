# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
1. 递归
*2. 通用法(visited) 与 简化
3. 一直左法(压栈时)
"""


class Solution144:
    """二叉树的前序遍历"""

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """递归. Ot(N) Os(N). N为结点数"""
        res = []

        def _preorderTraversal(_root: TreeNode):
            if _root is None:
                return
            res.append(_root.val)
            _preorderTraversal(_root.left)
            _preorderTraversal(_root.right)

        _preorderTraversal(root)
        return res

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        """迭代. Ot(N) Os(N). N为结点数"""
        res = []
        stack = [(root, False)]  # visited 先遍历(False) 后访问(True)
        while len(stack) > 0:
            x = stack.pop()
            if x[0] is None:
                continue
            elif x[1] is False:
                stack += [(x[0].right, False), (x[0].left, False), (x[0], True)]
            else:
                res.append(x[0].val)
        return res

    def preorderTraversal3(self, root: TreeNode) -> List[int]:
        """迭代简化. Ot(N) Os(N). N为结点数"""
        res = []
        stack = [root]
        while len(stack) > 0:
            x = stack.pop()
            if x is None:
                continue
            res.append(x.val)
            stack += [x.right, x.left]
        return res

    def preorderTraversal4(self, root: TreeNode) -> List[int]:
        """迭代一直左法. Ot(N) Os(N). N为结点数"""
        res, stack = [], []

        def add_and_visit_all_left(_x):
            while _x is not None:
                res.append(_x.val)
                stack.append(_x)
                _x = _x.left

        add_and_visit_all_left(root)
        while len(stack) > 0:
            x = stack.pop()
            add_and_visit_all_left(x.right)
        return res


root = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, None, TreeNode(6)))
print(Solution144().preorderTraversal(root))
print(Solution144().preorderTraversal2(root))
print(Solution144().preorderTraversal3(root))
print(Solution144().preorderTraversal4(root))

# [0, 1, 3, 4, 2, 6]
# [0, 1, 3, 4, 2, 6]
# [0, 1, 3, 4, 2, 6]
# [0, 1, 3, 4, 2, 6]

"""
1. 递归
2. 通用法(visited)
3. 一直左法(弹栈时)
"""


class Solution94:
    """二叉树的中序遍历"""

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """递归. Ot(N) Os(N). N为结点数"""
        res = []

        def _inorderTraversal(_root: TreeNode):
            if _root is None:
                return
            _inorderTraversal(_root.left)
            res.append(_root.val)
            _inorderTraversal(_root.right)

        _inorderTraversal(root)
        return res

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        """迭代. Ot(N) Os(N). N为结点数"""
        res = []
        stack = [(root, False)]  # visited 先遍历(False) 后访问(True)
        while len(stack) > 0:
            x = stack.pop()
            if x[0] is None:
                continue
            elif x[1] is False:
                stack += [(x[0].right, False), (x[0], True), (x[0].left, False)]
            else:
                res.append(x[0].val)
        return res

    def inorderTraversal3(self, root: TreeNode) -> List[int]:
        """迭代一直左法. Ot(N) Os(N). N为结点数"""

        def add_all_left(_x):
            """加入结点的左边一条"""
            while _x is not None:
                stack.append(_x)
                _x = _x.left

        stack, res = [], []
        add_all_left(root)
        while len(stack) > 0:
            # 左边已经遍历好
            x = stack.pop()
            res.append(x.val)  # 遍历根
            add_all_left(x.right)  # 遍历右边
        return res


print(Solution94().inorderTraversal(root))
print(Solution94().inorderTraversal2(root))
print(Solution94().inorderTraversal3(root))

# [3, 1, 4, 0, 2, 6]
# [3, 1, 4, 0, 2, 6]
# [3, 1, 4, 0, 2, 6]


"""
1. 递归
2. 通用法(visited) 与 简化
"""


class Solution145:
    """二叉树的后序遍历"""

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """递归. Ot(N) Os(N). N为结点数"""
        res = []

        def _postorderTraversal(_root: TreeNode):
            if _root is None:
                return
            _postorderTraversal(_root.left)
            _postorderTraversal(_root.right)
            res.append(_root.val)

        _postorderTraversal(root)
        return res

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        """迭代. Ot(N) Os(N). N为结点数"""
        res = []
        stack = [(root, False)]  # visited 先遍历(False) 后访问(True)
        while len(stack) > 0:
            x = stack.pop()
            if x[0] is None:
                continue
            elif x[1] is False:
                stack += [(x[0], True), (x[0].right, False), (x[0].left, False)]
            else:
                res.append(x[0].val)
        return res

    def postorderTraversal3(self, root: TreeNode) -> List[int]:
        """迭代简化. Ot(N) Os(N). N为结点数"""
        res = []
        stack = [root]
        while len(stack) > 0:
            x = stack.pop()
            if x is None:
                continue
            res.append(x.val)
            stack += [x.left, x.right]
        res.reverse()
        return res


root = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, None, TreeNode(6)))
print(Solution145().postorderTraversal(root))
print(Solution145().postorderTraversal2(root))
print(Solution145().postorderTraversal3(root))
# [3, 4, 1, 6, 2, 0]
# [3, 4, 1, 6, 2, 0]
# [3, 4, 1, 6, 2, 0]

from collections import deque


class Solution102:
    """二叉树的层序遍历"""

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """Ot(N) Os(N). N为结点数"""
        res = []
        if root is None:
            return res
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
            res.append(t)
        return res

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        """Ot(N) Os(N). N为结点数"""
        res = []
        queue = deque([(root, 0)])  # 0 代表层
        while len(queue) > 0:
            x, i = queue.popleft()
            if x is None:
                continue
            if len(res) <= i:  # res[n]
                res.append([])
            res[-1].append(x.val)
            queue += [(x.left, i + 1), (x.right, i + 1)]
        return res

    def levelOrder_v(self, root: TreeNode) -> List[int]:
        """variant变体. Ot(N) Os(N). N为结点数"""
        queue = deque([root])  # 0 代表层
        res = []
        while len(queue) > 0:
            x = queue.popleft()
            if x is None:
                continue
            res.append(x.val)
            queue += [x.left, x.right]
        return res


root = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, None, TreeNode(6)))
print(Solution102().levelOrder(root))
print(Solution102().levelOrder2(root))
print(Solution102().levelOrder_v(root))
