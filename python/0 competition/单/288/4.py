# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
from typing import List
from collections import defaultdict
from python.template.data_structure.sorted_list import SortedList

# class Solution:
#     def maximumBeauty(
#             self,
#             flowers: List[int],
#             newFlowers: int,
#             target: int,
#             full: int,
#             partial: int
#     ) -> int:
#         # dp[i][j]. 完美花园数, 不完善最少数量: 所需要的最少新花
#         n = len(flowers)
#         d = defaultdict(int)
#         for f in flowers:
#             if f > target:
#                 f = target
#             d[f] += 1
#         if target not in d:
#             d[target] = 0
#         d.items()
#         sl = SortedList(list(d.items()))
#         ans = sl[0][0] * partial + sl[-1][1] * full
#         print(sl, ans)
#         # 最大: 不完美差1 + 都完美 ; 都完美
#         f = 0
#         for i in range(sl[-1][1], n):
#             x = sl.pop(-2)
#             sl[-1][1] += x
#             sl2 = sl.copy()
#             for j in range(sl[0][0], target):
#                 x2 = sl.pop(0)
#                 f += (sl2[0][0] * 2) * j
#                 sl2[0][1] += x2[1]





flowers = [1,3,1,1]
newFlowers = 7
target = 6
full = 12
partial = 1
print(Solution().maximumBeauty(flowers, newFlowers, target, full, partial))

flowers = [2,4,5,3]
newFlowers = 10
target = 5
full = 2
partial = 6
print(Solution().maximumBeauty(flowers, newFlowers, target, full, partial))


