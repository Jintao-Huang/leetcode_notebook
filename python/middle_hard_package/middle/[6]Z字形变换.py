# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = [[] for _ in range(numRows)]

        i, j = 0, 0
        k = 0
        n = len(s)
        while k < n:
            while k < n and i < numRows - 1:
                ans[i].append(s[k])
                i += 1
                k += 1
            while k < n and i >= 1:
                ans[i].append(s[k])
                i -= 1
                j += 1
                k += 1

        ans = ["".join(l) for l in ans]
        return "".join(ans)


# print(Solution().convert("PAYPALISHIRING", 3))
# print(Solution().convert("PAYPALISHIRING", 4))
print(Solution().convert("A", 1))
