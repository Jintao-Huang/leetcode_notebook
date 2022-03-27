# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class Solution:
    """栈"""

    def minDeletion(self, nums: List[int]) -> int:
        ans = 0
        st = []
        for i in range(len(nums)):
            x = nums[i]
            if len(st) % 2 == 0:
                st.append(x)
            else:
                if x != st[-1]:
                    st.append(x)
                else:
                    ans += 1
        if len(st) % 2 == 1:
            ans += 1
        return ans


class Solution2:
    """空间优化. Os(1)"""

    def minDeletion(self, nums: List[int]) -> int:
        ans = 0
        st_top = -1
        even = True
        for i in range(len(nums)):
            x = nums[i]
            if even:
                st_top = x
                even = not even
            else:
                if x != st_top:
                    st_top = x
                    even = not even
                else:
                    ans += 1
        if not even:
            ans += 1
        return ans


nums = [1, 1, 2, 3, 5]
print(Solution().minDeletion(nums))
print(Solution2().minDeletion(nums))
nums = [1, 1, 2, 2, 3, 3]
print(Solution().minDeletion(nums))
print(Solution2().minDeletion(nums))
