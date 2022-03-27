# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

def bubble(arr, start, end) -> int:
    ans = 0
    if start < end:
        for i in range(start, end):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            ans += 1
    else:
        for i in range(start, end, -1):
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            ans += 1
    return ans


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
                        ans += bubble(s, lo + i, lo)
                        break
                    if s[lo] == s[hi - i]:
                        ans += bubble(s, hi - i, hi)
                        break
        return ans


s = "letelt"
print(Solution().minMovesToMakePalindrome(s))
