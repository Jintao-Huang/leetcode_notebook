# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List
from template.utils.palindrome import gen_palindrome_num


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
            x, x2 = gen_palindrome_num(a)
            if intLength % 2 == 1:
                ans.append(x)
            else:
                ans.append(x2)
        return ans


queries = [91]
intLength = 3
print(Solution().kthPalindrome(queries, intLength))

queries = [2, 201429812, 8, 520498110, 492711727, 339882032, 462074369, 9, 7, 6]
intLength = 1
print(Solution().kthPalindrome(queries, intLength))
