# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

def is_palindrome(s: str) -> bool:
    lo, hi = 0, len(s) - 1
    while lo < hi:
        if s[lo] != s[hi]:
            return False
        lo += 1
        hi -= 1
    return True


def reverse_num(x: int) -> int:
    """Ot(LogX) Os(1). 其中Log为Log10"""
    ans = 0
    while x > 0:
        ans *= 10
        ans += x % 10
        x //= 10
    return ans


from math import log10


def gen_palindrome_num(x: int, tag: int):
    # tag:
    # 0: even
    # 1: odd
    # 2: both
    if x == 0:
        return 0

    n = 10 ** int(log10(x))
    b = reverse_num(x)
    if tag == 1:
        x1 = x * n + b % n
        return x1
    elif tag == 0:
        x2 = x * n * 10 + b
        return x2
    else:
        x1 = x * n + b % n
        x2 = x * n * 10 + b
        return x1, x2


if __name__ == '__main__':
    print(gen_palindrome_num(1234, 0))
    print(gen_palindrome_num(1234, 1))
    print(gen_palindrome_num(1234, 2))
