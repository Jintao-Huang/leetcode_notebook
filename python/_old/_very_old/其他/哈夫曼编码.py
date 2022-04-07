# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from typing import Dict, List
import collections


class TreeNode:
    def __init__(self, val, weight, left=None, right=None):
        self.val: str = val
        self.weight: int = weight
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return "TreeNode(['%s', %d])" % (self.val, self.weight)

    def __str__(self) -> str:
        return self.__repr__()


def stat_letter(s: str) -> Dict[str, int]:
    """统计字母. Ot(Len(S))"""
    res: Dict[str, int] = {}
    for c in s:
        if c in res:
            res[c] += 1
        else:
            res[c] = 1
    return res


def bisect_left(forest: List[TreeNode], t: TreeNode) -> int:
    """在forest中找到t合适的插入点以维持有序. Ot(LogN) Os(1)"""
    lo, hi = 0, len(forest)
    while lo < hi:
        mid = (lo + hi) // 2
        if forest[mid].weight > t.weight:
            lo = mid + 1
        else:
            hi = mid  # 等于往左
    return lo


def build_huffman_tree(s: str) -> TreeNode:
    """Ot(N^2)"""
    d: Dict[str, int] = stat_letter(s)
    forest: List[TreeNode] = [TreeNode(k, v) for k, v in d.items()]
    forest.sort(key=lambda tn: -tn.weight)  # TreeNode. 从大到小
    while len(forest) > 1:
        t1 = forest.pop()
        t2 = forest.pop()
        t = TreeNode('^', t1.weight + t2.weight, t1, t2)
        idx = bisect_left(forest, t)
        forest.insert(idx, t)
    return forest[0]


def get_huffman_map(huffman_tree: TreeNode) -> Dict[str, str]:
    """回溯法(0左1右). Ot(N)"""
    res = {}
    prefix = []

    def _get_huffman_map(tn: TreeNode) -> None:
        if tn.val != '^':
            res[tn.val] = "".join(prefix)
            return
        prefix.append('0')
        _get_huffman_map(tn.left)
        prefix[-1] = '1'
        _get_huffman_map(tn.right)

    _get_huffman_map(huffman_tree)
    return res


def text2huffman_code(s: str, huffman_map: Dict[str, str]) -> str:
    """Ot(Len(S))"""
    res = []
    for c in s:
        res.append(huffman_map[c])
    return "".join(res)


def huffman_code2text(s: str, huffman_tree: TreeNode) -> str:
    """Ot(Len(S)). 0左1右"""
    p = huffman_tree
    res = []
    for c in s:
        if c == '0':
            p = p.left
        else:
            p = p.right
        if p.val != '^':
            res.append(p.val)
            p = huffman_tree
    # assert p == huffman_tree, "Code 错误"
    return "".join(res)


def print_tree(root: TreeNode) -> None:
    """广搜 For Debug. Ot(N)"""
    print("Tree: ")
    q = collections.deque([root])
    level = -1
    while len(q) > 0:
        level += 1
        t = []
        finished = True  # 是否结束
        for i in range(len(q)):
            tn: TreeNode = q.popleft()
            t.append(tn)
            if tn is not None:
                q += [tn.left, tn.right]
                finished = False
            else:
                q += [None, None]
        if not finished:
            print("Level %d: %s" % (level, t))
        else:
            return


if __name__ == "__main__":
    s = "aabbbccccd"
    print(s)
    huffman_tree: TreeNode = build_huffman_tree(s)
    huffman_map: Dict[str, str] = get_huffman_map(huffman_tree)
    print(huffman_map)
    hc: str = text2huffman_code(s, huffman_map)
    print(hc)
    text: str = huffman_code2text(hc, huffman_tree)
    print(text)
    print_tree(huffman_tree)
