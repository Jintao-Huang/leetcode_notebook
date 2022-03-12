# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from typing import List


# 更大元素: 递减栈
# a[i], a[j]: i < j; a[i] < a[j]; argmin[j](j-i)
class Solution:
    """弹出时"""

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        s = []  # 值
        ans = []
        for i in range(len(nums2)):
            x = nums2[i]
            while len(s) > 0 and x > s[-1]:  # s中有相同数字
                d[s.pop()] = x
            s.append(x)
        for i in range(len(nums1)):
            x = nums1[i]
            ans.append(d.get(x, -1))
        return ans


class Solution2:
    """加入时"""

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        s = []
        ans = []
        for i in reversed(range(len(nums2))):
            x = nums2[i]
            while len(s) > 0 and x > s[-1]:  # s中有相同数字
                s.pop()
            if len(s) > 0:
                # 若d[x] = s[0]. i < j; a[i] < a[j]; argmax[j](a[j])
                d[x] = s[-1]
            s.append(x)
        for i in range(len(nums1)):
            x = nums1[i]
            ans.append(d.get(x, -1))
        return ans


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(Solution().nextGreaterElement(nums1, nums2))
print(Solution2().nextGreaterElement(nums1, nums2))
