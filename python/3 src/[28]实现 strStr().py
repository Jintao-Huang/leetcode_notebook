# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from typing import List


def kmp_matcher(T: str, P: str, pi: List[int]) -> int:
    # p589
    n = len(T)
    m = len(P)
    q = 0  # 匹配的数量/继续匹配的位置
    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = pi[q - 1]
        if P[q] == T[i]:
            q += 1
        if q == m:
            return i - m + 1
    return -1


# 与自动机区别:
# 自动机计算转义函数要考虑下一字符
#   kmp的next数组不考虑下一字符
def compute_prefix_function(P: str) -> List[int]:
    # pi[q]: P[:q]的最长相等[真]前后缀(不能等于P[:q])的字符数
    # 考研教科书中定义: P[:q-1]的最长相等[真]前后缀的字符数(+1, 若索引从1开始)
    m = len(P)
    pi = [0] * m
    # pi[0] = 0
    # pi_v[0] = 0
    k = 0
    for q in range(1, m):
        while k > 0 and P[k] != P[q]:
            k = pi[k - 1]
        if P[k] == P[q]:
            k += 1
        pi[q] = k
    pi_v = pi.copy()
    # pi: 利用错误的节点的前后缀的信息
    pi_v[0] = 0  # 利用错误的当前结点的信息
    for k in range(2, m):
        km = k - 1
        if P[k] == P[pi[km]] and pi[km] > 0:
            pi_v[km] = pi_v[pi[km] - 1]
        else:
            pi_v[km] = pi[km]
    return pi_v


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pi = compute_prefix_function(needle)
        print(pi)
        pi = [0, 1, 0, 0, 1, 3]
        return kmp_matcher(haystack, needle, pi)


class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


print(Solution().strStr("aabaaabaab",
                        "aabaab"))
