# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 



class Solution:
    """贪心"""
    def minMovesToMakePalindrome(self, s: str) -> int:
        lo, hi = 0, len(s) - 1
        s = list(s)
        ans = 0
        while lo < hi:
            if s[lo] == s[hi]:
                lo += 1
                hi -= 1
            else:
                for i in range(len(s)):
                    if s[lo + i] == s[hi]:
                        for j in range(i, 0, -1):
                            ans += 1
                            s[lo + j], s[lo + j - 1] = s[lo + j - 1], s[lo + j]
                        break
                    if s[lo] == s[hi - i]:
                        for j in range(i, 0, -1):
                            ans += 1
                            s[hi - j], s[hi - j + 1] = s[hi - j + 1], s[hi - j]
                        break
        return ans

s = "letelta"
print(Solution().minMovesToMakePalindrome(s))