# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
假设你有一个特殊的键盘，包含以下的按键：
key 1：（A）：在屏幕上打印一个 A
key 2：（Ctrl-A）：选中整个屏幕
key 3：（Ctrl-C）：复制选中区域到缓冲区
key 4：（Ctrl-V）：将缓冲区内容输出到上次输入的结束位置，并显示在屏幕上
现在，你只可以按键N次（使用上述四种按键），请问屏幕上最多可以显示几个A？

样例1：
输入：N=3
输出：3
解释：我们最多可以在屏幕上显示3个A，通过如下顺序按键：A, A, A

样例2：
输入：N=7
输出：N=9
解释：我们最多可以在屏幕上显示9个A，通过如下顺序按键：A, A, A, Ctrl-A, Ctrl-C, Ctrl-V, Ctrl-V
"""


class Solution:
    def maxA(self, N: int) -> int:
        # 选择: ...Ctrl-V, A
        # dp_N^2[i]: 按键i次, 最多的A
        # dp_N^2[i]; dp_N^2[i-1]; dp_N^2[i-3]
        dp = [0] * (N + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, N + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i - 3 + 1):
                dp[i] = max(dp[i], (i - j - 1) * dp[j])
        return dp[N]


print(Solution().maxA(3))  # 3
print(Solution().maxA(7))  # 9
