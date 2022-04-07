# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

class Solution:
    def countCollisions(self, directions: str) -> int:
        dp = [''] * len(directions)
        dp[0] = directions[0]
        ans = 0
        for i in range(1, len(directions)):
            if directions[i] == 'L' and dp[i - 1] != 'L':
                dp[i] = 'S'
                ans += 1
            else:
                dp[i] = directions[i]

        for i in reversed(range(len(directions) - 1)):
            if directions[i] == 'R' and dp[i + 1] != 'R':
                dp[i] = 'S'
                ans += 1
        return ans


class Solution2:
    def countCollisions(self, s: str) -> int:
        s = s.lstrip('L')
        s = s.rstrip('R')
        return len(s) - s.count('S')


# directions = "RLRSLL"
# print(Solution().countCollisions(directions))
#
directions = "SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"
print(Solution().countCollisions(directions))
print(Solution2().countCollisions(directions))

# directions = "LLRR"
# print(Solution().countCollisions(directions))
