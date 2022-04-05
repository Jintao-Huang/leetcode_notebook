# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

class ListNode:
    def __init__(self, key: int,
                 prev: 'ListNode' = None, next_: 'ListNode' = None):
        self.key = key
        self.prev = prev
        self.next = next_


class MyLinkedList:

    def __init__(self):
        self.nil = ListNode(0)
        self.nil.prev = self.nil
        self.nil.next = self.nil

    def get(self, index: int) -> int:
        x = self.nil.next
        while x != self.nil:
            if index == 0:
                return x.key
            x = x.next
            index -= 1
        return -1

    def insert_after(self, x: ListNode, x2: ListNode) -> None:
        # insert x after x2
        x.next = x2.next
        x2.next.prev = x
        x2.next = x
        x.prev = x2

    def addAtHead(self, val: int) -> None:
        x = ListNode(val)
        self.insert_after(x, self.nil)

    def addAtTail(self, val: int) -> None:
        x = ListNode(val)
        self.insert_after(x, self.nil.prev)

    def delete(self, x: ListNode) -> None:
        x.prev.next = x.next
        x.next.prev = x.prev

    def addAtIndex(self, index: int, val: int) -> None:
        x2 = ListNode(val)
        if index == 0:
            self.insert_after(x2, self.nil)

        x = self.nil.next
        index -= 1
        while x != self.nil:
            if index == 0:
                self.insert_after(x2, x)
                return
            x = x.next
            index -= 1

    def deleteAtIndex(self, index: int) -> None:
        x = self.nil.next
        while x != self.nil:
            if index == 0:
                self.delete(x)
                return
            x = x.next
            index -= 1

    def __str__(self) -> str:
        # just for test
        ans = []
        x = self.nil.next
        while x != self.nil:
            ans.append(x.key)
            x = x.next
        return str(ans)


from template.build.call_func import call_func

print(call_func(
    ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "__str__", "get", "deleteAtIndex", "get", "__str__"]
    , [[], [1], [3], [1, 2], [], [1], [1], [1], []], globals()))
