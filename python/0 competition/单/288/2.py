# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List


class Solution:
    def minimizeResult(self, expression: str) -> str:
        num1, num2 = expression.split('+')  # type: str, str
        ans = int(1e9)
        lo, hi = 0, 0
        for i in range(0, len(num1)):  # 加法含
            for j in range(1, len(num2) + 1):
                if i != 0:
                    x1 = int(num1[:i])
                else:
                    x1 = 1
                if j != len(num2):
                    x2 = int(num2[j:])
                else:
                    x2 = 1
                x = (int(num1[i:]) + int(num2[:j])) * x1 * x2
                if x < ans:
                    ans = x
                    lo = i
                    hi = j
        num1 = num1[:lo] + '(' + num1[lo:]
        num2 = num2[:hi] + ')' + num2[hi:]
        return num1 + '+' + num2


print(Solution().minimizeResult("247+38"))
print(Solution().minimizeResult("12+34"))
print(Solution().minimizeResult("999+999"))
