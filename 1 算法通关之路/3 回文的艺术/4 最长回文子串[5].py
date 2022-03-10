# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:


class Solution:
    """中心拓展法. Ot(N^2) Os(1)"""

    @staticmethod
    def extend(s: str, i: int, j: int) -> str:
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break
            i -= 1
            j += 1
        return s[i + 1:j]

    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            s1 = self.extend(s, i, i)
            s2 = self.extend(s, i, i + 1)
            if len(ans) < len(s1):
                ans = s1
            if len(ans) < len(s2):
                ans = s2
        return ans


s = "babad"
print(Solution().longestPalindrome(s))
