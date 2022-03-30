# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from typing import List

NestedInteger = List


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nl = nestedList
        self.has = True
        self.l = list(self.dfs(self.nl))
        self.i = 0

    def dfs(self, nl):
        # C: len(nl)
        for i in range(len(nl)):
            if nl[i].isInteger():
                yield nl[i]
            else:
                yield from self.dfs(nl[i].getList())

    def next(self) -> int:
        x = self.l[self.i]
        self.i += 1
        return x

    def hasNext(self) -> bool:
        return self.i < len(self.l)


l = [[1, 1], 2, [1, 1]]
ni = NestedIterator(l)
res = []
while ni.hasNext():
    res.append(ni.next())
print(res)
