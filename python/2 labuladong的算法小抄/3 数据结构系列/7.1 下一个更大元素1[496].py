from typing import List


class Solution:
    """单调栈. """

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 严格大于.
        d = {}
        s = []  # 值
        ans = []
        for hi in range(len(nums2)):
            x = nums2[hi]
            while len(s) > 0 and x >= s[-1]:
                d[s.pop()] = x
            s.append(x)
        #
        for i in range(len(nums1)):
            x = nums1[i]
            ans.append(d.get(x, -1))
        return ans


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(Solution().nextGreaterElement(nums1, nums2))
