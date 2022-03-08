# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

class ListNode:
    def __init__(self, val: int, prev, next):
        self.val = val
        self.prev = prev
        self.next = next


from typing import List


class LinkedList:
    """双向循环链表"""

    def __init__(self, nums: List[int]):
        head = ListNode(0, None, None)
        head.next, head.prev = head, head
        #
        self.head = head

        for x in nums:
            self.append(x)

    def append(self, x: int) -> None:
        self.insert_before(self.head, x
                           )

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

    def insert_after(self, p: ListNode, x) -> None:
        """insert x after p"""
        n = ListNode(x, p, p.next)
        p.next.prev = n
        p.next = n

    def insert_before(self, p: ListNode, x) -> None:
        """insert x before p"""
        n = ListNode(x, p.prev, p)
        p.prev.next = n
        p.prev = n

    def delete(self, p: ListNode) -> None:
        """delete p"""
        p.next.prev = p.prev
        p.prev.next = p.next

    def __str__(self) -> str:
        head = self.head
        #
        p = head.next
        ans = []
        while p != head:
            ans.append(p.val)
            p = p.next
        return str(ans)


if __name__ == '__main__':
    l = LinkedList([1, 2, 3, 4, 5])
    print(l)
    l.pop()
    l.popleft()
    l.appendleft(100)
    print(l)