# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List

"""
1. 先要考虑nums长度为0的情况，后面优化时可以省略
2. x in s 是O(1)的
*3. 出现乱序用hashMap
"""


class Solution217:
    """存在重复元素"""

    def containsDuplicate(self, nums: List[int]) -> bool:
        """Ot(N) Os(N)"""
        s = set()
        for x in nums:
            if x in s:  # O(1)
                return True
            else:
                s.add(x)  # O(1)
        else:
            return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        """Ot(N) Os(N)"""
        s = set(nums)
        return len(s) != len(nums)


# nums = [1, 2, 3, 1]
# print(Solution217().containsDuplicate(nums))  # True
#

"""
*1. 数组法
*2. 求和法
*3. 异或法
4. 是否使用set(arr)
"""


class Solution389:
    """找不同. t > s"""

    def findTheDifference(self, s: str, t: str) -> str:
        """Ot(N) Os(字符数26)"""
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for c in t:
            if c not in d:
                return c
            else:
                d[c] -= 1
                if d[c] < 0:
                    return c

    def findTheDifference2(self, s: str, t: str) -> str:
        """Ot(N) Os(字符数26). 使用数组"""
        a = [0] * 26  # a - z
        offset = ord("a")
        for c in s:
            a[ord(c) - offset] += 1
        for c in t:
            i = ord(c) - offset
            a[i] -= 1
            if a[i] < 0:
                return c

    def findTheDifference3(self, s: str, t: str) -> str:
        """Ot(N) Os(1). 求和法"""
        sum_ = 0
        for c in t:
            sum_ += ord(c)
        for c in s:
            sum_ -= ord(c)
        return chr(sum_)

    def findTheDifference4(self, s: str, t: str) -> str:
        """Ot(N) Os(1). 异或法

        异或运算：
        1. 交换律：a ^ b ^ c <=> a ^ c ^ b
        2. 任何数于0异或为任何数 0 ^ n => n
        3. 相同的数异或为0: n ^ n => 0
        """
        sum_ = 0
        for c in t:
            sum_ ^= ord(c)
        for c in s:
            sum_ ^= ord(c)
        return chr(sum_)


# s = "ae"
# t = "aea"
# print(Solution389().findTheDifference(s, t))  # a
# print(Solution389().findTheDifference2(s, t))  # a
# print(Solution389().findTheDifference3(s, t))  # a
# print(Solution389().findTheDifference4(s, t))  # a


class Solution496:
    """下一个最大元素I. 见栈"""
    pass
