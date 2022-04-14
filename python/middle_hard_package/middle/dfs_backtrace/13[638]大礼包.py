# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    def buy(self, price, needs) -> int:
        ans = 0
        for i in range(len(needs)):
            ans += needs[i] * price[i]
        return ans

    def dfs(self, price, special, needs, ans, cur_price, i):
        if i == len(special):
            p = self.buy(price, needs)
            ans[0] = min(ans[0], p + cur_price)
            return
        #
        while True:  # 买n次
            self.dfs(price, special, needs.copy(), ans, cur_price, i + 1)
            #
            n = len(price)
            for j in range(n):
                s = special[i][j]
                needs[j] -= s
                if needs[j] < 0:
                    return
            cur_price += special[i][n]

    def shoppingOffers(
            self,
            price: List[int],
            special: List[List[int]],
            needs: List[int]
    ) -> int:
        INF = int(1e9)
        ans = [INF]
        self.dfs(price, special, needs, ans, 0, 0)
        return ans[0]


price = [2,5]
special = [[3,0,5],[1,2,10]]
needs = [3,2]
print(Solution().shoppingOffers(price, special, needs))

price = [2,3,4]
special = [[1,1,0,4],[2,2,1,9]]
needs = [1,2,1]
print(Solution().shoppingOffers(price, special, needs))
price = [9, 9]
special = [[1, 1, 1]]
needs = [2, 2]
print(Solution().shoppingOffers(price, special, needs))
