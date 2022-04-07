# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from collections import OrderedDict
# from template.utils.dict import OrderedDict
from typing import Optional, Dict


class LRUCache:
    def __init__(self, capacity: int):
        self.d = OrderedDict()
        self.cap = capacity

    def _get(self, key: int) -> Optional[int]:
        if key in self.d:
            self.d.move_to_end(key)
            return self.d[key]
        else:
            return None

    def put(self, key: int, value: int) -> None:
        v = self._get(key)
        if v is None:
            self.d[key] = value
            #
            if len(self.d) > self.cap:
                self.d.popitem(last=False)
        else:
            self.d[key] = value
