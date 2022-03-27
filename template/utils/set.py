# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import Set


def update(s1: Set[int], s2: Set[int]) -> None:
    for x in s2:
        if x not in s1:
            s1.add(x)


def intersection_update(s1: Set[int], s2: Set[int]) -> None:
    for x in s1.copy():
        if x not in s2:
            s1.remove(x)


def difference_update(s1: Set[int], s2: Set[int]) -> None:
    for x in s2:
        if x in s1:
            s1.remove(x)


def symmetric_difference(s1: Set[int], s2: Set[int]) -> Set[int]:
    ans = set()
    for x in s1:
        if x not in s2:
            ans.add(x)
    for x in s2:
        if x not in s1:
            ans.add(x)
    return ans


if __name__ == '__main__':
    s1 = {1, 2}
    s2 = {2, 3}
    print(s1 | s2)
    update(s1, s2)
    print(s1)

    #
    s1 = {1, 2}
    print(s1 & s2)
    intersection_update(s1, s2)
    print(s1)

    #
    s1 = {1, 2}
    print(s1 - s2)
    difference_update(s1, s2)
    print(s1)

    #
    s1 = {1, 2}
    print(s1 ^ s2)
    print(symmetric_difference(s1, s2))


def issuperset(s1: Set[int], s2: Set[int]) -> bool:
    for x in s2:
        if x not in s1:
            return False
    return True


def issubset(s1: Set[int], s2: Set[int]) -> bool:
    for x in s1:
        if x not in s2:
            return False
    return True


def isdisjoint(s1: Set[int], s2: Set[int]) -> bool:
    # 不相交的
    # return len(s1 & s2) == 0
    for x in s1:
        if x in s2:
            return False
    return True


if __name__ == '__main__':
    s1 = {1, 2}
    s2 = {1, 2}
    print(issuperset(s1, s2))
    print(issubset(s1, s2))
    print(isdisjoint(s1, s2))
    print(s1.issuperset(s2))
    print(s1.issubset(s2))
    print(s1.isdisjoint(s2))
