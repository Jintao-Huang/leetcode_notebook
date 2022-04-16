# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List


class Solution:
    def dfs(self, materials, cookbooks, attribute, limit, path, ans, idx):
        # path: 美味, 饱腹
        if idx >= len(cookbooks):
            if path[1] >= limit:
                ans[0] = max(ans[0], path[0])
            return
        #
        self.dfs(
            materials, cookbooks, attribute, limit,
            path, ans, idx + 1
        )
        #
        c = cookbooks[idx]
        m_copy = materials.copy()
        for j in range(len(m_copy)):
            m_copy[j] -= c[j]
            if m_copy[j] < 0:
                return
        self.dfs(
            m_copy, cookbooks, attribute, limit,
            [path[0] + attribute[idx][0], path[1] + attribute[idx][1]], ans, idx + 1
        )

    def perfectMenu(
            self,
            materials: List[int],
            cookbooks: List[List[int]],
            attribute: List[List[int]],
            limit: int
    ) -> int:
        ans = [-1]
        self.dfs(materials, cookbooks, attribute, limit, [0, 0], ans, 0)
        return ans[0]


materials = [3, 4, 4, 1, 2]
cookbooks = [[1, 1, 0, 1, 2], [2, 1, 4, 0, 0], [3, 2, 4, 1, 0]]
attribute = [[3, 2], [6, 4], [7, 6]]
limit = 6
print(Solution().perfectMenu(materials, cookbooks, attribute, limit))

# materials = [10, 10, 10, 10, 10]
# cookbooks = [[1, 1, 1, 1, 1], [3, 3, 3, 3, 3], [10, 10, 10, 10, 10]]
# attribute = [[5, 5], [6, 6], [10, 10]]
# limit = 1
# print(Solution().perfectMenu(materials, cookbooks, attribute, limit))
# #
# materials = [1 ,0 ,1, 1, 1]
# cookbooks = [[1, 1, 1, 1, 1], [3, 3, 3, 3, 3], [10, 10, 10, 10, 10]]
# attribute = [[5, 5], [6, 6], [10, 10]]
# limit = 5
# print(Solution().perfectMenu(materials, cookbooks, attribute, limit))
