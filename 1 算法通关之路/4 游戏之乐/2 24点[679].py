# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Set, Tuple, Union, Dict


def counter(nums: List[int], need_sorted: bool = False) -> Union[Dict, List[List[int]]]:
    """返回 按字典序."""
    d = {}
    for x in nums:
        if x not in d:
            d[x] = 0
        d[x] += 1
    #
    if need_sorted:
        keys = sorted(d.keys())
        return [[k, d[k]] for k in keys]
    else:
        return d


def permute(nums: List[int]) -> List[List[int]]:
    """含去重. """
    ans = []  # type: List[List[int]]
    target = len(nums)
    nums = counter(nums, need_sorted=True)

    def dfs(nums: List[List[int]], path: List[int], target: int) -> None:
        # 选择: nums
        """选择+路径. """
        if len(path) == target:
            ans.append(path.copy())
            return
        for i in range(len(nums)):
            x = nums[i]
            if not x[1]:
                continue
            x[1] -= 1
            path.append(x[0])
            dfs(nums, path, target)
            x[1] += 1
            path.pop()

    dfs(nums, [], target)
    return [list(a) for a in ans]


class Solution:
    """全排列回溯+24点回溯/搜索. 优势: 全排列含去重."""

    def _dfs(self, nums: List[float]) -> bool:
        # 选择: 算哪一个位置 and 加减乘除
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
                if self._dfs(new_nums):
                    return True
        return False

    def judgePoint24(self, cards: List[int]) -> bool:
        ps = permute(cards)
        for p in ps:
            if self._dfs(p):
                return True
        return False


print(Solution().judgePoint24([1, 5, 5, 5]))
print(Solution().judgePoint24([1, 1, 1, 1]))


class Solution2:
    """24点直接搜索.
    优势: 去除加法乘法结合率的重复运算. 全排列的冗余运算(也可以用生成器优化).
    缺点: 重复元素全排列的出现"""

    def _dfs(self, nums: List[float]) -> bool:
        # 选择: 算哪两个位置 and 加减乘除.
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
                if self._dfs(new_nums):
                    return True

                new_nums[0] = x - y
                if self._dfs(new_nums):
                    return True
                new_nums[0] = y - x
                if self._dfs(new_nums):
                    return True
                new_nums[0] = x * y
                if self._dfs(new_nums):
                    return True

                if y != 0:
                    new_nums[0] = x / y
                    if self._dfs(new_nums):
                        return True
                if x != 0:
                    new_nums[0] = y / x
                    if self._dfs(new_nums):
                        return True
        return False

    def judgePoint24(self, cards: List[int]) -> bool:
        return self._dfs(cards)


print(Solution2().judgePoint24([1, 5, 5, 5]))
print(Solution2().judgePoint24([1, 1, 1, 1]))
