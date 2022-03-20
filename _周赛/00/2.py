# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from typing import List, Dict, Tuple


class Solution:
    def digArtifacts(self, n: int,
                     artifacts: List[List[int]],
                     dig: List[List[int]]) -> int:
        ans = 0
        s = set(tuple(d) for d in dig)
        artifacts.sort()
        k = 0
        for i in range(n):
            for j in range(n):
                if k >= len(artifacts):
                    return ans
                a = artifacts[k]
                if a[0] == i and a[1] == j:
                    k += 1
                    yes = True
                    for ii in range(a[0], a[2] + 1):
                        for jj in range(a[1], a[3] + 1):
                            if (ii, jj) not in s:
                                yes = False
                                break
                    ans += yes
        return ans


n = 2
artifacts = [[0, 0, 0, 0], [0, 1, 1, 1]]
dig = [[0, 0], [0, 1]]
# dig = [[0, 0], [0, 1], [1, 1]]
print(Solution().digArtifacts(n, artifacts, dig))
