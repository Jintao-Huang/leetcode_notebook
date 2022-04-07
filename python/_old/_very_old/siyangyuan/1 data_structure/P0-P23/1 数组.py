# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from typing import List

"""
*1. 加尾哨兵的思路。 
  当然也可以在出循环/返回时加上max()
2. 可能需要判断输入合法:
  e.g. 不是None，长度>0
"""


class Solution485:
    """最大连续1的个数"""

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """Ot(N) Os(1). 哨兵"""
        max_ = 0
        length = 0
        nums.append(0)  # 哨兵
        for n in nums:
            if n == 1:
                length += 1
            else:
                max_ = max(length, max_)
                length = 0
        return max_

    def findMaxConsecutiveOnes2(self, nums: List[int]) -> int:
        """Ot(N) Os(1)"""
        max_ = 0
        length = 0
        for n in nums:
            if n == 1:
                length += 1
            else:
                max_ = max(length, max_)
                length = 0
        return max(length, max_)


# l = [1, 1, 0, 1, 1, 1]
# print(Solution485().findMaxConsecutiveOnes2(l))  # 3


"""
1. 双指针的思想
*2. 覆盖代替pop. 相当于一个假象的辅助数组
*3. 交换的思想(与覆盖相对应)
"""


class Solution283:
    """移动零"""

    def moveZeroes(self, nums: List[int]) -> None:
        """Ot(N) Os(1). 覆盖"""
        i = 0
        for n in nums:
            if n != 0:
                nums[i] = n
                i += 1
        for i in range(i, len(nums)):
            nums[i] = 0

    def moveZeroes2(self, nums: List[int]) -> None:
        """Ot(N) Os(1). 交换"""
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1


# l = [0, 1, 0, 3, 12]
# Solution283().moveZeroes2(l)
# print(l)  # [1, 3, 12, 0, 0]

"""
1. 双指针
*2. 覆盖
"""


class Solution27:
    """移除元素. 与283类似"""

    def removeElement(self, nums: List[int], val: int) -> int:
        """Ot(N) Os(1). 覆盖"""
        i = 0
        for n in nums:  # （为什么会比range慢??？）
            if n != val:
                # 不需要判断nums[i], n是不是在同一位置，因为赋值是便宜的
                nums[i] = n
                i += 1
        # for _ in range(i, len(nums)):
        #     nums.pop()
        return i
        # 5
        # [0, 1, 3, 0, 4, 0, 4, 2]

    def removeElement2(self, nums: List[int], val: int) -> int:
        """Ot(N) Os(1). 交换(相比于覆盖的作用是保留被覆盖的元素信息)"""
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        # for _ in range(i, len(nums)):
        #     nums.pop()
        return i

    def removeElement3(self, nums: List[int], val: int) -> int:
        """Ot(N) Os(1). 覆盖(交换改)"""
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        # for _ in range(i, len(nums)):
        #     nums.pop()
        return i

# l = [3, 2, 2, 3]
# print(Solution27().removeElement3(l, 3))  # 2
# print(l)  # [2, 2]
#
# l = [0, 1, 2, 2, 3, 0, 4, 2]
# print(Solution27().removeElement3(l, 2))  # 5
# print(l)  # [0, 1, 3, 0, 4]
