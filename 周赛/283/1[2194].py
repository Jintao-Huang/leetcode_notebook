# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans = []
        for i in range(ord(s[0]), ord(s[3]) + 1):
            for j in range(ord(s[1]), ord(s[4]) + 1):
                ans.append(chr(i) + chr(j))
        return ans


s = "K1:L2"
print(Solution().cellsInRange(s))
