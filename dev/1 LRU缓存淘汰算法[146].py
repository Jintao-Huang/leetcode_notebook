# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import Dict, Optional
from template.data_structure.lru_cache import LRUCache as _LRUCache
from template.build.call_func import call_func


class LRUCache(_LRUCache):
    def get(self, key: int) -> int:
        v = self._get(key)
        return -1 if v is None else v


func = ["LRUCache","put","put","get","put","put","get"]
args =[[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]

print(call_func(func, args, globals()))
