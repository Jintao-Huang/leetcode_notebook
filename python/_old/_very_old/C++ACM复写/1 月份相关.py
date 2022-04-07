# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from typing import Tuple


def is_leap_year(year: int) -> bool:
    """Ot(1)"""
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


N_M_DAYS = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
N_Y_DAYS = 0


def check_leap_year(year: int) -> None:
    """Ot(1)"""
    global N_M_DAYS, N_Y_DAYS
    if is_leap_year(year):
        N_M_DAYS[1] = 29
        N_Y_DAYS = 366
    else:
        N_M_DAYS[1] = 28
        N_Y_DAYS = 365


check_leap_year(2000)
print(N_M_DAYS)
print(N_Y_DAYS)

Date = Tuple[int, int, int]  # Y, M, D


def calc_y_days(date: Date) -> int:
    """计算(y, m, d)是y年的第几天. 假设1月1日是第一天. Ot(m)"""
    y, m, d = date
    res = 0
    check_leap_year(y)
    for i in range(m - 1):
        res += N_M_DAYS[i]
    res += d
    return res


print(calc_y_days((2021, 1, 1)))
print(calc_y_days((2021, 2, 1)))
print(calc_y_days((2021, 12, 31)))
print(calc_y_days((2020, 12, 31)))
"""
1
32
365
366
"""


def date_add_days(date: Date, days: int) -> Date:
    """返回date + days. Ot(days // 365)"""
    days += calc_y_days(date) - 1
    y, m, d = date[0], 1, 1
    # check_leap_year()
    while days >= N_Y_DAYS:
        days -= N_Y_DAYS
        y += 1
        check_leap_year(y)
    while days >= N_M_DAYS[m - 1]:
        days -= N_M_DAYS[m - 1]
        m += 1
    d += days

    return y, m, d


print(date_add_days((2007, 1, 1), 0))
print(date_add_days((2007, 1, 1), 31))
print(date_add_days((2007, 1, 1), 365))
print(date_add_days((2007, 1, 1), 366))
print(date_add_days((2007, 1, 1), 365 + 365))
print(date_add_days((2007, 1, 1), 365 + 366))
"""
(2007, 1, 1)
(2007, 2, 1)
(2008, 1, 1)
(2008, 1, 2)
(2008, 12, 31)
(2009, 1, 1)
"""


def date_ge(date1: Date, date2: Date) -> bool:
    """是否date1 > date2. Ot(1)"""
    y1, m1, d1 = date1
    y2, m2, d2 = date2
    return y1 > y2 or y1 == y2 and (m1 > m2 or m1 == m2 and d1 >= d2)


print(date_ge((2008, 1, 1), (2008, 1, 2)))
print(date_ge((2008, 1, 2), (2008, 1, 1)))
print(date_ge((2008, 1, 1), (2008, 1, 1)))
"""
False
True
True
"""


def calc_diff_days(date1: Date, date2: Date) -> int:
    """date2 - date1. Ot(m1 + m2 + |y2-y1|)"""
    neg = False
    if not date_ge(date2, date1):
        date1, date2 = date2, date1
        neg = True
    day1 = calc_y_days(date1)
    day2 = calc_y_days(date2)
    diff_days = day2 - day1
    y1, y2 = date1[0], date2[0]
    while y1 < y2:
        check_leap_year(y1)
        y1 += 1
        diff_days += N_Y_DAYS
    return -diff_days if neg else diff_days


print(calc_diff_days((2010, 1, 1), (2011, 1, 1)))
print(calc_diff_days((2008, 1, 1), (2009, 1, 1)))
print(calc_diff_days((2008, 1, 1), (2008, 12, 31)))
"""
365
366
365
"""


def test_date_valid(date) -> bool:
    """Ot(1)"""
    y, m, d = date
    check_leap_year(y)
    return 0 <= m < 12 and 0 < d <= N_M_DAYS[m - 1]


print(test_date_valid((2008, 2, 29)))
print(test_date_valid((2009, 2, 29)))
"""
True
False
"""
