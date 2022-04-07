# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

"""
https://leetcode-cn.com/problems/n-queens/
51. N 皇后
- 困难
- 推荐
=
- 回溯
"""

from typing import List, Set


class Solution:
    """回溯"""
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        ru_diag, lu_diag = set(), set()  # right up, left up
        default_board = ['.'] * n  # type: List[str]  # one row

        #
        def _backtrack(choices: Set[int], track: List[int]) -> None:
            """

            :param choices: cols: [0, n)
            :param track: cols. 索引代表rows
            :return:
            """
            nonlocal ans, ru_diag, lu_diag, default_board
            if len(choices) == 0:
                # create_board
                board = []  # type: List[str]
                for j in track:
                    default_board[j] = 'Q'
                    board.append("".join(default_board))
                    default_board[j] = '.'
                #
                ans.append(board)
                return
            #
            r = len(track)  # [0, n)
            for c in list(choices):
                # 剪枝
                ru, lu = r + c, r - c
                if ru in ru_diag or lu in lu_diag:
                    continue
                #
                ru_diag.add(ru)
                lu_diag.add(lu)
                choices.remove(c)
                track.append(c)
                #
                _backtrack(choices, track)
                #
                track.pop()
                choices.add(c)
                lu_diag.remove(lu)
                ru_diag.remove(ru)

        _backtrack(set(range(n)), [])
        return ans


n = 4
print(Solution().solveNQueens(n))
