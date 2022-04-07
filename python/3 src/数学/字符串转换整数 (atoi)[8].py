# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


class Solution:
    def myAtoi(self, s: str) -> int:

        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        #
        if i >= len(s):
            return 0
        if s[i] == '-':
            flag = -1
            i += 1
        else:
            if s[i] == '+':
                i += 1
            flag = 1
        #
        ord_0 = ord('0')
        ans = 0
        for i in range(i, len(s)):
            c = ord(s[i]) - ord_0
            if 0 <= c <= 9:
                ans *= 10
                ans += c
            else:
                break

        return max(min(ans * flag, 2147483647), -2147483648)


print(Solution().myAtoi('  -'))
