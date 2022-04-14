# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List


class Solution:
    def gen_ip(self, s, idx_path):
        ans = list(s)
        for i in reversed(range(1, len(idx_path) - 1)):
            idx = idx_path[i]
            ans.insert(idx, '.')
        return "".join(ans)

    def dfs(self, idx_path: List[int], s: str, i: int, ans: List[str]) -> None:
        if len(idx_path) == 5:
            if i == len(s):
                ans.append(self.gen_ip(s, idx_path))
            return
        if i >= len(s):
            return
        prev = idx_path[-1]
        for j in range(i, len(s)):
            ss = s[prev:j + 1]
            if ss[0] == '0' and len(ss) > 1:
                return
            if int(ss) > 255:  # s[prev..j]
                return
            idx_path.append(j + 1)
            self.dfs(idx_path, s, j + 1, ans)
            idx_path.pop()

    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.dfs([0], s, 0, ans)
        return ans


print(Solution().restoreIpAddresses("25525511135"))
print(Solution().restoreIpAddresses("0000"))
print(Solution().restoreIpAddresses("101023"))
