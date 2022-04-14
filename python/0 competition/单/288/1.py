# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from typing import List

class Solution:
    def largestInteger(self, num: int) -> int:
        nums = [int(x) for x in str(num)]
        even = [x for x in nums if x % 2 == 0]
        odd = [x for x in nums if x % 2 == 1]
        even.sort(key=lambda x:-x)
        odd.sort(key=lambda x:-x)
        j, k = 0, 0
        for i in range(len(nums)):
            x = nums[i]
            if x % 2 == 0:
                nums[i] = even[j]
                j += 1
            else:
                nums[i] = odd[k]
                k += 1
        return int("".join(str(x) for x in nums))


print(Solution().largestInteger(1234))
print(Solution().largestInteger(65875))