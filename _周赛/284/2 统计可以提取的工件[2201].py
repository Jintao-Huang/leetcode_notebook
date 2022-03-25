# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from typing import List, Dict, Tuple


class C:
    def __init__(self, val):
        self.val = val  # 引用数


class Solution:
    """哈希."""

    def digArtifacts(self, n: int,
                     artifacts: List[List[int]],
                     dig: List[List[int]]) -> int:
        exist = {}
        for l, t, r, b in artifacts:
            c = C((r - l + 1) * (b - t + 1))
            for i in range(l, r + 1):
                for j in range(t, b + 1):
                    exist[(i, j)] = c

        ans = 0
        for d in dig:
            d = tuple(d)
            if d in exist:
                exist[d].val -= 1
                if exist[d].val == 0:
                    ans += 1
        return ans


class Solution2:
    """哈希."""

    def digArtifacts(self, n: int,
                     artifacts: List[List[int]],
                     dig: List[List[int]]) -> int:
        dig = set(tuple(d) for d in dig)
        ans = 0

        for l, t, r, b in artifacts:
            no_dig = False
            for i in range(l, r + 1):
                for j in range(t, b + 1):
                    if (i, j) not in dig:
                        no_dig = True
                        break
                if no_dig:
                    break
            if no_dig is False:
                ans += 1

        return ans


n = 7

artifacts = [[1, 1, 1, 4], [6, 0, 6, 3], [2, 0, 3, 1], [1, 6, 4, 6]]
dig = [[0, 1], [0, 4], [0, 6], [1, 3], [1, 6], [2, 1], [2, 5], [2, 6], [3, 0], [3, 1], [3, 2], [3, 3], [4, 3], [4, 4],
       [5, 0], [5, 2], [5, 3], [5, 4], [6, 6]]

# dig = [[0, 0], [0, 1], [1, 1]]
print(Solution().digArtifacts(n, artifacts, dig))
print(Solution2().digArtifacts(n, artifacts, dig))
