# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


"""
https://leetcode-cn.com/problems/permutations-ii/
47. 全排列 II
- 中等
=
- 回溯
"""

from typing import List, Dict


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        #
        choices = {}
        for x in nums:
            if x not in choices:
                choices[x] = 0
            choices[x] += 1

        #
        def _backtrack(choices: Dict[int, int], track: List[int]) -> None:
            nonlocal ans
            if len(choices) == 0:
                ans.append(track.copy())
                return
            #
            for c in list(choices.keys()):
                #
                choices[c] -= 1
                if choices[c] == 0:
                    choices.pop(c)
                track.append(c)
                #
                _backtrack(choices, track)
                #
                track.pop()
                if c not in choices.keys():
                    choices[c] = 0
                choices[c] += 1

        _backtrack(choices, [])
        return ans


nums = [1, 1, 2]
print(Solution().permuteUnique(nums))
