# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import Iterable, Dict, Any


class defaultdict(dict):
    def __init__(self, default_factory, **kwargs):
        self.default_factory = default_factory
        super(defaultdict, self).__init__(kwargs)

    def __missing__(self, key):
        return self.default_factory()


def fromkeys(seq: Iterable[int], value: int = None) -> Dict[int, int]:
    return {x: value for x in seq}


def get(d: Dict[int, int], key: int, default: int = None) -> int:
    if key in d:
        return d[key]
    return default


def setdefault(d: Dict[int, int], key: int, default: int = None) -> int:
    if key in d:
        return d[key]
    d[key] = default
    return default


def pop(d: Dict[int, int], key: int, default: int = None) -> int:
    if key in d:
        x = d[key]
        del d[key]
        return x
    return default


from template.data_structure.linked_list import LinkedList, ListNode2
from typing import Optional, Dict


class OrderedDict:
    def __init__(self, d: Dict[int, int] = None):
        if d is None:
            d = {}
        self.q = LinkedList([(k, v) for k, v in d.items()])
        self.d = {}
        for x in self.q:
            self.d[x[0]] = x  # type: Dict[int, ListNode2]  # key, refer

    def popitem(self, last: bool = True) -> int:
        if last:
            k, v = self.q.pop()
        else:
            k, v = self.q.popleft()
        return self.d.pop(k)

    def move_to_end(self, key: int, last=True) -> None:
        x = self.d[key]
        self.q.delete(x)
        if last:
            self.q.append(x)
        else:
            self.q.appendleft(x)

    def __contains__(self, key: int) -> bool:
        return key in self.d

    def __getitem__(self, key: int) -> int:
        return self.d[key].val[1]

    def __setitem__(self, key: int, value: int):
        if key not in self.d:
            x = ListNode2((key, value))
            self.d[key] = x
            self.q.append(x)
        else:
            self.d[key].val = key, value

    def pop(self, key: int) -> int:
        x = self.d.pop(key)
        self.q.delete(x)
        return x[1]

    def __len__(self):
        return len(self.q)
