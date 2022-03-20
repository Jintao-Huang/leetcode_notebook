# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """贪心. Ot(N) Os(N). 分为左右限制"""
    def candy(self, ratings: List[int]) -> int:
        c = 1
        cl = [c]  # 只考虑左边
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                c += 1
            else:
                c = 1
            cl.append(c)
        ans = cl[-1]
        c = 1
        for i in reversed(range(len(ratings) - 1)):
            if ratings[i] > ratings[i + 1]:
                c += 1
            else:
                c = 1
            ans += max(cl[i], c)
        return ans


ratings = [1, 3, 2, 2, 1]
print(Solution().candy(ratings))
print(Solution().candy([1, 0, 2]))
