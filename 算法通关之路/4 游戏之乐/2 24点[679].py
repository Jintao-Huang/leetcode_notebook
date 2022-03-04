# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Set, Tuple


# def permute(nums: List[int]) -> List[List[int]]:
#     """nums不重复才行"""
#     ans = []  # type: List[List[int]]
#
#     def backtrace(nums: Set[int], trace: List[int]) -> None:
#         """选择+路径. """
#         if len(nums) == 0:
#             ans.append(trace.copy())
#             return
#         for x in nums.copy():
#             nums.remove(x)
#             trace.append(x)
#             backtrace(nums, trace)
#             nums.add(x)
#             trace.pop()
#
#     backtrace(set(nums), [])
#     return ans


def permute2(nums: List[int]) -> List[List[int]]:
    """含去重. """
    ans = set()  # type: Set[Tuple[int]]
    visited = [False] * len(nums)

    def backtrace(nums: List[int], trace: List[int]) -> None:
        """选择+路径. """
        if len(trace) == len(nums):
            ans.add(tuple(trace))
            return
        for i in range(len(nums)):
            if visited[i]:
                continue
            visited[i] = True
            trace.append(nums[i])
            backtrace(nums, trace)
            visited[i] = False
            trace.pop()

    backtrace(nums, [])
    return [list(a) for a in ans]


class Solution:
    """全排列回溯+24点回溯/搜索. 优势: 全排列含去重."""

    def compute(self, nums: List[float]) -> bool:
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-8

        for i in range(len(nums) - 1):
            tmp = []  # 四则运算结果
            x, y = nums[i], nums[i + 1]
            tmp.append(x + y)
            tmp.append(x - y)
            tmp.append(x * y)
            if y != 0:
                tmp.append(x / y)
            #
            new_nums = nums.copy()
            new_nums.pop(i)
            for t in tmp:
                new_nums[i] = t
                if self.compute(new_nums):
                    return True
        return False

    def judgePoint24(self, cards: List[int]) -> bool:
        ps = permute2(cards)
        for p in ps:
            if self.compute(p):
                return True
        return False


print(Solution().judgePoint24([1, 5, 5, 5]))
print(Solution().judgePoint24([1, 1, 1, 1]))


class Solution2:
    """24点直接搜索.
    优势: 去除加法乘法结合率的重复运算. 全排列的冗余运算(也可以用生成器优化).
    缺点: 重复元素全排列的出现"""

    def compute(self, nums: List[float]) -> bool:
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-8
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                x, y = nums[i], nums[j]
                new_nums = [0]  # 0 用作放 x,y 运算结果
                for k in range(len(nums)):
                    if k != i and k != j:
                        new_nums.append(nums[k])
                #
                new_nums[0] = x + y
                if self.compute(new_nums):
                    return True

                new_nums[0] = x - y
                if self.compute(new_nums):
                    return True
                new_nums[0] = y - x
                if self.compute(new_nums):
                    return True
                new_nums[0] = x * y
                if self.compute(new_nums):
                    return True

                if y != 0:
                    new_nums[0] = x / y
                    if self.compute(new_nums):
                        return True
                if x != 0:
                    new_nums[0] = y / x
                    if self.compute(new_nums):
                        return True
        return False

    def judgePoint24(self, cards: List[int]) -> bool:
        return self.compute(cards)


print(Solution2().judgePoint24([1, 5, 5, 5]))
print(Solution2().judgePoint24([1, 1, 1, 1]))
