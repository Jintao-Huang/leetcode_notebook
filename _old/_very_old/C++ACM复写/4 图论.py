# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List

"""并查集"""


class UF_Node:
    def __init__(self, father: int = -1, height: int = 0):
        """根的height才有意义"""
        self.father: int = father
        self.height: int = height

    def __repr__(self):
        return "UF_Node([P: %d, H: %d])" % (self.father, self.height)

    def __str__(self):
        return self.__repr__()


def find_root(uf_set: List[UF_Node], x: int) -> int:
    """Ot(1)"""
    node: UF_Node = uf_set[x]
    if node.father == -1:
        return x
    else:
        node.father = find_root(uf_set, node.father)
        return node.father


def union_uf_set(uf_set: List[UF_Node], a: int, b: int) -> bool:
    """如果a, b同根，则返回False. 否则合并并返回True. O(1)"""
    root_a: int = find_root(uf_set, a)
    root_b: int = find_root(uf_set, b)
    if root_a == root_b:
        return False
    node_ra: UF_Node = uf_set[root_a]
    node_rb: UF_Node = uf_set[root_b]

    if node_ra.height > node_rb.height:
        node_rb.father = root_a
    elif node_ra.height < node_rb.height:
        node_ra.father = root_b
    else:
        node_rb.father = root_a
        node_ra.height += 1
    return True


N = 100
uf_set = [UF_Node() for i in range(N)]
print(find_root(uf_set, 10))
print(union_uf_set(uf_set, 1, 2))
print(union_uf_set(uf_set, 1, 3))
print(union_uf_set(uf_set, 2, 3))
print(union_uf_set(uf_set, 0, 3))
print(uf_set[:5])

"""is_tree()略"""

"""最小生成树"""

"""最短路径算法"""

