# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from typing import List, Deque, Set
from collections import deque


class Solution:
    """bfs"""

    def _bfs(self, begin: str, deadends: Set[str], target: str) -> int:
        # 选择: i, 0-9
        if begin in deadends:
            return -1
        deadends.add(begin)
        q = deque([begin])
        ans = 0
        while len(q) > 0:
            for _ in range(len(q)):
                s = q.popleft()
                if s == target:
                    return ans
                for i in range(len(s)):
                    c = s[i]
                    c_list = [str((int(c) + 1) % 10), str((int(c) - 1) % 10)]
                    for c2 in c_list:
                        s2 = s[:i] + c2 + s[i + 1:]
                        if s2 not in deadends:
                            q.append(s2)
                            deadends.add(s2)

            ans += 1
        return -1

    def openLock(self, deadends: List[str], target: str) -> int:
        return self._bfs("0000", set(deadends), target)


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
print(Solution().openLock(deadends, target))
