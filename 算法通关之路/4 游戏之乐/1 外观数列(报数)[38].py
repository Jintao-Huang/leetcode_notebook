# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from typing import List


class Solution:
    """迭代. Ot(NM) Os(M). M为最后一次的字符串长度. (此时间复杂度为 不进行memo时间优化时的复杂度)"""

    def __init__(self):
        self.memo = ["1"]  # type: List[str]

    def countAndSay(self, n: int) -> str:
        for i in range(len(self.memo), n):
            s = self.memo[-1]
            #
            tmp = []
            c_prev = s[0]
            nums = 0
            for c in s:
                if c == c_prev:
                    nums += 1
                else:
                    tmp += [str(nums), c_prev]
                    c_prev = c
                    nums = 1
            tmp += [str(nums), c_prev]
            self.memo.append("".join(tmp))
        return self.memo[n - 1]


class Solution2:
    """递归. Ot(NM) Os(M+N). M为最后一次的字符串长度. (此时间复杂度为 不进行memo时间优化时的复杂度)"""

    def __init__(self):
        self.memo = ["1"]  # type: List[str]

    def countAndSay(self, n: int) -> str:
        if len(self.memo) >= n:
            return self.memo[n - 1]
        tmp = []
        #
        s = self.countAndSay(n - 1)
        c_prev = s[0]
        nums = 0
        for c in s:
            if c == c_prev:
                nums += 1
            else:
                tmp += [str(nums), c_prev]
                c_prev = c
                nums = 1
        tmp += [str(nums), c_prev]
        #
        self.memo.append("".join(tmp))
        return self.memo[n - 1]

s = Solution()
s2 = Solution2()
print(s.countAndSay(4))
print(s.countAndSay(4))
print(s2.countAndSay(4))
print(s2.countAndSay(4))
