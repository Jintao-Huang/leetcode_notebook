# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List

"""
*1. 滑动窗口: for结构
*2. 在下标越界前判断是否break
*3. 使用闭区间优势是索引, 开区间优势是len
"""


class Solution209:
    """长度最小的子数组"""

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """滑动窗口. Ot(N) Os(1). 推荐"""
        length = len(nums)
        i = 0  # start
        t = 0
        min_len = length + 1
        for j in range(0, length):  # end
            t += nums[j]
            while t >= target:
                min_len = min(min_len, j - i + 1)
                t -= nums[i]
                i += 1

        return 0 if min_len == length + 1 else min_len


target = 11
nums = [1, 2, 3, 4, 5]
print(Solution209().minSubArrayLen(target, nums))

target = 4
nums = [1, 4, 4]
print(Solution209().minSubArrayLen(target, nums))

target = 40
nums = [1, 4, 4]
print(Solution209().minSubArrayLen(target, nums))

target = 213
nums = [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]
print(Solution209().minSubArrayLen(target, nums))

"""
*1. 索引越界 -> 边界条件 -> 边界(for)
"""


class Solution1456:
    """定长子串中元音的最大数目"""

    def maxVowels(self, s: str, k: int) -> int:
        """Ot(N) Os(1)"""
        yuan = {"a", "e", "i", "o", "u"}
        count = 0
        max_yuan = 0
        # 初始化
        for i in range(k):
            if s[i] in yuan:
                count += 1
        max_yuan = max(count, max_yuan)
        for i in range(k, len(s)):
            if s[i - k] in yuan:
                count -= 1
            if s[i] in yuan:
                count += 1
            max_yuan = max(count, max_yuan)
        return max_yuan


s = "weallloveyou"
k = 7

print(Solution1456().maxVowels(s, k))
