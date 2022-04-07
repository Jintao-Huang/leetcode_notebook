# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


### 列出100以内的质数
"""不使用函数"""
l = []
for i in range(2, 101):
    """质数只有1和自身两个公因数"""
    for j in range(2, i):  # j: (1, 自身) 即[2, 自身-1]
        if i % j == 0:
            break
    else:
        l.append(i)
print(l)
"""用函数"""


def is_prime(x: int) -> bool:
    """若x是质数返回True; 否则返回False"""

    for j in range(2, x):
        if x % j == 0:
            return False
    else:
        return True


primeList = []
for i in range(2, 101):
    if is_prime(i):
        primeList.append(i)
print(primeList)

### 计算第1000个菲波那切数列
"""fibonacci"""
x, y = 1, 1
for _ in range(3, 1001):
    x, y = y, x + y

print(y)

"""fibonacci生成器"""


def fibonacci(n=None):
    """fibonacci(n: int = None) -> generator

    返回可以生成n个 fibonacci 数列的生成器，如果n=None则无限生成"""
    x, y = 1, 1  # x前 y后
    i = 0
    while True:
        if n is not None and i >= n:
            return
        i += 1
        yield x
        x, y = y, x + y


for i in fibonacci(10):
    print(i)
"""递归写法"""


def fibonacci(n):
    if n == 1 or n == 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))

### 一元二次方程
from math import sqrt


def quadratic(a, b, c):
    """quadratic(a: float, b: float, c: float) -> tuple[float]

    返回ax^2 + bx + c = 0的两个根(x1, x2)
    如果只有一个根，返回(x,)
    如果没有根，返回()"""

    delta = (b ** 2 - 4 * a * c)  # 三角形
    mean = -b / (2 * a)  # 对称轴的x坐标
    if delta < 0:
        return ()

    elif delta == 0:
        return mean,
    else:
        return mean + sqrt(delta) / (2 * a), mean - sqrt(delta) / (2 * a)


def quadratic2(a, b, c):
    """quadratic(a: float, b: float, c: float) -> tuple[float, float]

    返回ax^2 + bx + c = 0的两个根(mean, 未根号部分)
    例如 x^2 - 4x + 6 = 0  返回(2.0, -2.0)
    """

    b, c = b / a, c / a  # 全部除去a
    mean = -b / 2  # 对称轴的x坐标
    u2 = mean ** 2 - c  # b ^ 2 / (4 * a ^ 2) - c / a
    return mean, u2


print(quadratic(1, 6, 4))  # (-0.7639320225002102, -5.23606797749979)
print(quadratic2(1, 6, 4))  # (-3.0, 5.0)
print(quadratic2(1, -4, 6))  # (2.0, -2.0)


### 对身份证号进行验证


def check_id_num(id_num):
    """check_id_num(id_num: str) -> bool

    检查id_num；通过返回True，不通过返回False

    算法：sum-i[0, 17](id_num[i]*W[i]) % 11 = 1
    W[i] = 2**(17-i) % 11
    """
    sum_ = 0
    # 前17位
    for i in range(len(id_num) - 1):
        w = 2 ** (17 - i) % 11
        sum_ += int(id_num[i]) * w
    # 最后1位
    # w = 2 ** (17 - 17) % 11 = 1
    if id_num[17] == 'x':
        sum_ += 10
    else:
        sum_ += int(id_num[17])

    if sum_ % 11 == 1:
        return True
    else:
        return False


## 经典


### 计算某一天到某一天经过的天数
start = (2008, 1, 1)
end = (2009, 2, 29)

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year: int) -> bool:
    """判断是否是闰年"""
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def is_legal_date(year: int, month: int, day: int) -> bool:
    """判断日期是否合法"""
    if year < 1 or month < 1 or month > 12 or day < 1:
        return False
    if is_leap_year(year) and month == 2:
        if day > 29:
            return False
    else:
        if day > months[month - 1]:
            return False
    return True


def days_from0(year: int, month: int, day: int) -> int:
    """返回(year, month, day) - 元年(1, 1, 1) 的天数"""
    if not is_legal_date(year, month, day):
        print("Error: %d-%d-%d not a legal date" % (year, month, day))
        exit(0)

    year_diff, month_diff, day_diff = year - 1, month - 1, day - 1  # 得到差
    # year_day + month_day + day_day + ?1
    return (year_diff * 365 + year_diff // 4 - year_diff // 100 + year_diff // 400) + sum(
        months[:month_diff]) + day_diff + (is_leap_year(year) and month >= 3)


print(days_from0(*end) - days_from0(*start))


### 最大公因数


def gcd(x, y):
    """gcd(x: int, y: int) -> int

    Returns gcd(greatest common divisor) of x and y.\n
    实现算法: 辗转相除法"""

    while y != 0:
        x, y = y, x % y
    return x


print(gcd(30021, 234))  # 9


### 汉诺塔问题

# 汉诺塔问题：
# 有三根杆子A，B，C。A杆上有N个(N>1)穿孔圆盘，盘的尺寸由下到上依次变小。
# 要求按下列规则将所有圆盘移至C杆：
# 1. 每次只能移动一个圆盘。
# 2. 大盘不能叠在小盘上面。
#
# 提示：可将圆盘临时置于B杆，也可将从A杆移出的圆盘重新移回A杆，但都必须遵循上述两条规则。
# 问：如何移？最少要移动多少次？


def hanoi(n, from_="A", to_="C", tmp_="B"):
    """hanoi(n: int, from_: Any = "A", to_: Any = "C", tmp_: Any = "B") -> List[tuple[from_, to_]]

    解决汉诺塔问题：将n个圆盘从 `from_` 移动到 `to_`，临时盘为 `tmp_`

    返回一个List，里面是一个个二元组(from_, to_)，存放着每一步的操作"""
    opera_list = []

    def __hanoi(n, from_, to_, tmp_):
        if n == 0:
            return
        __hanoi(n - 1, from_, tmp_, to_)
        opera_list.append((from_, to_))
        __hanoi(n - 1, tmp_, to_, from_)

    __hanoi(n, from_, to_, tmp_)
    return opera_list


# 步数 = 2 ** N - 1
opera_list = hanoi(6)
print(len(opera_list))  # 63
print(opera_list)
# [('A', 'B'), ('A', 'C'), ('B', 'C'), ('A', 'B'), ('C', 'A'), ('C', 'B'), ('A', 'B'), ('A', 'C'), ('B', 'C'),
# ('B', 'A'), ('C', 'A'), ('B', 'C'), ('A', 'B'), ('A', 'C'), ('B', 'C'), ('A', 'B'), ('C', 'A'), ('C', 'B'),
# ('A', 'B'), ('C', 'A'), ('B', 'C'), ('B', 'A'), ('C', 'A'), ('C', 'B'), ('A', 'B'), ('A', 'C'), ('B', 'C'),
# ('A', 'B'), ('C', 'A'), ('C', 'B'), ('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'A'), ('C', 'A'), ('B', 'C'),
# ('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'A'), ('C', 'A'), ('C', 'B'), ('A', 'B'), ('C', 'A'), ('B', 'C'),
# ('B', 'A'), ('C', 'A'), ('B', 'C'), ('A', 'B'), ('A', 'C'), ('B', 'C'), ('A', 'B'), ('C', 'A'), ('C', 'B'),
# ('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'A'), ('C', 'A'), ('B', 'C'), ('A', 'B'), ('A', 'C'), ('B', 'C')]
