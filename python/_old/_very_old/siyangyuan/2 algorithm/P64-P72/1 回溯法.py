# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from functools import lru_cache
from typing import List

"""
1. 递归复杂度: 等于 递归结点数 * 每个结点复杂度

"""


class Solution22:
    """括号生成"""

    def generateParenthesis(self, n: int) -> List[str]:
        """回溯法1. Ot(^)"""
        res = []

        def _generateParenthesis(s: str, left: int, right: int) -> None:
            if left < right or left > n or right > n:
                return
            if left >= right:
                if left == right == n:
                    res.append(s)
                    return
                _generateParenthesis(s + '(', left + 1, right)
                _generateParenthesis(s + ')', left, right + 1)

        _generateParenthesis('', 0, 0)
        return res

    def generateParenthesis2(self, n: int) -> List[str]:
        """回溯法2. O(^)"""

        def _generateParenthesis(_n: int) -> List[str]:
            if _n == 0:
                return ['']
            ans = []
            for c in range(_n):
                mid = _generateParenthesis(c)
                right = _generateParenthesis(_n - 1 - c)
                for m in mid:
                    for r in right:
                        ans.append('({}){}'.format(m, r))
            return ans

        return _generateParenthesis(n)


print(Solution22().generateParenthesis(3))
print(Solution22().generateParenthesis2(3))


class Solution78:
    """子集"""

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """分治法. Ot(^)"""

        def merge(s1: List[List[int]], s2: List[List[int]]) -> List[List[int]]:
            s = []
            for i in range(0, len(s1)):
                for j in range(0, len(s2)):
                    s.append(s1[i] + s2[j])
            return s

        def _subsets(_nums: List[int], lo: int, hi: int) -> List[List[int]]:
            if hi - lo == 1:
                return [[], [_nums[lo]]]
            mid = (lo + hi) // 2
            s1 = _subsets(nums, lo, mid)
            s2 = _subsets(nums, mid, hi)
            return merge(s1, s2)

        return _subsets(nums, 0, len(nums))

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        """扩展法. Ot(^)"""
        res = [[]]
        for i in range(len(nums)):
            for j in range(len(res)):  # len()语句只会执行一次. 与`in res`不同
                res.append(res[j] + [nums[i]])  # 隐含着拷贝的操作

        return res

    def subsets3(self, nums: List[int]) -> List[List[int]]:
        """回溯法1. Ot(^)"""
        res = []
        s = []

        def _subsets(idx: int) -> None:
            res.append(s.copy())
            if idx == len(nums):
                return
            for i in range(idx, len(nums)):
                s.append(nums[i])
                _subsets(i + 1)
                s.pop()

        _subsets(0)
        return res

    def subsets4(self, nums: List[int]) -> List[List[int]]:
        """回溯法2. Ot(^)"""
        res = []
        s = []

        def _subsets(idx: int) -> None:
            # length代表 长度最长为length的子集
            if idx == len(nums):
                res.append(s.copy())
                return
            s.append(nums[idx])
            _subsets(idx + 1)  # 选择当前位置
            s.pop()
            _subsets(idx + 1)  # 不选择当前位置

        _subsets(0)
        return res


nums = [1, 2, 3]
print(Solution78().subsets(nums))
print(Solution78().subsets2(nums))
print(Solution78().subsets3(nums))
print(Solution78().subsets4(nums))


class Solution77:
    """组合"""

    def combine(self, n: int, k: int) -> List[List[int]]:
        """回溯法1. Ot(^)"""
        res = []
        c = []

        def _combine(idx: int) -> None:
            if len(c) + n - idx < k:  # 剪枝
                return
            if k == len(c):
                res.append(c.copy())
                return
            for i in range(idx, n):
                c.append(i + 1)
                _combine(i + 1)
                c.pop()

        _combine(0)
        return res

    def combine2(self, n: int, k: int) -> List[List[int]]:
        """回溯法2. Ot(^)"""
        res = []
        c = []  # 类似深搜，所以只需要全局变量

        def _combine(idx: int) -> None:
            if len(c) + n - idx < k:  # 剪枝
                return
            # if idx > n:
            #     return
            if k == len(c):
                res.append(c.copy())
                return
            c.append(idx + 1)
            _combine(idx + 1)  # 选idx
            c.pop()
            _combine(idx + 1)  # 不选idx

        _combine(0)
        return res


print(Solution77().combine(4, 2))
print(Solution77().combine2(4, 2))

print("-------------------------")


class Solution46:
    """全排列"""

    def permute(self, nums: List[int]) -> List[List[int]]:
        """回溯法1. Ot(^)"""
        s = set(nums)
        p = []
        res = []

        def _permute() -> None:
            if len(p) == len(nums):
                res.append(p.copy())
                return
            for x in s.copy():
                s.remove(x)
                p.append(x)
                _permute()
                p.pop()
                s.add(x)

        _permute()
        return res

    def permute2(self, nums: List[int]) -> List[List[int]]:
        """回溯法2. Ot(^)"""
        res = []

        def _permute(idx: int) -> None:
            if idx + 1 == len(nums):
                res.append(nums.copy())
                return
            for i in range(idx, len(nums)):
                nums[i], nums[idx] = nums[idx], nums[i]
                _permute(idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]

        _permute(0)
        return res


print(Solution46().permute([1, 2, 3]))
print(Solution46().permute2([1, 2, 3]))


class Solution51:
    """N皇后"""

    def solveNQueens(self, n: int) -> List[List[str]]:
        """回溯法. O(^)"""
        res = []
        queens = []  # int
        cols = set()  # 含: NO
        right_diag = set()  # to right down
        left_diag = set()  # to left down
        temp = ['.'] * n

        def to_board() -> List[str]:
            out = []
            for c in queens:
                temp[c] = 'Q'
                out.append(''.join(temp))
                temp[c] = '.'
            return out

        def _solveNQueens(r: int) -> None:
            if r == n:
                res.append(to_board())
            for c in range(n):
                if c in cols or (c - r) in right_diag or (r + c) in left_diag:
                    continue
                queens.append(c)
                cols.add(c)
                right_diag.add(c - r)
                left_diag.add(r + c)
                _solveNQueens(r + 1)
                queens.pop()
                cols.remove(c)
                right_diag.remove(c - r)
                left_diag.remove(r + c)

        _solveNQueens(0)
        return res


print(Solution51().solveNQueens(4))
print(len(Solution51().solveNQueens(8)))  # 92


class Solution52:
    """N皇后2"""

    def totalNQueens(self, n: int) -> int:
        """回溯法. O(^)"""
        res = 0
        cols = set()  # 含: NO
        right_diag = set()  # to right down
        left_diag = set()  # to left down

        def _solveNQueens(r: int) -> None:
            nonlocal res
            if r == n:
                res += 1
            for c in range(n):
                if c in cols or (c - r) in right_diag or (r + c) in left_diag:
                    continue
                cols.add(c)
                right_diag.add(c - r)
                left_diag.add(r + c)
                _solveNQueens(r + 1)
                cols.remove(c)
                right_diag.remove(c - r)
                left_diag.remove(r + c)

        _solveNQueens(0)
        return res

    res = [-1, 1, 0, 0, 2, 10, 4, 40, 92, 352]

    def totalNQueens2(self, n: int) -> int:
        return self.res[n]


l = []
for i in range(10):
    l.append(Solution52().totalNQueens(i))  # [-1, 1, 0, 0, 2, 10, 4, 40, 92, 352]
print(l)

print(Solution52().totalNQueens(8))
print(Solution52().totalNQueens2(8))


class Solution36:
    """有效的数独"""

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Ot(N^2) Os(N^2)"""
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x == '.':
                    continue
                x = int(x)
                bi = i // 3 * 3 + j // 3
                if x in rows[i] or x in cols[j] or x in boxes[bi]:
                    return False
                rows[i].add(x)
                cols[j].add(x)
                boxes[bi].add(x)
        return True


board = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
         [".", "4", ".", "3", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "3", ".", ".", "1"],
         ["8", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", ".", "2", ".", "7", ".", ".", ".", "."],
         [".", "1", "5", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "2", ".", ".", "."],
         [".", "2", ".", "9", ".", ".", ".", ".", "."],
         [".", ".", "4", ".", ".", ".", ".", ".", "."]]

print(Solution36().isValidSudoku(board))

"""
回溯的两种题型：
1. 找到全部符合的情况
2. 找到一种就返回
"""


class Solution37:
    """解数独"""

    def solveSudoku(self, board: List[List[str]]) -> None:
        """回溯法. Ot(^)"""
        rows = [set(range(1, 10)) for _ in range(9)]  # 没有
        cols = [set() for _ in range(9)]  # 有
        boxes = [set() for _ in range(9)]  # 有
        pos_list = []
        valid = False
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    pos_list.append((i, j))
                else:
                    x = int(board[i][j])
                    bi = i // 3 * 3 + j // 3
                    rows[i].remove(x)
                    cols[j].add(x)
                    boxes[bi].add(x)

        del i, j, x, bi

        def _solveSudoku(pos) -> None:
            nonlocal valid
            if pos == len(pos_list):
                valid = True
                return

            r, c = pos_list[pos]
            bi = r // 3 * 3 + c // 3
            for x in rows[r].copy():
                if x in cols[c] or x in boxes[bi]:
                    continue
                rows[r].remove(x)
                cols[c].add(x)
                boxes[bi].add(x)
                board[r][c] = str(x)
                _solveSudoku(pos + 1)
                if valid:
                    return
                boxes[bi].remove(x)
                cols[c].remove(x)
                rows[r].add(x)

        _solveSudoku(0)

    def solveSudoku2(self, board: List[List[str]]) -> None:
        # 类似与hashMap: int -> bool
        line = [[False] * 9 for _ in range(9)]
        column = [[False] * 9 for _ in range(9)]
        block = [[[False] * 9 for _a in range(3)] for _b in range(3)]
        valid = False
        spaces = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))
                else:
                    x = int(board[i][j]) - 1
                    line[i][x] = column[j][x] = block[i // 3][j // 3][x] = True
        del i, j, x

        def _solveSudoku(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return

            i, j = spaces[pos]
            for x in range(9):
                if line[i][x] == column[j][x] == block[i // 3][j // 3][x] == False:
                    line[i][x] = column[j][x] = block[i // 3][j // 3][x] = True
                    board[i][j] = str(x + 1)
                    _solveSudoku(pos + 1)
                    if valid:
                        return
                    line[i][x] = column[j][x] = block[i // 3][j // 3][x] = False

        _solveSudoku(0)


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
board1 = [r.copy() for r in board]
Solution37().solveSudoku(board)
print(board)

Solution37().solveSudoku2(board1)
print(board1)
