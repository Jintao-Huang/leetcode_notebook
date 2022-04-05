# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.Q = [0] * (k + 1)  # type: List[int]
        self.head = 0  # 含
        self.tail = 0  # 不含

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.Q[self.tail] = value
        if self.tail == len(self.Q) - 1:
            self.tail = 0
        else:
            self.tail += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == len(self.Q) - 1:
            self.head = 0
        else:
            self.head += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.Q[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.Q[self.tail - 1]

    def isEmpty(self) -> bool:
        return self.tail == self.head

    def isFull(self) -> bool:
        return (self.tail - self.head) % len(self.Q) == self.k
