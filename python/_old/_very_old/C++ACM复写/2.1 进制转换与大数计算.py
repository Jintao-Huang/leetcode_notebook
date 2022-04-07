# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from typing import Tuple, Sequence

"""1. 进制转换"""

ORD_0 = ord('0')
ORD_a = ord('a')
ORD_A = ord('A')


def char2int(c: str):
    """参数条件: Len(s) = 1. Ot(1)"""
    ord_c = ord(c.lower())
    if ORD_0 <= ord_c < ORD_0 + 10:
        x = ord_c - ORD_0
    else:
        x = ord_c - ORD_a + 10
    return x


print(char2int('f'))
print(char2int('F'))
print(char2int('0'))
"""
15
15
0
"""

"""int -> char
1. STRING 哈希法
2. ASCII法
"""


def int2char(x: int) -> str:
    """Ot(1)"""
    return chr(x + ORD_0) if x < 10 else chr(x - 10 + ORD_A)


print(int2char(0))
print(int2char(15))
print(int2char(35))
"""
0
F
Z
"""

"""e.g. 11 -> '1011' """


def int2str(x: int, base: int = 10) -> str:
    """参数条件: x > 0. base属于[0, 36). Ot(Len(Res))"""
    res = []  # 栈
    while x > 0:
        res.append(int2char(x % base))
        x //= base
    return "".join(reversed(res))


print(int2str(0, 2))
print(int2str(11, 2))
"""

1011
"""

"""e.g. '1101' -> 11"""

"""思考
1. 一直乘倍数、一直乘res
"""


def str2int(s: str, base: int = 10) -> int:
    """参数条件: s和base合法. Ot(Len(S))"""
    res = 0
    for c in s:
        res *= base
        res += char2int(c)
    return res


print(str2int('1011', 2))
print(str2int('f', 16))

"""
11
15
"""

"""2. 大数运算"""

""" e.g. '9999' + '9999' = '19998' """


def str_add_int(s: str, x: int) -> str:
    """Ot(Len(Rew))"""
    i = len(s) - 1
    carry = x
    res = []  # 栈
    while i >= 0 or carry > 0:
        x2 = char2int(s[i]) if i >= 0 else 0  # Ot(1)
        carry += x2
        res.append(int2char(carry % 10))  # Ot(1)
        carry //= 10
        i -= 1

    return "".join(reversed(res))


print(str_add_int('9999', 99999))
print(str_add_int('9999', 999))
print(str_add_int('9999', 0))


def str_add_str(s1: str, s2: str) -> str:
    """Ot(Len(Res))"""
    i, j = len(s1) - 1, len(s2) - 1
    carry = 0
    res = []  # 栈
    while i >= 0 or j >= 0 or carry > 0:
        x1 = char2int(s1[i]) if i >= 0 else 0  # Ot(1)
        x2 = char2int(s2[j]) if j >= 0 else 0
        carry += x1 + x2
        res.append(int2char(carry % 10))  # Ot(1)
        carry //= 10
        i -= 1
        j -= 1

    return "".join(reversed(res))


print(str_add_str('9999', '99999'))
print(str_add_str('9999', '999'))
print(str_add_str('9999', ''))
"""
109998
10998
9999
"""

""" e.g '9999' * 9 = '89991' """


def str_mul_int(s: str, x: int) -> str:
    """Ot(Len(Res))"""
    i = len(s) - 1
    carry = 0
    res = []  # 栈
    while i >= 0 or carry > 0:  # !
        x2 = char2int(s[i]) if i >= 0 else 0
        carry += x2 * x
        res.append(int2char(carry % 10))  # Ot(1)
        carry //= 10
        i -= 1

    return "".join(reversed(res))


print(str_mul_int('9999', 9))  # 89991


def str_mul_str(s1: str, s2: str) -> str:
    """Ot(Len(S1)Len(S2))"""
    d = {}
    res = ""
    for i in range(len(s2)):
        res = str_mul_int(res, 10)  # O(Len(Res))
        x = char2int(s2[i])
        if x in d:
            s = d[x]
        else:
            s = str_mul_int(s1, x)  # O(Len(s1))
            d[x] = s
        res = str_add_str(res, s)  # O(Len(res) + Len(s))
    return res


print(str_mul_str("9999999999999999999999999", "99999999999999999999999"))
"""
999999999999999999999989900000000000000000000001
"""

DivMod = Tuple[int, int]  # Div, Mod


def get_start_pos(s: Sequence) -> int:
    """将先导0去掉. Ot(1)"""
    for i in range(len(s)):
        if s[i] != '0':
            return i
    else:
        return len(s)


s = "00001"
print(s[get_start_pos(s):])  # 1


def str_divmod_int(s: str, x: int):
    """%3_Ot(N), %2_Ot(1)可以用特殊办法做. Ot(Len(DIV))"""
    remainder = 0
    div = []
    for i in range(len(s)):
        remainder *= 10
        remainder += char2int(s[i])
        div.append(int2char(remainder // x))
        remainder %= x

    return "".join(div[get_start_pos(div):]), remainder


print(str_divmod_int("1234", 2))
print(str_divmod_int("1234", 3))


def big10_to_2(s: str, base: int) -> str:
    """十进制转二进制. Ot(Len(s) * Len(Res))"""
    res = []  # 栈
    while len(s) > 0:
        s, mod = str_divmod_int(s, base)  # Ot(Len(s))
        res.append(int2char(mod))
    return "".join(reversed(res))


def big2_to_10(s: str, base: int) -> str:
    """二进制转十进制. Ot(Len(s) * Len(Res))"""
    res = ""
    for i in range(len(s)):
        res = str_mul_int(res, base)  # Ot(Len(s))
        res = str_add_int(res, char2int(s[i]))
    return "".join(reversed(res))


print(big10_to_2('11', 2))  # 1011
