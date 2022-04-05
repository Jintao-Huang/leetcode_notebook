# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

import heapq
from typing import List, Any
import collections

"""数组中的 第K/前K 个最大元素
方法1: 直接sorted排序(tim sort). Ot(NLogN) Os(N). 一般用于K = N时
方法2: 冒泡、选择. Ot(NK) Os(K). 一般用于K = 1时
方法3: 最小堆(剩下的为最大的n个. python官方实现). Ot(K + NLogK) Os(K). 一般用于K !<< N, K < N时（K较大）
方法4: 最大堆. Ot(N + KLogN) Os(1). 一般用于K较小时
"""


class Solution215:
    """数组中的第K个最大元素

    方法1: 直接sorted排序(tim sort). Ot(NLogN) Os(N). 一般用于K = N时
    方法2: 冒泡、选择. Ot(NK) Os(K). 一般用于K = 1时
    方法3: 最小堆(剩下的为最大的n个. python官方实现). Ot(K + NLogK) Os(K). 一般用于K !<< N, K < N时（K较大）
    方法4: 最大堆. Ot(N + KLogN) Os(1). 一般用于K较小时
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """sort(python中为tim sort). Ot(NLogN) Os(N)"""
        return sorted(nums, reverse=True)[k - 1]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        """最小堆. Ot(K + NLogK) Os(K)"""
        return heapq.nlargest(k, nums)[k - 1]

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        """最大堆. Ot(N + KLogN) Os(1)"""
        heapq._heapify_max(nums)
        for _ in range(k - 1):
            heapq._heappop_max(nums)
        return heapq._heappop_max(nums)

    @staticmethod
    def partition(arr: List[Any], lo: int, hi: int) -> int:
        """Ot(N) Os(1). [lo, hi)"""
        value = arr[lo]  # 取第一个
        hi -= 1
        while lo < hi:
            while lo < hi and arr[hi] >= value:
                hi -= 1
            arr[lo] = arr[hi]
            while lo < hi and arr[lo] <= value:
                lo += 1
            arr[hi] = arr[lo]
        arr[lo] = value
        return lo

    def mid_partition(self, arr: List[Any], lo: int, hi: int) -> int:
        mid = (lo + hi) // 2
        arr[lo], arr[mid] = arr[mid], arr[lo]
        return self.partition(arr, lo, hi)

    def _quick_select(self, arr: List[Any], k: int, lo: int, hi: int) -> int:
        """快速随机选择. Ot(N) Os(LogN)"""
        pivot = self.mid_partition(arr, lo, hi)
        if pivot == k:
            x = arr[pivot]
        elif pivot < k:
            x = self._quick_select(arr, k, pivot + 1, hi)
        else:
            x = self._quick_select(arr, k, lo, pivot)
        return x

    def findKthLargest4(self, nums: List[int], k: int) -> int:
        """快排划分法. Ot(N) Os(LogN)"""
        return self._quick_select(nums, len(nums) - k, 0, len(nums))


a = [1, 0, 7, 4, 2, 3, 6, 5, 8, 9]
print(Solution215().findKthLargest(a, 4))
print(Solution215().findKthLargest2(a, 4))
print(Solution215().findKthLargest3(a.copy(), 4))
print(Solution215().findKthLargest4(a, 4))


class CMP1:
    def __init__(self, word, num):
        self.word = word
        self.num = num

    def __lt__(self, other):
        return self.num > other.num or self.num == other.num and self.word < other.word


class CMP2:
    def __init__(self, word, num):
        self.word = word
        self.num = num

    def __lt__(self, other):
        return self.num < other.num or self.num == other.num and self.word > other.word


"""
*1. topK 最大堆 最小堆都可
2. CMP的使用
"""


class Solution692:
    """前K个高频单词"""

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """最大堆. Ot(L(N + K + MLogK + KLogK)) Os(L(M + K)). nsmallest中的sort有点问题"""
        d = {}
        for word in words:  # O(N)
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        arr = [(n, word) for word, n in d.items()]
        arr = heapq.nsmallest(k, arr, key=lambda x: (-x[0], x[1]))  # O(K + MLogK)
        arr.sort(key=lambda x: (-x[0], x[1]))  # O(KLogK)
        return [word for n, word in arr]

    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        """排序. Ot(L(N + MLogM)) Os(LM)"""
        d = {}
        for word in words:  # O(N)  # L为字符串平均长度, N为序列长度(len(words))
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        arr = [(n, word) for word, n in d.items()]
        arr.sort(key=lambda x: (-x[0], x[1]))  # O(MLogM), M为字符串种类数(len(arr))
        return [word for n, word in arr[:k]]

    def topKFrequent3(self, words: List[str], k: int) -> List[str]:
        """最大堆 + CMP"""
        # d = collections.Counter(words)
        d = {}
        for word in words:  # O(N)
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        arr = [CMP2(word, n) for word, n in d.items()]
        arr = heapq.nlargest(k, arr)  # 不用key的方法
        return [cmp.word for cmp in arr[:k]]

    def topKFrequent4(self, words: List[str], k: int) -> List[str]:
        """排序 + CMP"""
        d = collections.Counter(words)
        arr = [CMP1(word, n) for word, n in d.items()]
        arr.sort()
        return [cmp.word for cmp in arr[:k]]


w = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
print(Solution692().topKFrequent3(w, 4))

w = ["i", "love", "leetcode", "i", "love", "coding"]
print(Solution692().topKFrequent3(w, 2))

w = ["i", "love", "leetcode", "i", "love", "coding"]
print(Solution692().topKFrequent3(w, 3))
