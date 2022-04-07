# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from enum import Enum


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


from typing import Optional


class RBTree:
    # 红黑树实现
    def __init__(self, root: RBTreeNode = None, nil: RBTreeNode = None):
        if nil is None:
            nil = RBTreeNode(0, Color.Black)
        if root is None:
            root = nil
        self.root = root
        self.nil = nil

    def left_rotate(self, x: RBTreeNode) -> None:
        # p177
        # 假设x.right不为空
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def right_rotate(self, y: RBTreeNode) -> None:
        # 假设x.left不为空
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.p = y
        x.p = y.p
        if y.p == self.nil:
            self.root = x
        elif y == y.p.left:
            y.p.left = x
        else:
            y.p.right = x
        x.right = y
        y.p = x

    def rb_insert(self, z: RBTreeNode) -> None:
        # p178
        # 只可能破坏: 根结点黑(z为根); 红结点不能有红孩子(父为红).
        y = self.nil
        x = self.root
        while x is not self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = Color.Red  # 置为红, 可能违背红黑性质
        self.rb_insert_fixup(z)

    def rb_insert_fixup(self, z: RBTreeNode) -> None:
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
                    self.left_rotate(z)
                else:
                    z.p.color = Color.Black
                    z.p.p.color = Color.Red
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == Color.Red:
                    z.p.color = Color.Black
                    y.color = Color.Black
                    z.p.p.color = Color.Red
                    z = z.p.p
                elif z == z.p.left:
                    z = z.p
                    self.right_rotate(z)
                else:
                    z.p.color = Color.Black
                    z.p.p.color = Color.Red
                    self.left_rotate(z.p.p)
        self.root.color = Color.Black

    def rb_transplant(self, u: RBTreeNode, v: RBTreeNode) -> None:
        # p183
        # 用v替代u
        if u.p == self.nil:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def tree_minimum(self, x: RBTreeNode) -> RBTreeNode:
        # p164
        while x.left != self.nil:
            x = x.left
        return x

    def rb_delete(self, z: RBTreeNode) -> None:
        # p183
        # 删z
        # x, y可能破坏红黑性质
        # y: 在树中删除的节点或者移至树内的节点
        # x: 移到y的原始位置上
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.rb_transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        # y为红色: 红黑性质保持:
        # 1. 黑高不变
        # 2. 不存在相邻红节点
        # 3. y红, 则不为根节点
        if y_original_color == Color.Black:
            self.rb_delete_fixup(x)  # 删了一个黑

    def rb_delete_fixup(self, x: RBTreeNode) -> None:
        # p185
        # while目标: 将额外的黑色沿树上移, 直到:
        while x != self.root and x.color == Color.Black:
            if x == x.p.left:
                w = x.p.right
                if w.color == Color.Red:
                    w.color = Color.Black
                    x.p.color = Color.Red
                    self.left_rotate(x.p)
                    w = x.p.right
                if w.left.color == Color.Black and w.right.color == Color.Black:
                    w.color = Color.Red
                    x = x.p
                elif w.right.color == Color.Black:
                    w.left.color = Color.Black
                    w.color = Color.Red
                    self.right_rotate(w)
                    w = x.p.right
                else:
                    w.color = x.p.color
                    x.p.color = Color.Black
                    w.right.color = Color.Black
                    self.left_rotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.color == Color.Red:
                    w.color = Color.Black
                    x.p.color = Color.Red
                    self.right_rotate(x.p)
                    w = x.p.left
                if w.right.color == Color.Black and w.left.color == Color.Black:
                    w.color = Color.Red
                    x = x.p
                elif w.left.color == Color.Black:
                    w.right.color = Color.Black
                    w.color = Color.Red
                    self.left_rotate(w)
                    w = x.p.left  # 保证一致性
                else:
                    w.color = x.p.color
                    x.p.color = Color.Black
                    w.left.color = Color.Black
                    self.right_rotate(x.p)
                    x = self.root
        x.color = Color.Black

    def search(self, k: int) -> RBTreeNode:
        # p163
        x = self.root
        while x != self.nil and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x
