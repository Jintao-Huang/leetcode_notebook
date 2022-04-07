# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        ans = 0
        #
        for i in range(2, n):
            if not is_prime[i]:
                continue
            #
            ans += 1
            for j in range(i * i, n, i):
                is_prime[j] = False
        return ans
