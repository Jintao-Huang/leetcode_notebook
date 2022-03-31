# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from template.utils.palindrome import gen_palindrome_num


class Solution:

    def nearestPalindromic(self, n: str) -> str:
        len_ = len(n)
        int_n = int(n)
        x = int(n[:(len_ + 1) // 2])
        tag = len_ % 2
        ans = []
        for x2 in [x, x + 1, x - 1]:
            a = gen_palindrome_num(x2, tag)
            if a != int_n:
                ans.append(a)
        # 备选的
        if len_ - 1 > 0:
            x2 = int('9' * (len_ - 1))
            if x2 != int_n:
                ans.append(x2)
        x2 = int('1' + '0' * (len_ - 1) + '1')
        if x2 != int_n:
            ans.append(x2)

        return str(min(ans, key=lambda t: (abs(t - int_n), t)))


# n = "123"
# print(Solution().nearestPalindromic(n))
#
n = "1"
print(Solution().nearestPalindromic(n))

n = "10"
print(Solution().nearestPalindromic(n))
