# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from template.data_structure.union_find import UnionFind


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        mapper = {c: i for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        ne = []
        for e in equations:
            a, b = mapper[e[0]], mapper[e[3]]
            if e[1] == '=':
                uf.union(a, b)
            else:
                ne.append(e)
        for e in ne:
            a, b = mapper[e[0]], mapper[e[3]]
            if uf.find(a) == uf.find(b):
                return False
        return True
