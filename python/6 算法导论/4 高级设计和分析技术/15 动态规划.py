# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from typing import List

"""15 动态规划"""


# 最优化问题; 最优子结构(子问题独立, 并可以组成原问题)

# 钢条切割

def cut_rod(p: List[int], n: int) -> int:
    # p206
    # p[i]: 长度i+1的价格.
    if n == 0:
        return 0
    INF = int(1e9)
    q = -INF
    for i in range(n):
        q = max(q, p[i] + cut_rod(p, n - i - 1))
    return q


INF = int(1e9)


def memoized_cut_rod(p: List[int], n: int) -> int:
    # p207
    r = [-INF] * (n + 1)
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p: List[int], n: int, r: List[int]) -> int:
    # p207
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -INF
        for i in range(n):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i - 1, r))
    r[n] = q
    return q


def bottom_up_cut_rod(p: List[int], n: int) -> int:
    # p208
    r = [0] * (n + 1)
    for j in range(1, n + 1):
        q = -INF
        for i in range(j):
            q = max(q, p[i] + r[j - i - 1])
        r[j] = q
    return r[n]


from typing import Tuple


def extended_bottom_up_cut_rod(p: List[int], n: int) -> Tuple[List[int], List[int]]:
    # p209
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    for j in range(1, n + 1):
        q = -INF
        q2 = 0
        for i in range(j):
            a = p[i] + r[j - i - 1]
            if q < a:
                q = a
                q2 = i + 1
        r[j] = q
        s[j] = q2
    return r, s


def print_cut_rod_solution(s: List[int], n: int) -> List[int]:
    # p210
    ans = []
    while n > 0:
        ans.append(s[n])
        n -= s[n]
    return ans


# if __name__ == '__main__':
#     p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
#     print(cut_rod(p, 4))
#     print(memoized_cut_rod(p, 4))
#     print(bottom_up_cut_rod(p, 4))
#     r, s = extended_bottom_up_cut_rod(p, 10)
#     print(print_cut_rod_solution(s, 4), r[4])
#     print(print_cut_rod_solution(s, 10), r[10])
#     print(print_cut_rod_solution(s, 7), r[7])


# 矩阵链乘法
def matrix_multiply(A: List[List[int]], B: List[List[int]]) \
        -> List[List[int]]:
    # p211
    if len(A[0]) != len(B):
        raise ValueError("incompatible dimensions")
    n = len(A)
    m = len(B[0])
    l = len(B)
    C = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            C[i][j] = 0
            for k in range(l):
                C[i][j] += A[i][k] * B[k][j]
    return C


def compute_bracket_scheme_nums(n: int) -> int:
    # p211
    P = [0] * (n + 1)
    P[1] = 1  #
    for i in range(2, n + 1):
        q = 0
        for j in range(1, i):
            q += P[j] * P[i - j]
        P[i] = q
    return P[n]


# from math import factorial
# if __name__ == '__main__':
#     A = [[1, 2], [3, 4]]
#     B = [[4, 3], [2, 1]]
#     print(matrix_multiply(A, B))
#     print(compute_bracket_scheme_nums(3))
#     n = 10
#     print(compute_bracket_scheme_nums(n))
#     print(factorial(2 * n - 2) // factorial(n - 1) ** 2 // n)  # 卡特兰数


def matrix_chain_order(p: List[int]) -> Tuple[List[List[int]], List[List[int]]]:
    # p214
    n = len(p) - 1  # 矩阵数
    m = [[0] * n for _ in range(n)]  # m[i,i]=0
    s = [[0] * n for _ in range(n)]
    for l in range(2, n + 1):  # 链长
        for i in range(n - l + 1):  # [i..j]
            j = i + l - 1
            m[i][j] = INF
            # 选择
            for k in range(i, j):  # 分点
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s


def print_optimal_parens(s: List[List[int]], i: int, j: int, ans: List[str]) -> None:
    # p215
    if i == j:
        ans.append("A%d" % i)
    else:
        ans.append("(")
        print_optimal_parens(s, i, s[i][j], ans)
        print_optimal_parens(s, s[i][j] + 1, j, ans)
        ans.append(")")


# if __name__ == '__main__':
#     p = [30, 35, 15, 5, 10, 20, 25]
#     m, s = matrix_chain_order(p)
#     ans = []
#     print(m[0][len(p) - 2])
#     print_optimal_parens(s, 0, len(p) - 2, ans)
#     print("".join(ans))


"""p216 动态规划原理
1. 最优子结构: 一个问题的最优解包含其子问题的最优解
    即: 一个问题最优, 其子问题一定最优
2. 重叠子问题: 递归算法反复求解相同的子问题
    相对的: 分治方法求解的问题通常在递归的每一步都生成全新的子问题
====
3. 重构最优解. 表s的使用. 
"""


# 动态规划的多项式复杂度并不影响 背包问题是NPC问题. 我们只是利用了其重叠子问题的性质.

def recursive_matrix_chain(p: List[int], i: int, j: int) -> int:
    # p219
    if i == j:
        return 0
    ans = INF
    for k in range(i, j):
        q = recursive_matrix_chain(p, i, k) + \
            recursive_matrix_chain(p, k + 1, j) + \
            p[i] * p[k + 1] * p[j + 1]
        if q < ans:
            ans = q
    return ans


def memoized_matrix_chain(p: List[int]) -> int:
    # p221
    n = len(p) - 1
    m = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            m[i][j] = INF
    return lookup_chain(m, p, 0, n - 1)


def lookup_chain(m: List[List[int]], p: List[int], i: int, j: int) -> int:
    # p221
    if m[i][j] < INF:
        return m[i][j]
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i, j):
            q = recursive_matrix_chain(p, i, k) + \
                recursive_matrix_chain(p, k + 1, j) + \
                p[i] * p[k + 1] * p[j + 1]
            if q < m[i][j]:
                m[i][j] = q
    return m[i][j]


# if __name__ == '__main__':
#     p = [30, 35, 15, 5, 10, 20, 25]
#     print(recursive_matrix_chain(p, 0, len(p) - 2))
#     print(memoized_matrix_chain(p))


# 最长公共子序列

def LCS_length(X: str, Y: str) -> Tuple[List[List[int]], List[List[int]]]:
    # p224
    m = len(X)
    n = len(Y)
    # 0: i+1, j
    # 1: i, j+1
    # 2: i+1, j+1
    b = [[0] * n for _ in range(m)]
    c = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        c[i][0] = 0
    for j in range(n + 1):
        c[0][j] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # i,j for c
            im, jm = i - 1, j - 1
            if X[im] == Y[jm]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[im][jm] = 2
            elif c[i - 1][j] >= c[i][j - 1]:  # >
                c[i][j] = c[i - 1][j]
                b[im][jm] = 0
            else:
                c[i][j] = c[i][j - 1]
                b[im][jm] = 1
    return c, b


def print_LCS(b: List[List[int]], X: str, i: int, j: int, ans: List[str]) -> None:
    # p225
    if i < 0 or j < 0:
        return
    if b[i][j] == 0:
        print_LCS(b, X, i - 1, j, ans)
    elif b[i][j] == 1:
        print_LCS(b, X, i, j - 1, ans)
    else:
        print_LCS(b, X, i - 1, j - 1, ans)
        ans.append(X[i])


# if __name__ == '__main__':
#     X = "BDCABA"
#     Y = "ABCBDAB"
#     c, b = LCS_length(X, Y)
#     print(c[len(X)][len(Y)])
#     ans = []
#     print_LCS(b, X, len(X) - 1, len(Y) - 1, ans)
#     print("".join(ans))


# 状态压缩. p226. 空间变线性, 但重构困难.


# 最优二叉搜索树
#   我们希望频繁词出现在靠近根的位置.
#   给定出现频率, 组织二叉搜索树
#   最优二叉树(哈夫曼树)(见贪心): 需要编码表: 单词 -> 01码. 与此问题不同.
#   二叉搜索树不需要编码表, 是有序的


# 知道每个关键字和伪关键字的搜索概率, 所以可以确定其搜索的期望代价
def optimal_BST(p: List[float], q: List[float]) -> Tuple[List[List[float]], List[List[int]]]:
    # p229
    # p: n个关键字, q: n+1个伪关键字
    # e[i,j]: pi-1..pj-1的最优二叉树一次搜索的期望代价. 我们希望计算e[1,n]
    #   期望代价=sum((depth+1)*pi + (depth+1)*qi)
    # w[i,j]: pi-1..pj-1的子树的所有概率之和
    # root[i-1,j-1]: 保存pi-1..pj-1的根节点kr-1的下标r-1
    n = len(p)
    INF = float("inf")
    # e[i:i-1]: 表示不含关键字, 含q[i-1]. e[i:i]表示q[i-1], p[i-1], q[i]
    e = [[0.] * (n + 1) for _ in range(n + 2)]
    w = [[0.] * (n + 1) for _ in range(n + 2)]
    root = [[0] * n for _ in range(n)]
    for i in range(1, n + 2):
        im = i - 1
        e[i][im] = q[im]
        w[i][im] = q[im]
    for l in range(n):  # 长度
        for i in range(1, n - l + 1):
            j = i + l
            im, jm = i - 1, j - 1  # for p, root
            e[i][j] = INF
            w[i][j] = w[i][j - 1] + p[jm] + q[j]
            for r in range(i, j + 1):
                rm = r - 1
                t = e[i][r - 1] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[im][jm] = rm
    return e, root


# 知道每个关键字和伪关键字的搜索概率, 所以可以确定其搜索的期望代价
def optimal_BST2(p: List[float], q: List[float]) -> Tuple[List[List[float]], List[List[int]]]:
    # p229
    # p: n个关键字, q: n+1个伪关键字
    # e[i,j]: pi..pj-1的最优二叉树一次搜索的期望代价. 我们希望计算e[1,n]
    #   期望代价=sum((depth+1)*pi + (depth+1)*qi)
    # w[i,j]: pi..pj-1的子树的所有概率之和
    # root[i,j-1]: 保存pi..pj-1的根节点kr的下标r
    n = len(p)
    INF = float("inf")
    # e[i,i]: 表示不含关键字, 含q[i]. e[i,i+1]表示q[i], p[i], q[i+1]
    e = [[0.] * (n + 1) for _ in range(n + 1)]
    w = [[0.] * (n + 1) for _ in range(n + 1)]
    root = [[0] * n for _ in range(n)]
    for i in range(n + 1):
        e[i][i] = q[i]
        w[i][i] = q[i]
    for l in range(1, n + 1):  # 长度
        for i in range(n - l + 1):
            j = i + l
            jm = j - 1  # for p, root
            e[i][j] = INF
            w[i][j] = w[i][j - 1] + p[jm] + q[j]
            for r in range(i, j):
                t = e[i][r] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][jm] = r
    return e, root


def print_optimal_BST(root: List[List[int]], i: int, j: int, ans: List[str]) -> None:
    # p215
    if i == j:
        ans.append("p%d" % i)
    else:
        r = root[i][j]
        if i <= r - 1:
            ans.append("(")
            print_optimal_BST(root, i, r - 1, ans)
            ans.append(")")
        ans.append("p%d" % r)
        if r + 1 <= j:
            ans.append("(")
            print_optimal_BST(root, r + 1, j, ans)
            ans.append(")")


# if __name__ == '__main__':
#     p = [0.15, 0.1, 0.05, 0.1, 0.2]
#     q = [0.05, 0.1, 0.05, 0.05, 0.05, 0.1]
#     e, root = optimal_BST(p, q)
#     e2, root2 = optimal_BST2(p, q)
#     print(e, root)
#     print(e[1][len(p)])
#     print(e2[0][len(p)])
#     #
#     ans = []
#     print_optimal_BST(root, 0, len(p) - 1, ans)  # 这不是红黑树, 只是二叉搜索树
#     print("".join(ans))
#     ans = []
#     print_optimal_BST(root2, 0, len(p) - 1, ans)  # 这不是红黑树, 只是二叉搜索树
#     print("".join(ans))

"""p236
1. 动态规划分类
    如果一动态规划表格大小O(N^t), 每个表项依赖其他O(N^e)个表项, 称为tD/eD
    e.g: 15.2：2D/1D, 15.4: 2D/0D
"""
