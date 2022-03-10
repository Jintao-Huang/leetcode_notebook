# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

class Solution:
    """Ot(n) Os(1)"""

    def isPalindrome(self, x: int) -> bool:
        # 不加也是对的
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0:
            return False
        #
        x_r = 0
        t = x
        while t > 0:
            x_r *= 10
            x_r += t % 10
            t //= 10
        return x_r == x


print(Solution().isPalindrome(-121))
