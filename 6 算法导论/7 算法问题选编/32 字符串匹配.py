# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List

"""32 字符串匹配"""


# T: 文本串, P: 模式串. s: 有效偏移
# 预处理+匹配
# 符号:


# 朴素字符串匹配
# 完全忽略了检测无效s值时获得的文本信息.
def naive_string_matcher(T: str, P: str) -> List[int]:
    # p579
    # 返回s
    n, m = len(T), len(P)
    ans = []
    for s in range(n - m + 1):
        if P == T[s:s + m]:
            ans.append(s)
    return ans


# if __name__ == '__main__':
#     T = "acaabc"
#     P = "aab"
#     print(naive_string_matcher(T, P))

def rabin_karp_matcher(T: List[int], P: List[int], d: int, q: int) -> List[int]:
    # p582
    # d: base number
    # q: 素数
    # 这里使用List[int]代替str进行实验. 用str只需要减去ord('a')或ord('0')即可
    # 也可以利用前缀和思想拓展到求任意S[lo..hi]的哈希. 预处理O(N), 取hash O(1)
    n, m = len(T), len(P)
    h = d ** (m - 1) % q  # 最高位base
    # p: 模式串哈希, t0: s=0时的文本串哈希
    p = 0
    t0 = 0
    # 预处理
    for i in range(m):
        p = (d * p + P[i]) % q
        t0 = (d * t0 + T[i]) % q
    # 匹配
    ans = []
    t = t0
    for s in range(n - m + 1):
        if p == t:
            if P == T[s:s + m]:
                ans.append(s)
        if s < n - m:
            t = (d * (t - T[s] * h) + T[s + m]) % q
    return ans


# if __name__ == '__main__':
#     P = [3, 1, 4, 1, 5]
#     T = [2, 3, 5, 9, 0, 2, 3, 1, 4, 1, 5, 2, 6, 7, 3, 9, 9, 2, 1]
#     d = 10
#     q = 13  # q越大, 越不容易冲突
#     print(rabin_karp_matcher(T, P, d, q))


# 有限自动机

"""p583
1. 有限自动机M: 5元祖(Q, q0, A, Sigma, delta)
    状态的有限集合, 初始状态, 接受状态集合, 输入字母表, 转移函数
"""


def finite_automaton_matcher(T: List[int], delta: List[List[int]]) -> List[int]:
    # p586
    # delta: 转移函数(理解成建好的有限自动机M).
    #   状态i, 输入j. 转移到delta_ij
    # T: 输入文本. 用List代替.
    n = len(T)
    m = len(delta) - 1  # 接受状态
    q = 0  # 状态. 或 匹配的字符数.
    ans = []
    for i in range(n):
        q = delta[q][T[i]]
        if q == m:  # m-1也为结束状态
            ans.append(i - m + 1)
    return ans


# if __name__ == '__main__':
#     # a, b, c
#     delta = [[1, 0, 0], [1, 2, 0], [3, 0, 0], [1, 4, 0],
#              [5, 0, 0], [1, 4, 6], [7, 0, 0], [1, 2, 0]]
#     T = [0, 1, 0, 1, 0, 1, 0, 2, 0, 1, 0]
#     print(finite_automaton_matcher(T, delta))


def ends_with(s: List[int], s2: List[int]) -> bool:
    # 是否 s ends with s2
    n = len(s)
    m = len(s2)
    start = n - m
    for i in range(len(s2)):
        j = start + i
        if s[j] != s2[i]:
            return False
    return True


def compute_transition_function(P: List[int], Sigma: List[int]) -> List[List[int]]:
    # p587
    # 直接根据定义delta[q][a] = sigma[Pq+a]
    #   其中sigma: 辅助函数, sigma(x)是x的后缀, P的最长前缀的长度.
    # 使用定义计算, 复杂度较高. 可改进. 见下
    m = len(P)
    theta = [[0] * len(Sigma) for _ in range(m + 1)]
    for q in range(m + 1):  # 状态
        for c in Sigma:
            k = min(q + 1, m)
            while True:
                # P[:q] + [c]: 对T
                # P[:k]: 对P
                # 若P前缀是当前T的后缀, 减少相同前后缀的比较
                if ends_with(P[:q] + [c], P[:k]):
                    break
                k -= 1
            theta[q][c] = k
    return theta


# if __name__ == '__main__':
#     P = [0, 1, 0, 1, 0, 2, 0]
#     T = [0, 1, 0, 1, 0, 1, 0, 2, 0, 1, 0]
#     Sigma = [0, 1, 2]
#     delta = compute_transition_function(P, Sigma)
#     print(finite_automaton_matcher(T, delta))
#
#     P = [0, 1, 0, 1]
#     T = [0, 1, 0, 1, 0, 1]
#     Sigma = [0, 1]
#     delta = compute_transition_function(P, Sigma)
#     print(finite_automaton_matcher(T, delta))


def kmp_matcher(T: str, P: str, pi: List[int] = None) -> List[int]:
    # p589
    n = len(T)
    m = len(P)
    if pi is None:
        pi = compute_prefix_function(P)
    q = 0  # 匹配的数量/继续匹配的位置
    ans = []
    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = pi[q - 1]
        if P[q] == T[i]:
            q += 1
        if q == m:
            ans.append(i - m + 1)
            q = pi[q - 1]
    return ans


# 与自动机区别:
# 自动机计算转义函数要考虑下一字符
#   kmp的next数组不考虑下一字符
def compute_prefix_function(P: str) -> List[int]:
    # pi[q]: P[:q]的最长相等[真]前后缀(不能等于P[:q])的字符数
    # 考研教科书中定义: P[:q-1]的最长相等[真]前后缀的字符数(+1, 若索引从1开始)
    m = len(P)
    pi = [0] * m
    pi[0] = 0
    k = 0
    for q in range(1, m):
        while k > 0 and P[k] != P[q]:
            k = pi[k - 1]
        if P[k] == P[q]:
            k += 1
        pi[q] = k
    return pi


# if __name__ == '__main__':
#     pi = [0, 0, 1, 2, 3, 0, 1]
#     T = "ababababacacbab"
#     P = "ababaca"
#     print(compute_prefix_function(P))
#     print(kmp_matcher(T, P, pi))


def compute_transition_function2(P: List[int], Sigma: List[int]) -> List[List[int]]:
    # p587
    # 直接根据定义delta[q][a] = sigma[Pq+a]
    #   其中sigma: 辅助函数, sigma(x)是x的后缀, P的最长前缀的长度.
    # 使用定义计算, 复杂度较高. 可改进. 见书
    m = len(P)
    theta = [[0] * len(Sigma) for _ in range(m + 1)]
    pi = compute_prefix_function(P)
    # 第一个
    for c in Sigma:
        if c == P[0]:
            theta[0][c] = 1
        else:
            theta[0][c] = 0
    #
    for q in range(1, m + 1):  # 状态
        for c in Sigma:
            if q == m or P[q] != c:
                theta[q][c] = theta[pi[q - 1]][c]
            elif P[q] == c:
                theta[q][c] = q + 1
    return theta


# if __name__ == '__main__':
#     # P = [0, 1, 0, 1, 0, 2, 0]
#     # T = [0, 1, 0, 1, 0, 1, 0, 2, 0, 1, 0]
#     # Sigma = [0, 1, 2]
#     # delta = compute_transition_function2(P, Sigma)
#     # print(finite_automaton_matcher(T, delta))
#
#     P = [0, 1, 0, 1]
#     T = [0, 1, 0, 1, 0, 1]
#     Sigma = [0, 1]
#     delta = compute_transition_function(P, Sigma)
#     delta2 = compute_transition_function2(P, Sigma)
#     print(delta)
#     print(delta2)
#     print(finite_automaton_matcher(T, delta2))


# 使用考研定义的next数组: 缺点: 不能连续匹配.

def kmp_matcher2(T: str, P: str, pi: List[int]) -> int:
    # p589
    n = len(T)
    m = len(P)
    q = 0  # 匹配的数量/继续匹配的位置
    for i in range(n):
        while q >= 0 and P[q] != T[i]:
            q = pi[q]
        if q == -1 or P[q] == T[i]:
            q += 1
        if q == m:
            return i - m + 1


# 与自动机区别:
# 自动机计算转义函数要考虑下一字符
#   kmp的next数组不考虑下一字符
def compute_prefix_function2(P: str) -> List[int]:
    # pi[q]: P[:q]的最长相等[真]前后缀(不能等于P[:q])的字符数
    # 考研教科书中定义: P[:q-1]的最长相等[真]前后缀的字符数
    m = len(P)
    pi = [0] * m
    pi[0] = -1
    pi[1] = 0
    k = 0
    for q in range(1, m - 1):
        while k >= 0 and P[k] != P[q]:
            k = pi[k]
        if k == -1 or P[k] == P[q]:
            k += 1
        pi[q + 1] = k
    return pi


if __name__ == '__main__':
    P = "abaabcac"
    T = "babaaabaabcac"
    pi = compute_prefix_function(P)
    pi2 = compute_prefix_function2(P)
    print(kmp_matcher(T, P, pi))
    print(kmp_matcher2(T, P, pi2))
    print(pi)
    print(pi2)
