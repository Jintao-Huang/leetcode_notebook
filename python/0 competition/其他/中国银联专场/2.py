# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
import bisect

from template.data_structure.sorted_list import SortedList
from collections import defaultdict

class Activity:
    def __init__(self, actId: int, priceLimit: int, discount: int, number: int, userLimit: int):
        self.actId = actId
        self.priceLimit = priceLimit
        self.discount = discount
        self.number = number
        self.userLimit = userLimit
        self.u_cnt = defaultdict(int)  # 参加次数

    def consume(self, userId: int, cost: int) -> bool:
        if self.number <= 0:
            return False
        if cost < self.priceLimit:
            return False
        if self.u_cnt[userId] >= self.userLimit:
            return False
        self.u_cnt[userId] += 1
        self.number -= 1
        return True


class DiscountSystem:

    def __init__(self):
        self.sl = SortedList()
        self.d = {}

    def addActivity(self, actId: int, priceLimit: int, discount: int, number: int, userLimit: int) -> None:
        item = discount, -actId, Activity(actId, priceLimit, discount, number, userLimit)
        self.d[actId] = item
        self.sl.add(item)

    def removeActivity(self, actId: int) -> None:
        item = self.d.pop(actId)
        self.sl.remove(item)

    def consume(self, userId: int, cost: int) -> int:
        for i in reversed(range(len(self.sl))):
            d, aid, a = self.sl[i]
            if a.consume(userId, cost):
                return cost - d
        return cost

