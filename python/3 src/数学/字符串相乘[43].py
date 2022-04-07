# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List


def nums_mul_int(nums: List[int], x2: int) -> List[int]:
    ans = []
    s = 0
    for x in reversed(nums):
        s += x * x2
        s, mo = divmod(s, 10)
        ans.append(mo)
    while s > 0:
        s, mo = divmod(s, 10)
        ans.append(mo)
    ans.reverse()
    return ans


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


def nums_mul_nums(n1: List[int], n2: List[int]) -> List[int]:
    ans = []
    for x1 in n1:
        if len(ans) > 0:
            ans.append(0)  # *10
        z = nums_mul_int(n2, x1)
        ans = nums_add_nums(ans, z)
    return ans


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0':
            num1 = ''
        if num2 == '0':
            num2 = ''

        num1 = [int(x) for x in num1]
        num2 = [int(x) for x in num2]
        ans = nums_mul_nums(num1, num2)
        if len(ans) == 0:
            ans.append(0)
        return "".join([str(a) for a in ans])


print(Solution().multiply("9133", "0"))
