# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from enum import Enum
from collections import deque
import json


class Color(Enum):
    Red = 1
    Black = 2


class RBTreeNode:
    # p193
    def __init__(self, key: int, color: Color = Color.Black, size: int = 0,
                 p: 'RBTreeNode' = None, left: 'RBTreeNode' = None, right: 'RBTreeNode' = None):
        self.key = key
        self.color = color
        # x.size = x.left.size + x.right.size + 1
        self.size = size
        self.p = p
        self.left = left
        self.right = right


class RBTree:
    # 红黑树实现
    def __init__(self, root: RBTreeNode = None, nil: RBTreeNode = None):
        if nil is None:
            nil = RBTreeNode(0, Color.Black)
        if root is None:
            root = nil
        self.root = root
        self.nil = nil

    def getitem(self, x: RBTreeNode, i: int) -> RBTreeNode:
        # p194
        # 外部调用时: x为root.
        # order statistics. 返回x为根的子树中包含第i小关键字的节点
        r = x.left.size + 1  # rank
        if i == r:
            return x
        elif i < r:
            return self.getitem(x.left, i)
        else:
            return self.getitem(x.right, i - r)

    def bisect_left(self, x) -> int:
        # p194
        y = self.root
        ans = 0
        while y != self.nil:
            if x <= y.key:
                y = y.left
            else:
                ans += y.left.size + 1
                y = y.right
        return ans

    def bisect_right(self, x) -> int:
        # p194
        y = self.root
        ans = 0
        while y != self.nil:
            if x < y.key:
                y = y.left
            else:
                ans += y.left.size + 1
                y = y.right
        return ans

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
        y.size = x.size
        x.size = x.left.size + x.right.size + 1

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
        x.size = y.size
        y.size = y.left.size + y.right.size + 1

    def rb_insert(self, z: RBTreeNode) -> None:
        # p178
        # 只可能破坏: 根结点黑(z为根); 红结点不能有红孩子(父为红).
        y = self.nil
        x = self.root
        while x is not self.nil:
            y = x
            x.size += 1
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
        z.size = 1
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
            y.size = z.size
        p = x.p
        while p != self.nil:
            p.size -= 1
            p = p.p
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

    def __str__(self):
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
                ans.append((n.key, 'R' if n.color == Color.Red else 'B', n.size))
                q.append(n.left)
                q.append(n.right)
                if n.left != self.nil or n.right != self.nil:
                    all_None = False
            if all_None:
                break
        while len(ans) > 0 and ans[-1] is None:
            ans.pop()

        return json.dumps(ans)


class SortedList:
    def __init__(self, nums=None):
        if nums is None:
            nums = []
        self.rbt = RBTree()
        self.length = 0
        for x in nums:
            self.add(RBTreeNode(x))

    def add(self, n: RBTreeNode):
        if not isinstance(n, RBTreeNode):
            n = RBTreeNode(n)
        self.rbt.rb_insert(n)
        self.length += 1

    def search(self, x) -> RBTreeNode:
        n = self.rbt.search(x)
        if n == self.rbt.nil:
            n = None
        return n

    def remove(self, n: RBTreeNode) -> None:
        if not isinstance(n, RBTreeNode):
            self.search(n)
        self.rbt.rb_delete(n)
        self.length -= 1

    def bisect_left(self, x: int) -> int:
        return self.rbt.bisect_left(x)

    def bisect_right(self, x: int) -> int:
        return self.rbt.bisect_right(x)

    def __len__(self):
        return self.length

    def __getitem__(self, i) -> RBTreeNode:
        return self.rbt.getitem(self.rbt.root, i + 1)

    def __str__(self):
        return str(self.rbt)


if __name__ == '__main__':
    x = SortedList([3, 2, 6, 4])  # [2, 3, 4, 6]
    print(x)
    print(x[1].key)
