# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

class Solution:
    def bulbSwitch(self, n: int) -> int:
        # e.g. 6: 1,2,3,6. 对称
        return int(n ** (1 / 2))
