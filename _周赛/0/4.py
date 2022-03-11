# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from collections import deque


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        # 选择: 单数跳/双数跳
        # dp[i][j]. 奇数偶数, 以j为起点. 是否可行
        q1, q2 = deque(), deque()  # 递增(最小), 递减(最大)
        next_ = [[-1] * len(arr) for _ in range(2)]
        arg = sorted(range(len(arr)), key=lambda i: arr[i])
        print(arg)
        for i in reversed(arg):
            while len(q1) > 0 and i <= q1[-1]:
                q1.pop()
            next_[0][i] = q1[0] if len(q1) > 0 else -1
            q1.append(i)
            while len(q2) > 0 and i > q2[-1]:
                q2.pop()
            next_[1][i] = q2[0] if len(q2) > 0 else -1
            q2.append(i)
        print(next_)
        exit(0)


        dp = [[False] * len(arr) for _ in range(2)]
        dp[0][-1] = True
        dp[1][-1] = True
        ans = 1
        #
        for i in reversed(range(len(arr))):
            x = arr[i]

            if i < len(arr) - 1:
                # 奇数
                if len(q2) > 0:
                    i2 = q2[-1]
                    if x <= arr[i2]:
                        dp[0][i] = dp[1][i2]
                        ans += dp[0][i]
                # 偶数
                if len(q1) > 0:
                    i2 = q1[-1]
                    if x >= arr[i2]:
                        dp[1][i] = dp[0][i2]

            q1.append(i)

            q2.append(i)
            #
        return ans, dp



arr = [10,13,12,14,15]
print(Solution().oddEvenJumps(arr))

arr = [1,2,3,2,1,4,4,5]
print(Solution().oddEvenJumps(arr))
