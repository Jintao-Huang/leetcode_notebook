# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


def find(arr: List[int], target: int):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def reverse(arr: List[int], lo: int, hi: int) -> None:
    """[lo, hi]"""
    while lo < hi:
        arr[lo], arr[hi] = arr[hi], arr[lo]
        lo += 1
        hi -= 1


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []
        for i in reversed(range(n)):
            if arr[i] != i + 1:
                idx = find(arr, i + 1)
                ans.append(idx + 1)
                ans.append(i + 1)
                reverse(arr, 0, idx)
                reverse(arr, 0, i)

        return ans


print(Solution().pancakeSort([3, 2, 4, 1]))
