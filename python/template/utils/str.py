# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

# class Solution:
#     def kmp(self, s: str, t: str) -> int:
#         # S < T
#         m, n = len(s), len(t)
#         if m == 0 or m > n:
#             return 0
#         ans = 0
#         # next: 利用最长相同前后缀进行加速, 前缀匹配, 后缀一定也匹配.
#         next_ = [0] * (m + 1)
#         next_[0] = -1
#         lo = -1
#         for hi in range(m):
#             if lo == -1 or s[lo] == s[hi]:
#                 pass
#
