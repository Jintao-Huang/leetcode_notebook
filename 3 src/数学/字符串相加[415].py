# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from typing import List


def nums_add_nums(n1: List[int], n2: List[int]):
    ans = []
    s = 0
    m, n = len(n1), len(n2)
    for i in range(max(m, n)):
        x1 = n1[m - 1 - i] if m - 1 - i >= 0 else 0
        x2 = n2[n - 1 - i] if n - 1 - i >= 0 else 0
        s += x1 + x2
        s, mo = divmod(s, 10)
        ans.append(mo)
    if s > 0:
        ans.append(s)
    ans.reverse()
    return ans


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = [int(x) for x in num1]
        num2 = [int(x) for x in num2]
        ans = nums_add_nums(num1, num2)
        return "".join([str(a) for a in ans])


print(Solution().addStrings("11", "123"))
