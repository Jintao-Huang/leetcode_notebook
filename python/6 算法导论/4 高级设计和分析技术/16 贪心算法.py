# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from typing import List, Tuple

"""16 贪心算法"""

# 局部最优选择

# 活动选择问题
#   选出最大的互相兼容的活动集合
# 半开区间


INF = int(1e9)


# 动态规划版本
def dp_activity_selector(s: List[int], f: List[int]) -> Tuple[List[List[int]], List[List[int]]]:
    # c[i][j]; max(c[i][k] + c[k][j] + 1), k in range(0, n)
    n = len(s)
    # c[i][j]: f[i-1]结束, s[j]开始. 之间的选择数. i in [0..n], j in [0..n]
    c = [[0] * (n + 1) for _ in range(n + 1)]
    # m[i][j-1]: i..j-1的划分点
    m = [[-1] * n for _ in range(n)]  # -1分不了

    for i in range(n + 1):
        c[i][i] = 0

    for l in range(1, n + 1):
        for i in range(n - l + 1):
            j = i + l
            im, jm = i - 1, j - 1
            c[i][j] = 0
            for k in range(i, j):  # f[k], s[k]
                if (i <= 0 or f[im] <= s[k]) and (j >= n or f[k] <= s[j]):
                    q = c[i][k] + c[k + 1][j] + 1
                    if q > c[i][j]:
                        c[i][j] = q
                        m[i][jm] = k
    return c, m


def print_activity_selector(m: List[List[int]], i: int, j: int, ans: List[int]) -> None:
    if i >= j or m[i][j] == -1:
        return

    k = m[i][j]
    print_activity_selector(m, i, k - 1, ans)
    ans.append(k)
    print_activity_selector(m, k + 1, j, ans)


# 贪心选择: 选这样一个活动, 选出后, 剩下资源应能被尽可能多其他任务使用
#   选择: 最早结束的活动


def recursive_activity_selector(s: List[int], f: List[int], k: int, ans: List[int]) -> None:
    # p239
    n = len(s)
    # find the first activity in Sk. to finish
    m = k + 1
    while m < n and s[m] < f[k]:
        m += 1
    if m < n:
        ans.append(m)
        recursive_activity_selector(s, f, m, ans)


def greedy_activity_selector(s: List[int], f: List[int]) -> List[int]:
    # p241
    n = len(s)
    ans = [0]
    k = 0
    for m in range(1, n):
        if s[m] >= f[k]:
            ans.append(m)
            k = m
    return ans


# if __name__ == '__main__':
#     s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
#     f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
#     # s, f服从一种顺序.
#     c, m = dp_activity_selector(s, f)
#     print(c[0][len(s)])
#     ans = []
#     print_activity_selector(m ,0, len(s) - 1, ans)
#     print(ans)
#
#     ans = [0]
#     recursive_activity_selector(s, f, 0, ans)
#     print(ans)
#     print(greedy_activity_selector(s, f))

"""p242 贪心与动态规划的关系
1. 最优子结构性质. 
2. 贪心选择性质(局部全局). (只剩一个子问题)
"""

# 01背包: 对每个商品, 要么完整拿走, 要么留下.
# 分数背包问题
# 贪心能求分数, 不能求01


"""p245 赫夫曼编码
1. 作用: 压缩数据
2. 名词: 定长/变长码字, 前缀码(码字的前缀不可能是其他码字)
"""

# 构建赫夫曼编码
#   正确性证明依赖于贪心选择性质和最优子结构

from heapq import heapify, heappush, heappop


class TreeNode:
    def __init__(self, val: str, freq: int,
                 left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.freq = freq
        self.left = left
        self.right = right


# 无法用动态规划解, 但存在最优子结构.
def huffman(C: str, freq: List[int]) -> TreeNode:
    # p247
    n = len(C)
    F = [(f, i, TreeNode(c, f)) for i, f, c in zip(range(n), freq, C)]
    heapify(F)
    for _ in range(n - 1):
        _, i, x = heappop(F)
        y = heappop(F)[2]  # type: TreeNode
        z = TreeNode('', x.freq + y.freq, x, y)
        heappush(F, (z.freq, i, z))
    return F[0][2]


import json

from typing import Optional
from collections import deque


def tree_to_str(root: Optional[TreeNode]) -> str:
    if root is None:
        return "[]"

    ans = []
    q = deque([root])
    while len(q) > 0:
        all_None = True
        for i in range(len(q)):
            n = q.popleft()
            if n is None:
                ans.append(None)
                continue
            ans.append((n.val, n.freq))
            q.append(n.left)
            q.append(n.right)
            if n.left or n.right:
                all_None = False
        if all_None:
            break
    while len(ans) > 0 and ans[-1] is None:
        ans.pop()

    return json.dumps(ans)


# if __name__ == '__main__':
#     C = "fecbda"
#     freq = [5, 9, 12, 13, 16, 45]
#     r = huffman(C, freq)
#     print(tree_to_str(r))


"""p250 拟阵 M(S, I) 满足. ???
1. S有限, I非空(空集一定属于). I: Set[Set[int]]. 独立子集的集群
2. 遗传性: 大属于, 小一定属于
3. 交换性: 大小属于, 大加一个到小, 小仍属于
======
1. 拟阵中所有最大独立子集具有相同大小
2. greedy(). 略
    最小生成树: 依次取最小边, 如果加入后无环(符合独立集性质), 就加入, 否则丢弃. 只到边数符合要求.
"""

# d: 截止时间
# w: 惩罚
# 略


if __name__ == '__main__':
    d = [4, 2, 4, 3, 1, 4, 6]
    w = [70, 60, 50, 40, 30, 20, 10]
