# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

class MinStack:
    def __init__(self):
        self.s = []

    def push(self, val: int) -> None:
        if len(self.s) > 0:
            m = min(self.s[-1][1], val)
        else:
            m = val

        self.s.append((val, m))

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]
