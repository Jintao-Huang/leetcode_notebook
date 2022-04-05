# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List

"""12 二叉搜索树"""


class TreeNode:
    def __init__(self, key: int, p: 'TreeNode' = None,
                 left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.key = key
        self.p = p
        self.left = left
        self.right = right


def inorder_tree_walk(r: TreeNode) -> List[int]:
    # p162
    ans = []

    def _itw(x: TreeNode):
        if x is not None:
            _itw(x.left)
            ans.append(x.key)
            _itw(x.right)

    _itw(r)
    return ans


from typing import Optional
import json
from collections import deque


def build_tree(tree: str) -> Optional[TreeNode]:
    l = json.loads(tree)
    if len(l) == 0:
        return None

    root = TreeNode(l[0], None, None)
    q = deque([(root, "left"), (root, "right")])
    for i in range(1, len(l)):
        x = l[i]
        p, s = q.popleft()
        n = None if x is None else TreeNode(x, p, None, None)
        setattr(p, s, n)
        if n is not None:
            q.append((n, "left"))
            q.append((n, "right"))
    return root


if __name__ == '__main__':
    r = """[15, 6, 18, 3, 7, 17, 20,
          2, 4, null, 13, null, null, null, null,
          null, null, null, null, 9]"""
    r = build_tree(r)


# if __name__ == '__main__':
#     print(inorder_tree_walk(r))

def tree_search(x: TreeNode, k: int) -> Optional[TreeNode]:
    # p163
    if x is None or k == x.key:
        return x
    if k < x.key:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)


def iterative_tree_search(x: TreeNode, k: int) -> Optional[TreeNode]:
    # p163
    while x is not None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x


def tree_minimum(x: TreeNode) -> TreeNode:
    # p164
    while x.left is not None:
        x = x.left
    return x


def tree_maximum(x: TreeNode) -> TreeNode:
    # p164
    while x.right is not None:
        x = x.right
    return x


# if __name__ == '__main__':
#     print(tree_search(r, 7).key)
#     print(iterative_tree_search(r, 7).key)
#     print(tree_minimum(r).key)
#     print(tree_maximum(r).key)

def tree_successor(x: TreeNode) -> TreeNode:
    # p164
    if x.right is not None:
        return tree_minimum(x.right)
    y = x.p
    while y is not None and x == y.right:
        x = y
        y = y.p
    return y


def tree_predecessor(x: TreeNode) -> TreeNode:
    # p164
    if x.left is not None:
        return tree_maximum(x.left)
    y = x.p
    while y is not None and x == y.left:
        x = y
        y = y.p
    return y


# if __name__ == '__main__':
#     x13 = r.left.right.right
#     x17 = r.right.left
#     print(tree_successor(r).key)
#     print(tree_predecessor(r).key)
#     print(tree_successor(x13).key)
#     print(tree_predecessor(x17).key)

class Tree:
    def __init__(self, root: TreeNode = None):
        self.root = root

    def __str__(self) -> str:
        root = self.root
        if root is None:
            return "[]"

        ans = []
        q = deque([root])
        while len(q) > 0:
            all_None = True
            for i in range(len(q)):
                n = q.popleft()
                if n is None:
                    ans.append(None)
                    continue
                ans.append(n.key)
                q.append(n.left)
                q.append(n.right)
                if n.left or n.right:
                    all_None = False
            if all_None:
                break
        while len(ans) > 0 and ans[-1] is None:
            ans.pop()

        return json.dumps(ans)


def tree_insert(T: Tree, z: TreeNode) -> None:
    # p166
    y = None  # type: Optional[TreeNode]
    x = T.root
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y is None:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z


def transplant(T: Tree, u: TreeNode, v: TreeNode) -> None:
    # p168
    # 用v替代u
    if u.p is None:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v is not None:
        v.p = u.p


def tree_delete(T: Tree, z: TreeNode) -> None:
    # p168
    # 删z
    if z.left is None:
        transplant(T, z, z.right)
    elif z.right is None:
        transplant(T, z, z.left)
    else:
        y = tree_minimum(z.right)  # 替换z的节点
        if y.p != z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        transplant(T, z, y)
        y.left = z.left
        y.left.p = y


# if __name__ == '__main__':
#     t = Tree(None)
#     r = TreeNode(10)
#     tree_insert(t, r)
#     tree_insert(t, TreeNode(9))
#     tree_insert(t, TreeNode(12))
#     tree_insert(t, TreeNode(11))
#     tree_insert(t, TreeNode(13))
#     print(t)
#     tree_delete(t, r)
#     print(t)

"""
1. p169. 随机构建二叉搜索树
"""
