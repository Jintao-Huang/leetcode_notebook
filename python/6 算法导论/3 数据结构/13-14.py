# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

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
    def __init__(self, key: int, color: Color = Color.Black,
                 p: 'RBTreeNode' = None, left: 'RBTreeNode' = None, right: 'RBTreeNode' = None):
        self.key = key
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

"""14 数据结构的扩张(使用红黑树)"""


# 顺序统计树(order-statistic tree)
# O(LogN)确定任意顺序统计量(查找具有给定秩的元素),
#   或确定一个元素的秩(在集合线性序中的位置)


# 覆盖
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


# 覆盖
# 叶节点size=1, nil.size=0
class RBTree:
    def __init__(self, root: RBTreeNode = None, nil: RBTreeNode = None):
        if nil is None:
            nil = RBTreeNode(0, Color.Black, 0)
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


def os_select(x: RBTreeNode, i: int) -> RBTreeNode:
    # p194
    # order statistics. 返回x为根的子树中包含第i小关键字的节点
    r = x.left.size + 1  # rank
    if i == r:
        return x
    elif i < r:
        return os_select(x.left, i)
    else:
        return os_select(x.right, i - r)


def os_rank(T: RBTree, x: RBTreeNode) -> int:
    # p194
    r = x.left.size + 1
    y = x
    while y != T.root:
        if y == y.p.right:
            r += y.p.left.size + 1
        y = y.p
    return r


# 覆盖
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
    y.size = x.size
    x.size = x.left.size + x.right.size + 1


# 覆盖
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
    x.size = y.size
    y.size = y.left.size + y.right.size + 1


# 覆盖
def rb_insert(T: RBTree, z: RBTreeNode) -> None:
    # p178
    # 只可能破坏: 根结点黑(z为根); 红结点不能有红孩子(父为红).
    y = T.nil
    x = T.root
    while x is not T.nil:
        y = x
        x.size += 1
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
    z.size = 1
    rb_insert_fixup(T, z)


# 覆盖
def rb_delete(T: RBTree, z: RBTreeNode) -> None:
    # p183
    # 删z
    # x, y可能破坏红黑性质
    # z: 在树中删除的节点
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
        y.size = z.size
    p = x.p
    while p != T.nil:
        p.size -= 1
        p = p.p
    # y为红色: 红黑性质保持:
    # 1. 黑高不变
    # 2. 不存在相邻红节点
    # 3. y红, 则不为根节点
    if y_original_color == Color.Black:
        rb_delete_fixup(T, x)  # 删了一个黑


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
#     rb_delete(rbt, x5)
#     # [1, 2, 3, 6, 7, 8, 9]
#     print(rbt)
#     print(os_select(rbt.root, 4).key)
#     print(os_select(rbt.root, 2).key)
#     print(os_rank(rbt, x2))


"""p197
1. 红黑树的扩张. 定理14.1
    f是红黑树扩张的属性. 对任意结点x. f的值仅依赖x, x.left, x.right
        (e.g: x.left.f, x.right.f)
    那么可在插入和删除期间对T的所有节点的f进行维护, 时间复杂度不变O(LogN)
"""

# 区间树(interval tree): 对动态集合进行维护的红黑树
#   假设闭区间


from typing import NamedTuple
from collections import namedtuple

Interval = namedtuple("Interval", ["low", "high"])


# if __name__ == '__main__':
# print(Interval(0, 1))


# 覆盖
class RBTreeNode:
    # p193
    def __init__(self, interval: Interval, color: Color = Color.Black, max_: int = 0,
                 p: 'RBTreeNode' = None, left: 'RBTreeNode' = None, right: 'RBTreeNode' = None):
        self.key = interval.low
        self.color = color
        self.itv = interval
        # x.max_ = max(x.itv.high, x.left.max_, x.right.max_)
        self.max_ = max_  # 以x为根的子树中所以区间右端点的最大值
        self.p = p
        self.left = left
        self.right = right


# 覆盖
class RBTree:
    def __init__(self, root: RBTreeNode = None, nil: RBTreeNode = None):
        if nil is None:
            nil = RBTreeNode(Interval(0, 0), Color.Black, 0)
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
                ans.append((n.itv, 'R' if n.color == Color.Red else 'B', n.max_))
                q.append(n.left)
                q.append(n.right)
                if n.left != self.nil or n.right != self.nil:
                    all_None = False
            if all_None:
                break
        while len(ans) > 0 and ans[-1] is None:
            ans.pop()

        return json.dumps(ans)


def overlap(i: Interval, i2: Interval) -> bool:
    if i.low > i2.high or i2.low > i.high:
        return False
    return True


def interval_search(T: RBTree, i: Interval) -> RBTreeNode:
    # p200
    # 没找到返回nil
    x = T.root
    while x != T.nil and not overlap(i, x.itv):
        if x.left != T.nil and x.left.max_ >= i.low:
            x = x.left  # 优先找左边
        else:
            x = x.right
    return x


# 覆盖
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
    y.max_ = x.max_
    x.max_ = max(x.itv.high, x.left.max_, x.right.max_)


# 覆盖
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
    x.max_ = y.max_
    y.max_ = max(y.itv.high, y.left.max_, y.right.max_)


# 覆盖
def rb_insert(T: RBTree, z: RBTreeNode) -> None:
    # p178
    # 只可能破坏: 根结点黑(z为根); 红结点不能有红孩子(父为红).
    y = T.nil
    x = T.root
    while x is not T.nil:
        y = x
        x.max_ = max(x.max_, z.itv.high)
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
    z.max_ = z.itv.high
    rb_insert_fixup(T, z)


# 覆盖
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
        y.max_ = z.max_
    p = x.p
    while p != T.nil:
        max_ = max(p.left.max_, p.right.max_)  # p.itv.high
        if max_ > p.max_:
            p.max_ = max_
        else:
            break
        p = p.p
    # y为红色: 红黑性质保持:
    # 1. 黑高不变
    # 2. 不存在相邻红节点
    # 3. y红, 则不为根节点
    if y_original_color == Color.Black:
        rb_delete_fixup(T, x)  # 删了一个黑

# if __name__ == '__main__':
#     rbt = RBTree()
#     x0 = RBTreeNode(Interval(0, 3))
#     x5 = RBTreeNode(Interval(5, 8))
#     x6 = RBTreeNode(Interval(6, 10))
#     x8 = RBTreeNode(Interval(8, 9))
#     x15 = RBTreeNode(Interval(15, 23))
#     x16 = RBTreeNode(Interval(16, 21))
#     x17 = RBTreeNode(Interval(17, 19))
#     x19 = RBTreeNode(Interval(19, 20))
#     x25 = RBTreeNode(Interval(25, 30))
#     x26 = RBTreeNode(Interval(26, 26))
#     rb_insert(rbt, x0)
#     rb_insert(rbt, x5)
#     rb_insert(rbt, x6)
#     rb_insert(rbt, x8)
#     rb_insert(rbt, x15)
#     rb_insert(rbt, x16)
#     rb_insert(rbt, x17)
#     rb_insert(rbt, x19)
#     rb_insert(rbt, x25)
#     rb_insert(rbt, x26)
#     print(rbt)
#     rb_delete(rbt, x8)
#     print(interval_search(rbt, Interval(22, 25)).itv)
#     print(interval_search(rbt, Interval(11, 14)) == rbt.nil)
#     print(rbt)
