# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/2-keys-keyboard/
650. 只有两个键的键盘
- 中等
=
- 动态规划
"""

from functools import lru_cache


class Solution:
    def minSteps(self, n: int) -> int:

        INT_MAX = int(1e9)

        @lru_cache(n + 3)
        def _dp(i: int, j: int) -> int:
            """

            :param i: 还需要打印A的个数
            :param j: 粘贴板A数目
            :return:
            """
            if i == 0:
                return 0
            if i < 0:
                return INT_MAX
            if i == j:
                return 1
            #
            return min(
                _dp(i - j, j) + 1 if j > 0 else INT_MAX,
                _dp(i, n - i) + 1 if j != n - i else INT_MAX
            )

        return _dp(n - 1, 0)


n = 5
print(Solution().minSteps(n))
