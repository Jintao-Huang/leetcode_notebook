# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from enum import Enum

"""13 红黑树"""

"""
红黑树比较于AVL树的优点:
1. 高度平衡较松, 旋转少(任何不平衡都能在三次旋转之内解决)
    插入删除操作多时, 比AVL树效果更好.
"""


class Color(Enum):
    Red = 1
    Black = 2


class RBTreeNode:
    # p174
    def __init__(self, key: int, color: Color = None,
                 p: 'RBTreeNode' = None, left: 'RBTreeNode' = None, right: 'RBTreeNode' = None):
        self.key = key
        if color is None:
            color = Color.Black
        self.color = color
        self.p = p
        self.left = left
        self.right = right


"""p174 红黑树的性质
1. 根黑, 叶(NIL)黑. 
    叶节点不存信息, 用nil哨兵代替(节约内存). 根结点父结点也为nil
2. 某红, 双子黑
3. 每个结点到后代叶节点的简单路径上, 相同黑
"""

import json
from collections import deque


class RBTree:
    def __init__(self, root: RBTreeNode = None, nil: RBTreeNode = None):
        if nil is None:
            nil = RBTreeNode(0, Color.Black)
        if root is None:
            root = nil
        self.root = root
        self.nil = nil

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
                if n == self.nil:
                    ans.append(None)
                    continue
                ans.append((n.key, 'R' if n.color == Color.Red else 'B'))
                q.append(n.left)
                q.append(n.right)
                if n.left != self.nil or n.right != self.nil:
                    all_None = False
            if all_None:
                break
        while len(ans) > 0 and ans[-1] is None:
            ans.pop()

        return json.dumps(ans)


def left_rotate(T: RBTree, x: RBTreeNode) -> None:
    # p177
    # 假设x.right不为空
    y = x.right
    x.right = y.left
    if y.left != T.nil:
        y.left.p = x
    y.p = x.p
    if x.p == T.nil:
        T.root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.left = x
    x.p = y


def right_rotate(T: RBTree, y: RBTreeNode) -> None:
    # 假设x.left不为空
    x = y.left
    y.left = x.right
    if x.right != T.nil:
        x.right.p = y
    x.p = y.p
    if y.p == T.nil:
        T.root = x
    elif y == y.p.left:
        y.p.left = x
    else:
        y.p.right = x
    x.right = y
    y.p = x


# if __name__ == '__main__':
#     nil = RBTreeNode(0, Color.Black)
#     x9 = RBTreeNode(9, Color.Black, None, nil, nil)
#     x19 = RBTreeNode(19, Color.Black, None, nil, nil)
#     x14 = RBTreeNode(14, Color.Black, None, nil, nil)
#     x18 = RBTreeNode(18, Color.Red, None,x14, x19)
#     x11 = RBTreeNode(11, Color.Black, nil, x9, x18)
#     x9.p = x11
#     x19.p = x18
#     x14.p = x18
#     x18.p = x11
#     t = RBTree(x11, nil)
#     print(t)
#     left_rotate(t, x11)
#     print(t)
#     right_rotate(t, x18)
#     print(t)

def rb_insert(T: RBTree, z: RBTreeNode) -> None:
    # p178
    # 只可能破坏: 根结点黑(z为根); 红结点不能有红孩子(父为红).
    y = T.nil
    x = T.root
    while x is not T.nil:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == T.nil:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = Color.Red  # 置为红, 可能违背红黑性质
    rb_insert_fixup(T, z)


def rb_insert_fixup(T: RBTree, z: RBTreeNode) -> None:
    # p178
    # z: 可能违背红黑性质的节点
    while z.p.color == Color.Red:
        # 保持的不变式: z红; z.p若是根, 则z.p黑; 至多一条性质被破坏
        if z.p == z.p.p.left:
            y = z.p.p.right
            if y.color == Color.Red:
                z.p.color = Color.Black
                y.color = Color.Black
                z.p.p.color = Color.Red
                z = z.p.p
            elif z == z.p.right:
                z = z.p
                left_rotate(T, z)
            else:
                z.p.color = Color.Black
                z.p.p.color = Color.Red
                right_rotate(T, z.p.p)
        else:
            y = z.p.p.left
            if y.color == Color.Red:
                z.p.color = Color.Black
                y.color = Color.Black
                z.p.p.color = Color.Red
                z = z.p.p
            elif z == z.p.left:
                z = z.p
                right_rotate(T, z)
            else:
                z.p.color = Color.Black
                z.p.p.color = Color.Red
                left_rotate(T, z.p.p)
    T.root.color = Color.Black


# if __name__ == '__main__':
#     rbt = RBTree()
#     rb_insert(rbt, RBTreeNode(1))
#     rb_insert(rbt, RBTreeNode(2))
#     rb_insert(rbt, RBTreeNode(3))
#     rb_insert(rbt, RBTreeNode(4))
#     rb_insert(rbt, RBTreeNode(5))
#     rb_insert(rbt, RBTreeNode(6))
#     rb_insert(rbt, RBTreeNode(7))
#     rb_insert(rbt, RBTreeNode(8))
#     rb_insert(rbt, RBTreeNode(9))
#     print(rbt)


def rb_transplant(T: RBTree, u: RBTreeNode, v: RBTreeNode) -> None:
    # p183
    # 用v替代u
    if u.p == T.nil:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    v.p = u.p


def tree_minimum(T: RBTree, x: RBTreeNode) -> RBTreeNode:
    # p164
    while x.left != T.nil:
        x = x.left
    return x


def rb_delete(T: RBTree, z: RBTreeNode) -> None:
    # p183
    # 删z
    # x, y可能破坏红黑性质
    # y: 在树中删除的节点或者移至树内的节点
    # x: 移到y的原始位置上
    y = z
    y_original_color = y.color
    if z.left == T.nil:
        x = z.right
        rb_transplant(T, z, z.right)
    elif z.right == T.nil:
        x = z.left
        rb_transplant(T, z, z.left)
    else:
        y = tree_minimum(T, z.right)
        y_original_color = y.color
        x = y.right
        if y.p == z:
            x.p = y
        else:
            rb_transplant(T, y, y.right)
            y.right = z.right
            y.right.p = y
        rb_transplant(T, z, y)
        y.left = z.left
        y.left.p = y
        y.color = z.color
    # y为红色: 红黑性质保持:
    # 1. 黑高不变
    # 2. 不存在相邻红节点
    # 3. y红, 则不为根节点
    if y_original_color == Color.Black:
        rb_delete_fixup(T, x)  # 删了一个黑


def rb_delete_fixup(T: RBTree, x: RBTreeNode) -> None:
    # p185
    # while目标: 将额外的黑色沿树上移, 直到:
    while x != T.root and x.color == Color.Black:
        if x == x.p.left:
            w = x.p.right
            if w.color == Color.Red:
                w.color = Color.Black
                x.p.color = Color.Red
                left_rotate(T, x.p)
                w = x.p.right
            if w.left.color == Color.Black and w.right.color == Color.Black:
                w.color = Color.Red
                x = x.p
            elif w.right.color == Color.Black:
                w.left.color = Color.Black
                w.color = Color.Red
                right_rotate(T, w)
                w = x.p.right
            else:
                w.color = x.p.color
                x.p.color = Color.Black
                w.right.color = Color.Black
                left_rotate(T, x.p)
                x = T.root
        else:
            w = x.p.left
            if w.color == Color.Red:
                w.color = Color.Black
                x.p.color = Color.Red
                right_rotate(T, x.p)
                w = x.p.left
            if w.right.color == Color.Black and w.left.color == Color.Black:
                w.color = Color.Red
                x = x.p
            elif w.left.color == Color.Black:
                w.right.color = Color.Black
                w.color = Color.Red
                left_rotate(T, w)
                w = x.p.left  # 保证一致性
            else:
                w.color = x.p.color
                x.p.color = Color.Black
                w.left.color = Color.Black
                right_rotate(T, x.p)
                x = T.root
    x.color = Color.Black


# if __name__ == '__main__':
#     rbt = RBTree()
#     x1 = RBTreeNode(1)
#     x2 = RBTreeNode(2)
#     x3 = RBTreeNode(3)
#     x4 = RBTreeNode(4)
#     x5 = RBTreeNode(5)
#     x6 = RBTreeNode(6)
#     x7 = RBTreeNode(7)
#     x8 = RBTreeNode(8)
#     x9 = RBTreeNode(9)
#     rb_insert(rbt, x1)
#     rb_insert(rbt, x2)
#     rb_insert(rbt, x3)
#     rb_insert(rbt, x4)
#     rb_insert(rbt, x5)
#     rb_insert(rbt, x6)
#     rb_insert(rbt, x7)
#     rb_insert(rbt, x8)
#     rb_insert(rbt, x9)
#     print(rbt)
#     rb_delete(rbt, x4)
#     print(rbt)

"""
1. insert fix和delete fix的复杂度都为O(logn). 但是旋转至多分别做2次, 3次. 
"""

"""14 数据结构的扩张"""
