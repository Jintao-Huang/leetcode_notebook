# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List, Tuple
from heapq import heapify, heapreplace, heappop
from template.build.build_list import ListNode, build_list, list_to_str


def _merge(nums_list: List[ListNode]) -> ListNode:
    # 多路归并
    n = len(nums_list)
    heap = []  # type: List[Tuple[int, int, ListNode]]
    for i in range(n):
        p = nums_list[i]
        if p is not None:
            heap.append((p.val, i, p))
    if len(heap) == 0:
        return None
    heapify(heap)
    #
    head = p2 = ListNode(0, None)
    while len(heap) > 1:
        val, i, p = heap[0]
        p2.next = p
        p2 = p2.next
        p = p.next
        if p is not None:
            heapreplace(heap, (p.val, i, p))
        else:
            heappop(heap)
    val, i, p = heap[0]
    p2.next = p
    return head.next


class Solution:
    """堆. Ot(NLogK) Os(K). 其中K=len(lists), N为总元素数."""

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return _merge(lists)


def merge2(p1: ListNode, p2: ListNode) -> ListNode:
    """mid: 是两个有序序列的分割点[lo, mid), [mid, hi]. Ot(N) Os(N)"""
    head = p = ListNode(0, None)
    while p1 is not None and p2 is not None:
        if p1.val <= p2.val:
            p.next = p1
            p1 = p1.next
        else:
            p.next = p2
            p2 = p2.next
        p = p.next
    if p1 is not None:
        p.next = p1
    else:
        p.next = p2
    return head.next


class Solution2:
    """dfs/分治法. Ot(NLogK) Os(K). 其中K=len(lists), N为总元素数."""

    def _dfs(self, lists: List[ListNode], lo: int, hi: int) -> ListNode:
        # [lo, hi]. 后序
        if lo == hi:
            return lists[lo]
        mid = lo + (hi - lo) // 2
        p1 = self._dfs(lists, lo, mid)
        p2 = self._dfs(lists, mid + 1, hi)
        return merge2(p1, p2)

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        return self._dfs(lists, 0, len(lists) - 1)


lists = [
    build_list("[1, 4, 5]"),
    build_list("[1, 3, 4]"),
    build_list("[2, 6]")
]
# lists = [build_list("[]")]
print(list_to_str(Solution().mergeKLists(lists)))
lists = [
    build_list("[1, 4, 5]"),
    build_list("[1, 3, 4]"),
    build_list("[2, 6]")
]
print(list_to_str(Solution2().mergeKLists(lists)))
