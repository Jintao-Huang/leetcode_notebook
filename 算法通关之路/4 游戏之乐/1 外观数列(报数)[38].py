# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
class Solution:
    """迭代. Ot(NM) Os(M). M为最后一次的字符串长度. (此时间复杂度为 不进行memo时间优化时的复杂度)"""

    def __init__(self):
        self.memo = ["1"]

    def countAndSay(self, n: int) -> str:
        s = self.memo[-1]
        #
        for i in range(len(s) - 1, n):
            ans = []
            c_prev = s[0]
            nums = 0
            for c in s:
                if c == c_prev:
                    nums += 1
                else:
                    ans += [str(nums), c_prev]
                    c_prev = c
                    nums = 1
            ans += [str(nums), c_prev]
            s = "".join(ans)
            self.memo.append(s)
        return self.memo[n - 1]


class Solution2:
    """递归. Ot(NM) Os(M+N). M为最后一次的字符串长度. (此时间复杂度为 不进行memo时间优化时的复杂度)"""

    def __init__(self):
        self.memo = ["1"]

    def countAndSay(self, n: int) -> str:
        if len(self.memo) >= n:
            return self.memo[n - 1]
        ans = []
        #
        s = self.countAndSay(n - 1)
        c_prev = s[0]
        nums = 0
        for c in s:
            if c == c_prev:
                nums += 1
            else:
                ans += [str(nums), c_prev]
                c_prev = c
                nums = 1
        ans += [str(nums), c_prev]
        ans = "".join(ans)
        #
        self.memo.append(ans)
        return self.memo[n - 1]


print(Solution().countAndSay(4))
print(Solution2().countAndSay(4))
