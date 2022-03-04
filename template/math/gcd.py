# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

def gcd(x: int, y: int) -> int:
    """最大公约数. O(1)"""
    while y > 0:
        x, y = y, x % y
    return x


def lcm(x: int, y: int) -> int:
    """O(1)"""
    return x * y // gcd(x, y)


print(lcm(5, 4))  # 20
