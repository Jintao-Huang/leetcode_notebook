# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List

"""10 基本数据结构"""


# 栈
class Stack:
    # p129
    def __init__(self):
        self.S = []  # type: List[int]

    def stack_empty(self) -> bool:
        if len(self.S) == 0:
            return True
        else:
            return False

    def push(self, x: int) -> None:
        self.S.append(x)

    def pop(self) -> int:
        if self.stack_empty():
            raise ValueError("underflow")
        else:
            return self.S.pop()


# if __name__ == '__main__':
#     s = Stack()
#     print(s.stack_empty())
#     s.push(2)
#     print(s.stack_empty())
#     s.push(1)
#     print(s.pop())
#     print(s.pop())
#     # print(s.pop())  # underflow

# 队列
class Queue:
    # p130
    def __init__(self, n: int):
        # n: 容量
        self.n = n
        self.Q = [0] * (n + 1)  # type: List[int]
        self.head = 0
        self.tail = 0

    def enqueue(self, x: int) -> None:
        if self.queue_full():
            raise ValueError("overflow")
        else:
            self.Q[self.tail] = x
            if self.tail == len(self.Q) - 1:
                self.tail = 0
            else:
                self.tail += 1

    def dequeue(self) -> int:
        if self.queue_empty():
            raise ValueError("underflow")
        else:
            x = self.Q[self.head]
            if self.head == len(self.Q) - 1:
                self.head = 0
            else:
                self.head += 1
            return x

    def queue_empty(self) -> bool:
        return self.tail == self.head

    def queue_full(self) -> bool:
        return (self.tail - self.head) % len(self.Q) == self.n


# if __name__ == '__main__':
#     q = Queue(3)
#     q.enqueue(10)
#     q.enqueue(11)
#     print(q.dequeue())
#     q.enqueue(12)
#     q.enqueue(13)
#     # q.enqueue(14)  # overflow
#     print(q.dequeue())
#     print(q.dequeue())
#     print(q.dequeue())
#     # print(q.dequeue())  # underflow


# 链表
class ListNode:
    def __init__(self, key: int,
                 prev: 'ListNode' = None, next_: 'ListNode' = None):
        self.key = key
        self.prev = prev
        self.next = next_


class LinkedList:
    # p132
    # 不使用头节点
    def __init__(self):
        self.head = None

    def list_search(self, k: int) -> ListNode:
        x = self.head  # type: ListNode
        while x is not None and x.key != k:
            x = x.next
        return x

    def list_insert(self, x: ListNode) -> None:
        # 加在最前面. 对加在最后面无能为力. 但可以用LinkedList2实现
        x.next = self.head
        if self.head is not None:
            self.head.prev = x
        self.head = x
        x.prev = None

    def list_delete(self, x: ListNode) -> None:
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next is not None:
            x.next.prev = x.prev

    def __str__(self) -> str:
        # just for test
        ans = []
        x = self.head
        while x is not None:
            ans.append(x.key)
            x = x.next
        return str(ans)


class LinkedList2:
    # p133
    # 哨兵
    def __init__(self):
        self.nil = ListNode(0)
        self.nil.prev = self.nil
        self.nil.next = self.nil

    def list_search(self, k: int) -> ListNode:
        x = self.nil.next  # type: ListNode
        while x != self.nil and x.key != k:
            x = x.next
        return x

    def list_insert(self, x: ListNode) -> None:
        #
        x.next = self.nil.next
        self.nil.next.prev = x
        self.nil.next = x
        x.prev = self.nil

    def list_delete(self, x: ListNode) -> None:
        x.prev.next = x.next
        x.next.prev = x.prev

    def __str__(self) -> str:
        # just for test
        ans = []
        x = self.nil.next
        while x != self.nil:
            ans.append(x.key)
            x = x.next
        return str(ans)


# if __name__ == '__main__':
#     ll = LinkedList()
#     a, b, c = ListNode(3), ListNode(2), ListNode(1)
#     ll.list_insert(a)
#     ll.list_insert(b)
#     ll.list_insert(c)
#     print(ll.list_search(1).key)
#     print(ll)
#     ll.list_delete(a)
#     ll.list_delete(c)
#     ll.list_delete(b)
#     print(ll)
#     print(ll.list_search(1))
#     #
#     ll = LinkedList2()
#     a, b, c = ListNode(3), ListNode(2), ListNode(1)
#     ll.list_insert(a)
#     ll.list_insert(b)
#     ll.list_insert(c)
#     print(ll.list_search(1).key)
#     print(ll)
#     ll.list_delete(a)
#     ll.list_delete(c)
#     ll.list_delete(b)
#     print(ll)
#     print(ll.list_search(1) == ll.nil)

from typing import Optional


# 对象的分配与释放
class StaticList:
    # p136
    def __init__(self, n: int):
        # n: 容量
        self.n = n
        self.next_ = [i + 1 for i in range(n + 1)]  # one for head
        self.next_[-1] = -1
        self.free = 1
        #
        self.key = [None] * (n + 1)  # type: List[Optional[int]]  # None: 未分配
        self.prev = [0] * (n + 1)
        #
        self.nil = 0
        self.next_[0] = 0  # prev=0
        self.key[0] = 0

    def allocate_object(self, k: int) -> int:
        if self.free == -1:
            raise ValueError("out of space")
        else:
            x = self.free
            self.free = self.next_[x]
            self.key[x] = k
            return x  # idx

    def free_object(self, x) -> None:
        # 这里不检测是否free. 可以增加self.free_array判断.
        if self.key[x] is None:
            raise ValueError("already has been freed")
        else:
            self.next_[x] = self.free
            self.free = x
            self.key[x] = None

    def list_search(self, k: int) -> int:
        x = self.next_[self.nil]  # idx
        while x != self.nil and self.key[x] != k:
            x = self.next_[x]
        return x

    def list_insert(self, x: int) -> None:
        # 返回idx
        self.next_[x] = self.next_[self.nil]
        self.prev[self.next_[self.nil]] = x
        self.next_[self.nil] = x
        self.prev[x] = self.nil

    def list_delete(self, x: int) -> None:
        self.next_[self.prev[x]] = self.next_[x]
        self.prev[self.next_[x]] = self.prev[x]

    def __str__(self):
        # just for test
        ans = []
        x = self.next_[self.nil]
        while x != self.nil:
            ans.append(self.key[x])
            x = self.next_[x]
        return str(ans)


if __name__ == '__main__':
    ll = StaticList(3)
    a, b, c = ll.allocate_object(3), ll.allocate_object(2), ll.allocate_object(1)
    ll.list_insert(a)
    ll.list_insert(b)
    ll.list_insert(c)
    print(ll.key[ll.list_search(1)])
    print(ll)
    ll.list_delete(a)
    ll.list_delete(c)
    ll.list_delete(b)
    print(ll)
    print(ll.list_search(1) == ll.nil)
    # ll.allocate_object(4)  # out of space
    ll.free_object(a)
    ll.free_object(b)
    ll.free_object(c)
    # ll.free_object(c)  # already has been freed
    ll.allocate_object(3)
    ll.allocate_object(2)
    ll.allocate_object(1)
    # ll.allocate_object(1)  # out of space

"""
1. p138. 有根树的左孩子右兄弟表示(分支无限制的有根树)
"""
