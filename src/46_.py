# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/permutations/
46. 全排列
- 中等
- 模板: 回溯
- 推荐
=
- 回溯
"""
from typing import List, Set


class Solution:
    """回溯"""
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def _backtrack(choices: Set[int], track: List[int]) -> None:
            nonlocal ans
            if len(choices) == 0:
                ans.append(track.copy())
                return
            #
            for c in list(choices):
                # no 剪枝
                #
                choices.remove(c)
                track.append(c)
                #
                _backtrack(choices, track)
                #
                track.pop()
                choices.add(c)

        _backtrack(set(nums), [])
        return ans


nums = [1, 2, 3]
print(Solution().permute(nums))
