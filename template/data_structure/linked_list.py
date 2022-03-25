# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

class ListNode2:
    def __init__(self, val: int, prev, next):
        self.val = val
        self.prev = prev  # type: ListNode2
        self.next = next  # type: ListNode2


from typing import List, Union


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

    def is_tail(self, p: ListNode2):
        return p == self.head

    def append(self, x: int) -> None:
        self.insert_before(self.head, x)

    def appendleft(self, x: int) -> None:
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

    def insert_after(self, p: ListNode2, x: int) -> ListNode2:
        """insert x after p"""
        n = ListNode2(x, p, p.next)
        p.next.prev = n
        p.next = n
        self.length += 1
        return n

    def insert_before(self, p: ListNode2, x: int) -> ListNode2:
        """insert x before p"""
        n = ListNode2(x, p.prev, p)
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
        head = self.head
        #
        p = head.next
        ans = []
        while p != head:
            ans.append(p.val)
            p = p.next
        return str(ans)

    def __len__(self) -> int:
        return self.length


class ListNode:
    def __init__(self, val: int, next):
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
