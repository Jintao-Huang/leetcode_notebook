# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:


class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        sign = 1  # 当前环境
        ops = [1]  # 处理括号外(环境)
        ans = 0
        ord_0 = ord('0')
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            if 0 <= ord(s[i]) - ord_0 <= 9:
                n = 0
                while i < len(s) and 0 <= ord(s[i]) - ord_0 <= 9:
                    n *= 10
                    n += ord(s[i]) - ord_0
                    i += 1
                ans += sign * n
            else:
                if s[i] == '(':
                    ops.append(sign)
                elif s[i] == ')':
                    ops.pop()
                elif s[i] == '+':
                    sign = ops[-1]
                elif s[i] == '-':
                    sign = -ops[-1]
                i += 1
        return ans


# s = "1234"
# print(Solution().calculate(s))
s = "(1+(4+5+2)-3 )+(6+8)"
s = " 2-1 + 2 "
# s = "(4+5+2)"
print(Solution().calculate(s))
