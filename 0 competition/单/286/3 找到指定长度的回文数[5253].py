# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List


def reverse_num(x: int) -> int:
    """Ot(LogX) Os(1). 其中Log为Log10"""
    ans = 0
    while x > 0:
        ans *= 10
        ans += x % 10
        x //= 10
    return ans


class Solution:
    """回文数的生成, 数的限制"""

    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        i2 = (intLength - 1) // 2
        n = 10 ** i2
        ans = []
        for q in queries:
            a = q - 1 + n
            if a >= n * 10:
                ans.append(-1)
                continue
            b = reverse_num(a)
            if intLength % 2 == 1:
                x = a * n + b % n
            else:
                x = a * n * 10 + b
            ans.append(x)
        return ans


queries = [91]
intLength = 3
print(Solution().kthPalindrome(queries, intLength))

queries = [2, 201429812, 8, 520498110, 492711727, 339882032, 462074369, 9, 7, 6]
intLength = 1
print(Solution().kthPalindrome(queries, intLength))
