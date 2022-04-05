# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from typing import Iterable
from copy import copy

"""
*1. 插入、删除都需要prev
2. tail的变化!!!(appendleft注意len为0的情况, reverse()). 动态方法时
3. 单链表无法实现pop(), 因为不知道prev. 由1得
4. 动态方法时, self.length
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    """head不含头结点"""
    items = []
    p = head
    while p is not None:
        items.append(str(p.val))
        p = p.next
    print("LinkedList([%s])" % ', '.join(items))


class LinkedList:
    """只能存int"""

    def __init__(self, iterable: Iterable = None):
        self.tail = self.head = ListNode(0, None)
        self.length = 0
        if iterable is not None:
            self.extend(iterable)

    def append(self, x: int) -> None:
        """Ot(1) Os(1)"""
        self.tail.next = ListNode(x, None)
        self.tail = self.tail.next
        self.length += 1

    def appendleft(self, x: int) -> None:
        """Ot(1) Os(1)"""
        self.head.next = ListNode(x, self.head.next)
        # 即(连续append时，可用下面的方法)
        # p = self.head.next
        # p = ListNode(x, p)
        # self.head.next = p

        if self.length == 0:
            self.tail = self.tail.next
        self.length += 1

    def pop(self) -> int:
        raise NotImplementedError  # 无法实现Ot(1)

    def popleft(self) -> int:
        if self.length == 0:
            raise IndexError
        p = self.head.next
        self.head.next = p.next
        self.length -= 1
        return p.val

    def clear(self) -> None:
        self.tail = self.head = ListNode(0, None)
        self.length = 0

    def copy(self):
        return copy(self)

    def count(self, x: int) -> int:
        p = self.head.next
        c = 0
        while p is not None:
            if p.val == x:
                c += 1
            p = p.next
        return c

    def extend(self, iterable: Iterable) -> None:
        for x in iterable:
            self.append(x)

    def extendleft(self, iterable: Iterable) -> None:
        for x in iterable:
            self.appendleft(x)

    def insert(self, i: int, x: int) -> None:
        prev = self.head
        # 操作i
        if i < 0:
            i += self.length
        i = min(self.length, max(0, i))
        # 复杂度低，切不用额外操作tail
        if i == self.length:
            return self.append(x)

        while i > 0:
            i -= 1
            prev = prev.next
        prev.next = ListNode(x, prev.next)
        self.length += 1

    def remove(self, value) -> None:
        prev = self.head
        while prev.next is not None:
            p = prev.next
            if p.val == value:
                prev.next = p.next
                self.length -= 1
                return
            else:
                prev = p
        raise ValueError

    def reverse(self) -> None:
        p = self.head.next
        self.tail = p
        self.head.next = None
        while p is not None:
            n = p.next
            p.next = self.head.next
            self.head.next = p
            p = n

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __repr__(self) -> str:
        items = []
        p = self.head.next
        while p is not None:
            items.append(str(p.val))
            p = p.next
        return "LinkedList([%s])" % ', '.join(items)

    def __str__(self) -> str:
        return self.__repr__()

    def __len__(self) -> int:
        return self.length


l = LinkedList()
l.appendleft(1)
l.append(2)
l.appendleft(3)
l.append(4)
l.append(2)
print(l)  # LinkedList([3, 1, 2, 4])
print(l.popleft())
print(l, len(l), l.tail.next)
print(l.count(2))
print(l.count(1))
print(l.count(12))

print("------------------------")
l2 = LinkedList(range(10))
l2.extendleft(range(10))
print(l2, len(l2), l2.tail.next)
print("------------------------")
l3 = LinkedList()
l3.insert(0, 1)
l3.insert(0, 2)
l3.insert(-1, 3)
print(l3, len(l3), l3.tail.next)
l3.reverse()
print(l3, len(l3), l3.tail.next)
l3.remove(1)
print(l3, len(l3), l3.tail.next)


# l3.remove(0)
# print(l3, len(l3))

# l.clear()
# print(l, len(l))


class LinkedList2:
    """只能存int. 只有头结点"""

    def __init__(self):
        self.head = ListNode(0, None)

    def appendleft(self, x: int) -> None:
        """Ot(1) Os(1)"""
        self.head.next = ListNode(x, self.head.next)

    def popleft(self) -> int:
        p = self.head.next
        if p is None:
            raise IndexError
        self.head.next = p.next
        return p.val

    def count(self, x: int) -> int:
        p = self.head.next
        c = 0
        while p is not None:
            if p.val == x:
                c += 1
            p = p.next
        return c

    def extendleft(self, iterable: Iterable) -> None:
        for x in iterable:
            self.appendleft(x)

    def insert(self, i: int, x: int) -> None:
        """i不支持负数"""
        prev = self.head
        while i > 0:
            i -= 1
            if prev is None:
                raise IndexError
            prev = prev.next
        prev.next = ListNode(x, prev.next)

    def remove(self, value) -> None:
        prev = self.head
        while prev.next is not None:
            p = prev.next
            if p.val == value:
                prev.next = p.next
                return
            else:
                prev = p
        raise ValueError

    def reverse(self) -> None:
        p = self.head.next
        self.head.next = None
        while p is not None:
            n = p.next
            p.next = self.head.next
            self.head.next = p
            p = n

    def __repr__(self) -> str:
        items = []
        p = self.head.next
        while p is not None:
            items.append(str(p.val))
            p = p.next
        return "LinkedList([%s])" % ', '.join(items)

    def __str__(self) -> str:
        return self.__repr__()


print("------------------------")
l = LinkedList2()
l.appendleft(1)
l.appendleft(1)
l.appendleft(3)
l.appendleft(4)
print(l)  # LinkedList([3, 1, 2, 4])
print(l.popleft())
print(l.count(2))
print(l.count(1))

print("------------------------")
l.extendleft(range(10))
l2 = LinkedList2()
l2.insert(0, 1)
l2.insert(0, 2)
l2.insert(1, 3)
print(l2)
l2.reverse()
print(l2)
l2.remove(1)
print(l2)
