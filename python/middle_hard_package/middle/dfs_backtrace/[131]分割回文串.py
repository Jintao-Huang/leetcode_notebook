# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


def is_palindrome(s: str) -> bool:
    lo, hi = 0, len(s) - 1
    while lo < hi:
        if s[lo] != s[hi]:
            return False
        lo += 1
        hi -= 1
    return True


class Solution:
    def dfs(self, ans: List[List[str]], path: List[str], s: str, i):
        if i == len(s):
            if is_palindrome(path[-1]):
                ans.append(path.copy())
            return
        if is_palindrome(path[-1]):
            path.append(s[i])
            self.dfs(ans, path, s, i + 1)
            path.pop()
        s_old = path[-1]
        path[-1] = s_old + s[i]
        self.dfs(ans, path, s, i + 1)
        path[-1] = s_old

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.dfs(ans, [s[0]], s, 1)
        return ans


print(Solution().partition("aab"))