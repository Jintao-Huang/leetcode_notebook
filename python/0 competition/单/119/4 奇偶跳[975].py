# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
from collections import deque


def next_ge_min(nums: List[int]) -> List[int]:
    arg = sorted(range(len(nums)), key=lambda i: nums[i])
    ans = [-1] * len(arg)
    st = []
    for lo in reversed(range(len(arg))):
        x = arg[lo]
        while len(st) > 0 and x >= arg[st[-1]]:  # 队列内无相等元素.
            st.pop()
        if len(st) > 0:
            ans[x] = arg[st[-1]]  # ans[hi] = nums[st[-1]]  # st可存数字
        st.append(lo)
    return ans


def next_le_max(nums: List[int]) -> List[int]:
    arg = sorted(range(len(nums)), key=lambda i: -nums[i])
    ans = [-1] * len(arg)
    st = []
    for lo in reversed(range(len(arg))):
        x = arg[lo]
        while len(st) > 0 and x >= arg[st[-1]]:  # 队列内无相等元素.
            st.pop()
        if len(st) > 0:
            ans[x] = arg[st[-1]]  # ans[hi] = nums[st[-1]]  # st可存数字
        st.append(lo)
    return ans


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        # 选择: 单数跳/双数跳
        # dp[i][j]. 奇数偶数, 以j为起点. 是否可行
        odd_next = next_ge_min(arr)
        even_next = next_le_max(arr)
        odd_dp = [False] * len(arr)
        even_dp = [False] * len(arr)
        odd_dp[-1] = True
        even_dp[-1] = True
        for i in reversed(range(len(arr) - 1)):
            # odd
            ne = odd_next[i]
            odd_dp[i] = even_dp[ne] if 0 <= ne < len(arr) else False
            # even
            ne = even_next[i]
            even_dp[i] = odd_dp[ne] if 0 <= ne < len(arr) else False
        return sum(odd_dp)


nums = [10, 13, 12, 14, 15]
print(Solution().oddEvenJumps(nums))

arr = [2, 3, 1, 1, 4]
print(Solution().oddEvenJumps(arr))

arr = [5, 1, 3, 4, 2]
print(Solution().oddEvenJumps(arr))
