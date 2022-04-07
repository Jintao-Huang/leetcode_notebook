# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        st = []  # 若: next_le(), 将递减栈变为递增栈. 必须存idx.
        for hi in range(len(temperatures)):
            while len(st) > 0 and temperatures[hi] > temperatures[st[-1]]:
                lo = st.pop()
                ans[lo] = hi - lo
            st.append(hi)

        return ans
