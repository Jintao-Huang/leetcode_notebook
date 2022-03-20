# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List
class Solution:
    """贪心. Ot(N) Os(1)"""
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 选择: 停机限制/任务数限制
        d = {}
        for i in range(len(tasks)):
            t = tasks[i]
            if t not in d:
                d[t] = 0
            d[t] += 1
        #
        max_cnt = 0
        max_ = max(d.values())
        for k in d.keys():
            if max_ == d[k]:
                max_cnt += 1
        return max((max_ - 1) * (n + 1) + max_cnt, len(tasks))
