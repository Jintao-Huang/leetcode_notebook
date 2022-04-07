# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
"""
1. 考虑s为空的情况
"""

from typing import List

"""
1. 优化奇数一定不符合
"""


class Solution20:
    """有效的括号（典型的后进先出）"""

    def isValid(self, s: str) -> bool:
        """Ot(N) Os(N)"""
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif c == ')' and stack[-1] == '(':
                stack.pop()
            elif c == ']' and stack[-1] == '[':
                stack.pop()
            elif c == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
        return len(stack) == 0

    def isValid2(self, s: str) -> bool:
        """与1相似. Ot(N) Os(N)"""
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            elif len(stack) != 0:
                top = stack.pop()
                if c == ')' and top != '(' or \
                        c == ']' and top != '[' or \
                        c == '}' and top != '{':
                    return False
            else:
                return False
        return len(stack) == 0

    def isValid3(self, s: str) -> bool:
        """哈希表. Ot(N) Os(N + 符号集=6)"""
        if len(s) % 2 == 1:
            return False
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []
        for c in s:
            if c in pairs:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top != pairs[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0

    def isValid4(self, s: str) -> bool:
        """Ot(N) Os(N). 比2多了一句(奇数一定不满足)"""
        if len(s) % 2 == 1:
            return False
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            elif len(stack) != 0:
                top = stack.pop()
                if c == ')' and top != '(' or \
                        c == ']' and top != '[' or \
                        c == '}' and top != '{':
                    return False
            else:
                return False
        return len(stack) == 0


# string = "(({[]}"
# print(Solution20().isValid3(string))
# string = "{[]}))"
# print(Solution20().isValid3(string))
# string = "{[]}"
# print(Solution20().isValid3(string))

"""
1. 单调栈. 解决最近(最大等)-非递增栈。
  单调队列：解决区间最大-非递增/严格递减队列。
2. 顺序不同用hashMap
"""


class Solution496:
    """下一个最大元素I"""

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Ot(N2 + N1) Os(N2). 单调栈"""
        out = []
        fuzhu = {}  # 辅助字典
        stack = []  # 辅助栈. 单调递减栈
        for x in reversed(nums2):
            while len(stack) != 0 and stack[-1] < x:  # 不可能等于
                stack.pop()
            fuzhu[x] = -1 if len(stack) == 0 else stack[-1]
            stack.append(x)
        # print(fuzhu)  # {2: -1, 4: -1, 3: 4, 1: 3}
        for x in nums1:
            out.append(fuzhu[x])
        return out

    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Ot(N2 + N1) Os(N2). 单调栈（官方解法）"""
        out = []
        fuzhu = {}
        stack = []  # 单调递减栈
        for x in nums2:
            while len(stack) != 0 and stack[-1] < x:
                fuzhu[stack.pop()] = x
            stack.append(x)
        # print(fuzhu)  # {1: 3, 3: 4}
        for x in nums1:
            out.append(fuzhu.get(x, -1))
        return out


# nums1 = [4, 1, 2]
# nums2 = [1, 3, 4, 2]
# print(Solution496().nextGreaterElement2(nums1, nums2))  # [-1, 3, -1]

import heapq
import collections

"""
1. 单调双端队列
  单调栈
  堆
"""


class Solution239:
    """滑动窗口最大值"""

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """暴力. 超出时间限制"""
        res = []
        for i in range(len(nums) - k + 1):
            j = i + k
            res.append(max(nums[i:j]))

        return res

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        """用堆. Ot(NLogN) Os(N)"""
        res = []
        heap = [(-x, i) for i, x in enumerate(nums[:k])]  # 大根堆
        heapq.heapify(heap)
        res.append(-heap[0][0])

        for i in range(len(nums) - k):
            # i: 出, i+k: 入
            j = i + k
            heapq.heappush(heap, (-nums[j], j))
            while heap[0][1] <= i:
                heapq.heappop(heap)
            res.append(-heap[0][0])

        return res

    def maxSlidingWindow3(self, nums: List[int], k: int) -> List[int]:
        """用单调双端队列. Ot(N) Os(K)"""
        res = []
        q = collections.deque()  # 严格递减. 只存索引
        for i in range(k):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])

        for i in range(len(nums) - k):
            # i: 出. j: 入
            j = i + k
            while q and nums[q[-1]] <= nums[j]:
                q.pop()
            q.append(j)
            if q[0] == i:  # 或 <=
                q.popleft()
            res.append(nums[q[0]])
        return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(Solution239().maxSlidingWindow(nums, k))
print(Solution239().maxSlidingWindow2(nums, k))
print(Solution239().maxSlidingWindow3(nums, k))
