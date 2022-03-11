# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:


class Solution:
    """滑动窗口. Ot(NM) Os(M+N). M为最后一次的字符串长度. 初始化时的复杂度"""

    @staticmethod
    def next_s(s: str):
        # shrink: s[lo] != s[hi]
        # : True.
        lo = 0
        ans = []
        for hi in range(len(s)):
            c = s[hi]
            c2 = s[lo]
            if c != c2:
                ans.append(str(hi - lo))
                ans.append(c2)
                lo = hi

        ans.append(str(hi - lo + 1))
        ans.append(s[lo])
        return "".join(ans)

    def countAndSay(self, n: int) -> str:
        self.ans = ["1"]
        for i in range(1, n):
            self.ans.append(self.next_s(self.ans[-1]))
        return self.ans[n - 1]


s = Solution()
