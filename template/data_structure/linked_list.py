# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from typing import List, Union


class ListNode2:
    def __init__(self, val: int, prev=None, next=None):
        self.val = val
        self.prev = prev  # type: ListNode2
        self.next = next  # type: ListNode2


class LinkedList:
    """双向循环链表"""

    def __init__(self, nums: List[int]):
        head = ListNode2(0, None, None)
        head.next, head.prev = head, head
        self.length = 0
        #
        self.head = head

        for x in nums:
            self.append(x)

    def append(self, x: Union[int, ListNode2]) -> None:
        self.insert_before(self.head, x)

    def appendleft(self, x: Union[int, ListNode2]) -> None:
        self.insert_after(self.head, x)

    def pop(self) -> int:
        p = self.head.prev
        x = p.val
        self.delete(p)
        return x

    def popleft(self) -> int:
        p = self.head.next
        x = p.val
        self.delete(p)
        return x

    def insert_after(self, p: ListNode2, x: Union[int, ListNode2]) -> ListNode2:
        """insert x after p"""
        if not isinstance(x, ListNode2):
            n = ListNode2(x, p, p.next)
        else:
            n = x
            n.prev = p
            n.next = p.next
        p.next.prev = n
        p.next = n
        self.length += 1
        return n

    def insert_before(self, p: ListNode2, x: Union[int, ListNode2]) -> ListNode2:
        """insert x before p"""
        if not isinstance(x, ListNode2):
            n = ListNode2(x, p.prev, p)
        else:
            n = x
            n.prev = p.prev
            n.next = p
        p.prev.next = n
        p.prev = n
        self.length += 1
        return n

    def delete(self, p: ListNode2) -> None:
        """delete p"""
        p.next.prev = p.prev
        p.prev.next = p.next
        self.length -= 1

    def __str__(self) -> str:
        p = self.head.next
        ans = []
        while p != self.head:
            ans.append(p.val)
            p = p.next
        return str(ans)

    def __len__(self) -> int:
        return self.length

    def iter_list(self):
        p = self.head.next
        while p != self.head:
            yield p
            p = p.next

    def __iter__(self):
        return self.iter_list()


class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next  # type: ListNode


class ForwardList:
    def __init__(self, nums: List[int]):
        self.head = None
        self.length = 0

        for x in reversed(nums):
            self.appendleft(x)

    def appendleft(self, x: int) -> None:
        self.head = ListNode(x, self.head)
        self.length += 1

    def popleft(self) -> int:
        x = self.head.val
        self.head = self.head.next
        self.length -= 1
        return x

    def __str__(self) -> str:
        head = self.head
        #
        p = head
        ans = []
        while p is not None:
            ans.append(p.val)
            p = p.next
        return str(ans)

    def __len__(self) -> int:
        return self.length


if __name__ == '__main__':
    l = LinkedList([1, 2, 3, 4, 5])
    print(l)
    l.pop()
    l.popleft()
    l.appendleft(100)
    print(l)
    #
    l = ForwardList([1, 2, 3, 4, 5])
    print(l)
    l.popleft()
    l.appendleft(100)
    print(l)
