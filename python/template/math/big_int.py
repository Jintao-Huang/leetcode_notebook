# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List, Tuple, Union


class BigInt:
    """>=0"""

    def __init__(self, nums):
        self.nums = nums

    @staticmethod
    def nums_divmod_int(nums: List[int], x2: int) -> Tuple[List[int], int]:
        ans = []
        s = 0
        for x in nums:
            s *= 10
            s += x
            d, s = divmod(s, x2)
            if d == 0 and len(ans) == 0:
                continue
            ans.append(d)
        return ans, s

    def __divmod__(self, other) -> Tuple['BigInt', int]:
        ans = self.nums_divmod_int(self.nums, other)
        return BigInt(ans[0]), ans[1]

    def __floordiv__(self, other: int) -> 'BigInt':
        return self.__divmod__(other)[0]

    def __mod__(self, other: int) -> int:
        return self.__divmod__(other)[1]

    @staticmethod
    def nums_mul_nums(n1: List[int], n2: List[int]) -> List[int]:
        ans = []
        for x1 in n1:
            if len(ans) > 0:
                ans.append(0)  # *10
            z = BigInt.nums_mul_int(n2, x1)
            ans = BigInt.nums_add_nums(ans, z)
        return ans

    @staticmethod
    def nums_mul_int(nums: List[int], x2: int) -> List[int]:
        ans = []
        s = 0
        for x in reversed(nums):
            s += x * x2
            s, mo = divmod(s, 10)
            ans.append(mo)
        while s > 0:
            s, mo = divmod(s, 10)
            ans.append(mo)
        ans.reverse()
        return ans

    def __mul__(self, other: Union[int, 'BigInt']) -> 'BigInt':
        if isinstance(other, int):
            return BigInt(self.nums_mul_int(self.nums, other))
        else:
            return BigInt(self.nums_mul_nums(self.nums, other.nums))

    @staticmethod
    def nums_add_int(nums: List[int], x2: int) -> List[int]:
        ans = []
        s = 0
        for x in reversed(nums):
            x2, mo = divmod(x2, 10)
            s += x + mo
            s, mo = divmod(s, 10)
            ans.append(mo)
        x2 += s
        while x2 > 0:
            x2, mo = divmod(x2, 10)
            s += mo
            ans.append(mo)

        ans.reverse()
        return ans

    @staticmethod
    def nums_add_nums(n1: List[int], n2: List[int]):
        ans = []
        s = 0
        m, n = len(n1), len(n2)
        for i in range(max(m, n)):
            x1 = n1[m - 1 - i] if m - 1 - i >= 0 else 0
            x2 = n2[n - 1 - i] if n - 1 - i >= 0 else 0
            s += x1 + x2
            s, mo = divmod(s, 10)
            ans.append(mo)
        if s > 0:
            ans.append(s)
        ans.reverse()
        return ans

    def __add__(self, other: Union[int, 'BigInt']) -> 'BigInt':
        if isinstance(other, int):
            return BigInt(self.nums_add_int(self.nums, other))
        else:
            return BigInt(self.nums_add_nums(self.nums, other.nums))

    def __str__(self):
        return str(self.nums)

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    nums = [4, 3, 3, 8, 5, 2]
    print(divmod(BigInt(nums), 7))
    print(BigInt(nums) // 7)
    print(BigInt(nums) % 7)
    print(divmod(int("".join([str(x) for x in nums])), 7))
    print(BigInt(nums) * 7)
    print(int("".join([str(x) for x in nums])) * 7)
    x = 99876543
    print(BigInt(nums) + x)
    print(int("".join([str(x) for x in nums])) + x)
    print(BigInt(nums) + BigInt([9, 9, 9]))
    print(int("".join([str(x) for x in nums])) + 999)

    #
    print(BigInt(nums) * BigInt([9, 9, 9]))
    print(int("".join([str(x) for x in nums])) * 999)
    #
    print(divmod(BigInt([1, 0, 0, 0, 0]), 10))
