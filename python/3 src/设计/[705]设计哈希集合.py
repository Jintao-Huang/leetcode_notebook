# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

# prime
# 11
# 101
# 1009
# 10007
# int(1e5)+3
# int(1e6)+3
#
# int(1e7)+19
# int(1e8)+7
# int(1e9)+7
#
# int(1e16)+61
# int(1e17)+3
# int(1e18)+3

class MyHashSet:

    def hash_func(self, k: int):
        return k % self.p

    def __init__(self):
        self.p = 10007
        self.T = [[]] * self.p

    def add(self, key: int) -> None:
        ll = self.T[self.hash_func(key)]
        for k in ll:
            if k == key:
                return
        ll.append(key)

    def remove(self, key: int) -> None:
        ll = self.T[self.hash_func(key)]
        for i in range(len(ll)):
            k = ll[i]
            if k == key:
                ll.pop(i)
                return

    def contains(self, key: int) -> bool:
        ll = self.T[self.hash_func(key)]
        for k in ll:
            if k == key:
                return True
        return False


###

from template.data_structure.rb_tree import RBTree, RBTreeNode


class MyHashSet2:
    def __init__(self):
        self.rbt = RBTree()

    def add(self, key: int) -> None:
        n = self.rbt.search(key)
        if n == self.rbt.nil:
            self.rbt.rb_insert(RBTreeNode(key))

    def remove(self, key: int) -> None:
        n = self.rbt.search(key)
        if n != self.rbt.nil:
            self.rbt.rb_delete(n)

    def contains(self, key: int) -> bool:
        n = self.rbt.search(key)
        return n != self.rbt.nil
