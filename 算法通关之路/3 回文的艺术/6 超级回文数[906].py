# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from math import sqrt, log10


def valid(s: str) -> bool:
    """Ot(N) Os(1). 其中N=len(s), 即Log10(int(s))."""
    lo, hi = 0, len(s) - 1
    while lo < hi:
        if s[lo] != s[hi]:
            return False
        lo += 1
        hi -= 1
    return True


class Solution:
    r"""暴力. 超时. $Ot((\sqrt{R}-\sqrt{L})LogR)$ Os(1)"""

    def superpalindromesInRange(self, left: str, right: str) -> int:
        s = 0
        for i in range(int(sqrt(int(left))), int(sqrt(int(right))) + 1):
            if valid(str(i)) and valid(str(i ** 2)):
                s += 1

        return s


print(Solution().superpalindromesInRange("4", "1000"))


def reverse_num(x: int) -> int:
    """Ot(LogX) Os(1). 其中Log为Log10"""
    ans = 0
    while x > 0:
        ans *= 10
        ans += x % 10
        x //= 10
    return ans


class Solution2:
    r"""直接构造回文数. Ot(\sqrt[4]{R}Log{R}) Os(1)"""

    def superpalindromesInRange(self, left: str, right: str) -> int:
        left, right = int(left), int(right)
        ans = 0
        for a in range(1, 100000):
            b = reverse_num(a)
            n = 10 ** int(log10(a))  # 10 ** 位数
            x = (a * n + b % n) ** 2  # e.g. 12321 ** 2
            if x > right:
                return ans
            x2 = (a * n * 10 + b) ** 2  # e.g. 123321 ** 2
            if left <= x <= right and valid(str(x)):
                ans += 1
            if left <= x2 <= right and valid(str(x2)):
                ans += 1
        return ans


print(Solution2().superpalindromesInRange("4", "1000"))
