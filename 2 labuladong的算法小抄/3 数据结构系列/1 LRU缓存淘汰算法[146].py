# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from collections import deque
from typing import Dict, Optional
from template.data_structure.linked_list import LinkedList, ListNode2
from template.build.call_func import call_func


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}  # type: Dict[int, ListNode2]
        self.q = LinkedList([])

    def _get(self, key: int) -> Optional[ListNode2]:
        n = self.d.get(key, None)
        if n is not None:
            self.q.delete(n)
            n = self.q.insert_before(self.q.head, n.val)
            self.d[key] = n
        return n

    def get(self, key: int) -> int:
        n = self._get(key)
        return -1 if n is None else n.val[1]

    def put(self, key: int, value: int) -> None:
        n = self._get(key)
        if n is None:
            n = self.q.insert_before(self.q.head, [key, value])
            self.d[key] = n
            #
            if len(self.q) > self.capacity:
                n = self.q.head.next
                self.q.delete(n)
                self.d.pop(n.val[0])
        else:
            n.val[1] = value


func = ["LRUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
        "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get",
        "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put",
        "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put",
        "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put",
        "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put",
        "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]
args = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
        [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11],
        [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5],
        [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22],
        [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29],
        [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27], [11, 15],
        [12], [9, 19], [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2],
        [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]

print(call_func(func, args, globals()))
