# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

# 0: (), \0\0
# 1: 算前
# 2: 不算
# -1: 不可能
# pri['+']['-']: sop[-1]: '+', s[i]: '-'
m = {
    '+': 0, '-': 1, '*': 2, '/': 3, '(': 4, ')': 5, '\0': 6
}
pri = [
    [1, 1, 2, 2, 2, 1, 1],
    [1, 1, 2, 2, 2, 1, 1],
    [1, 1, 1, 1, 2, 1, 1],
    [1, 1, 1, 1, 2, 1, 1],
    [2, 2, 2, 2, 2, 0, -1],
    [-1, -1, -1, -1, -1, -1, -1],
    [2, 2, 2, 2, 2, -1, 0]
]


class Solution:
    def calculate(self, s: str) -> int:
        s += '\0'
        #
        sop, sn = [m['\0']], []  # opr, nums
        ord_0 = ord('0')
        i = 0
        while len(sop) > 0:
            if s[i] == ' ':
                i += 1
                continue
            #
            c = ord(s[i]) - ord_0
            if 0 <= c <= 9:
                n = 0
                while 0 <= c <= 9:
                    n *= 10
                    n += c
                    i += 1
                    c = ord(s[i]) - ord_0
                sn.append(n)
            else:
                op1 = sop[-1]
                op2 = m[s[i]]
                p = pri[op1][op2]
                if p == 0:
                    sop.pop()
                    i += 1
                elif p == 2:
                    sop.append(op2)
                    i += 1
                else:
                    sop.pop()
                    n2 = sn.pop()
                    n1 = sn.pop()
                    if op1 == m['+']:
                        sn.append(n1 + n2)
                    elif op1 == m['-']:
                        sn.append(n1 - n2)
                    elif op1 == m['*']:
                        sn.append(n1 * n2)
                    else:
                        sn.append(n1 // n2)
        return sn[-1] if len(sn) > 0 else 0


# s = "1234"
# print(Solution().calculate(s))
s = "(1+(4+5+2)-3 )+(6+8)"
# s = "(4+5+2)"
s = " 3+2*2 "
print(Solution().calculate(s))
