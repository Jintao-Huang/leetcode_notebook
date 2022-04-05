# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from collections import deque

"""
1. 要使得题目中所有条件发挥作用, 例如：t递增
*2. 使用栈还是队列的区分：
  需要先进先出，还是后进先出
"""


class RecentCounter:
    """933 最近的请求次数（先进先出的思想）"""

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        """接近Ot(1) 接近Os(1)"""
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)

# recentCounter = RecentCounter()
# print(recentCounter.ping(1))  # 1
# print(recentCounter.ping(100))  # 2
# print(recentCounter.ping(3001))  # 3
# print(recentCounter.queue)  # deque([1, 100, 3001])
# print(recentCounter.ping(3002))  # 3
# print(recentCounter.queue)  # deque([100, 3001, 3002])
