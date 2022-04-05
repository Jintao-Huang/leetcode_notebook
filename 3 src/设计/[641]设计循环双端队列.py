# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.Q = [0] * (k + 1)  # type: List[int]
        self.head = 0  # 含
        self.tail = 0  # 不含

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.head == len(self.Q) - 1:
            self.head = 0
        else:
            self.head -= 1
        self.Q[self.head] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.Q[self.tail] = value
        if self.tail == len(self.Q) - 1:
            self.tail = 0
        else:
            self.tail += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == len(self.Q) - 1:
            self.head = 0
        else:
            self.head += 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.tail == len(self.Q) - 1:
            self.tail = 0
        else:
            self.tail -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.Q[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.Q[self.tail - 1]

    def isEmpty(self) -> bool:
        return self.tail == self.head

    def isFull(self) -> bool:
        return (self.tail - self.head) % len(self.Q) == self.k


from template.build.call_func import call_func

print(call_func(
    ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast",
     "insertFront", "getFront"]
    , [[3], [1], [2], [3], [4], [], [], [], [4], []], globals()))
