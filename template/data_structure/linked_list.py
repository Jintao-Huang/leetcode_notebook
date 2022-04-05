# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from typing import List, Union


class ListNode2:
    def __init__(self, val: int, prev: 'ListNode2' = None, next: 'ListNode2' = None):
        self.val = val
        self.prev = prev  # type: ListNode2
        self.next = next  # type: ListNode2


class LinkedList:
    """双向循环链表"""

    def __init__(self, nums: List[int]):
        self.nil = ListNode2(0)
        self.nil.prev = self.nil
        self.nil.next = self.nil
        self.length = 0
        #
        for x in nums:
            self.append(x)

    def search(self, k: int) -> ListNode2:
        x = self.nil.next  # type: ListNode2
        while x != self.nil and x.val != k:
            x = x.next
        return x

    def append(self, x: Union[int, ListNode2]) -> None:
        if not isinstance(x, ListNode2):
            x = ListNode2(x)
        self.insert_after(x, self.nil.prev)

    def appendleft(self, x: Union[int, ListNode2]) -> None:
        if not isinstance(x, ListNode2):
            x = ListNode2(x)
        self.insert_after(x, self.nil)

    def pop(self) -> int:
        p = self.nil.prev
        if p == self.nil:
            raise ValueError("list empty")
        x = p.val
        self.delete(p)
        return x

    def popleft(self) -> int:
        p = self.nil.next
        if p == self.nil:
            raise ValueError("list empty")
        x = p.val
        self.delete(p)
        return x

    def insert_after(self, p: ListNode2, p2: ListNode2) -> None:
        """insert p after p2"""
        p.next = p2.next
        p2.next.prev = p
        p2.next = p
        p.prev = p2
        self.length += 1

    def delete(self, p: ListNode2) -> None:
        """delete p"""
        p.next.prev = p.prev
        p.prev.next = p.next
        self.length -= 1

    def __str__(self) -> str:
        # just for test
        ans = []
        x = self.nil.next
        while x != self.nil:
            ans.append(x.val)
            x = x.next
        return str(ans)

    def __len__(self) -> int:
        return self.length

    def iter_list(self):
        p = self.nil.next
        while p != self.nil:
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
