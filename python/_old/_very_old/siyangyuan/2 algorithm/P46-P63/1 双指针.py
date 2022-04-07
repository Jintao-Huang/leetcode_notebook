# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
1. and的妙用. (同merge)
2. 快慢双指针
"""


class Solution141:
    """环形链表"""

    def hasCycle(self, head: ListNode) -> bool:
        """哈希表. Ot(N) Os(N)"""
        s = set()
        p = head
        while p is not None:
            if p in s:
                return True
            else:
                s.add(p)
            p = p.next
        return False

    def hasCycle2(self, head: ListNode) -> bool:
        """快慢双指针. Ot(N) Os(1)"""
        p1 = p2 = head
        if p2 is None:
            return False
        p2 = p2.next
        while p2 is not None and p2.next is not None:
            if p1 == p2:
                return True
            p1 = p1.next
            p2 = p2.next.next
        return False

    def hasCycle3(self, head: ListNode) -> bool:
        """快慢双指针 写法2. Ot(N) Os(1)"""
        p1 = p2 = head
        if p2 is None:
            return False
        p2 = p1.next
        while p1 != p2:
            if p2 is None or p2.next is None:
                return False
            p1 = p1.next
            p2 = p2.next.next

        return True


l1 = ListNode(1, ListNode(2, ListNode(4, None)))
l2 = ListNode(1, ListNode(2, None))
l2.next.next = l2
l3 = None
print(Solution141().hasCycle2(l1))
print(Solution141().hasCycle2(l2))
print(Solution141().hasCycle2(l3))
print(Solution141().hasCycle3(l1))
print(Solution141().hasCycle3(l2))
print(Solution141().hasCycle3(l3))

"""
1. 对撞双指针
"""


class Solution167:
    """两数之和 II - 输入有序数组. 其余方法见上(哈希表 Ot(N) Os(N))"""

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """对撞双指针. Ot(N) Os(1)"""
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i + 1, j + 1]

    def binary_search(self, arr: List[int], x: int, lo: int = 0, hi: int = None) -> int:
        """没找到返回-1"""
        hi = len(arr) if hi is None else hi
        while lo < hi:
            mid = (lo + hi) // 2
            if x == arr[mid]:
                return mid
            elif x > arr[mid]:
                lo = mid + 1
            else:
                hi = mid
        return -1

    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        """暴力法(二分搜索). Ot(NLogN) Os(1)"""
        length = len(numbers)
        for i in range(length):
            j = self.binary_search(numbers, target - numbers[i], i + 1, length)
            if j != -1:
                return [i + 1, j + 1]


numbers = [2, 7, 11, 15]
target = 9
print(Solution167().twoSum(numbers, target))
print(Solution167().twoSum2(numbers, target))

"""
1. 对撞双指针
2. 贪心
"""


class Solution881:
    """救生艇"""

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """贪心 对撞双指针. Ot(NLogN) Os(N)"""
        people.sort()
        i, j = 0, len(people) - 1
        n = 0  # 船数
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            n += 1
        return n


people = [3, 5, 3, 4]
limit = 5
print(Solution881().numRescueBoats(people, limit))  # 4
