# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

from typing import List


class Solution1:
    """两数之和. 哈希表"""

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Ot(N) Os(N)"""
        d = {}
        for i, x in enumerate(nums):
            if x in d:
                return [d[x], i]
            else:
                d[target - x] = i

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """Ot(N^2) Os(1)"""
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


nums = [2, 7, 11, 15]
target = 9
print(Solution1().twoSum(nums, target))
print(Solution1().twoSum2(nums, target))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    """head不含头结点"""
    items = []
    p = head
    while p is not None:
        items.append(str(p.val))
        p = p.next
    print("LinkedList([%s])" % ', '.join(items))


"""
*1. 大数加法. carry语句的合并
"""


class Solution2:
    """两数相加. 链表, 大数"""

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """先转int. Ot(N1 + N2), Os(N1 + N2)"""
        n1, n2 = 0, 0
        i = 1
        while l1 is not None:
            n1 += l1.val * i
            i *= 10
            l1 = l1.next
        i = 1
        while l2 is not None:
            n2 += l2.val * i
            i *= 10
            l2 = l2.next
        l3 = ListNode(0, None)  # 头结点
        p = l3
        n3 = n1 + n2
        if n3 == 0:
            return l3
        while n3 > 0:
            x = n3 % 10
            n3 //= 10
            p.next = ListNode(x, None)
            p = p.next
        return l3.next

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """参考大数加法. Ot(N1 + N2), Os(N1 + N2)"""
        carry = 0
        p = l3 = ListNode(0, None)  # 头结点
        # 分开的思想: merge中
        while l1 is not None and l2 is not None:
            x = l1.val + l2.val + carry
            carry, x = divmod(x, 10)
            p.next = ListNode(x, None)
            p = p.next
            l1 = l1.next
            l2 = l2.next
            # print_list(l3.next)
        while l1 is not None:
            x = carry + l1.val
            carry, x = divmod(x, 10)
            p.next = ListNode(x, None)
            p = p.next
            l1 = l1.next
        while l2 is not None:
            x = carry + l2.val
            carry, x = divmod(x, 10)
            p.next = ListNode(x, None)
            p = p.next
            l2 = l2.next
        if carry:
            p.next = ListNode(carry, None)
        return l3.next

    def addTwoNumbers3(self, l1: ListNode, l2: ListNode) -> ListNode:
        """简化2. Ot(N1 + N2), Os(N1 + N2)"""
        carry = 0
        p = l3 = ListNode(0, None)  # 头结点
        # 分开的思想: merge中
        while l1 is not None or l2 is not None:
            val1 = 0 if l1 is None else l1.val
            val2 = 0 if l2 is None else l2.val
            x = val1 + val2 + carry
            carry, x = divmod(x, 10)
            p.next = ListNode(x, None)
            p = p.next
            l1 = l1 if l1 is None else l1.next
            l2 = l2 if l2 is None else l2.next
        if carry > 0:
            p.next = ListNode(carry, None)
        return l3.next

    def addTwoNumbers4(self, l1: ListNode, l2: ListNode) -> ListNode:
        """简化3. Ot(N1 + N2), Os(N1 + N2)"""
        carry = 0
        p = l3 = ListNode(0, None)  # 头结点
        # 分开的思想: merge中
        while l1 is not None or l2 is not None or carry > 0:
            x = carry
            if l1 is not None:
                x += l1.val
                l1 = l1.next
            if l2 is not None:
                x += l2.val
                l2 = l2.next
            carry, x = divmod(x, 10)
            p.next = ListNode(x, None)
            p = p.next

        return l3.next


# l1 = ListNode(0, None)
# l2 = ListNode(0, None)
# l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))
# l2 = ListNode(9, ListNode(9, ListNode(9, None)))
l1 = ListNode(2, ListNode(4, ListNode(3, None)))
l2 = ListNode(5, ListNode(6, ListNode(4, None)))
l3 = Solution2().addTwoNumbers(l1, l2)
print_list(l3)

l3 = Solution2().addTwoNumbers2(l1, l2)
print_list(l3)

l3 = Solution2().addTwoNumbers3(l1, l2)
print_list(l3)

l3 = Solution2().addTwoNumbers4(l1, l2)

print_list(l3)


class Solution20:
    """有效的括号. 见`数据机构的栈`"""
    pass


"""
*1. False or 执行. True and 执行
*2. extend链表时，直接接上就好了, 不需要循环
3. 能不创建新结点就不创建
"""


class Solution21:
    """合并两个有序链表. 链表, merge"""

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Ot(N1 + N2), Os(1)"""
        p = l3 = ListNode(0, None)  # 头结点
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        p.next = l1 or l2
        return l3.next

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """使用or合并. Ot(N1 + N2), Os(1)"""
        p = l3 = ListNode(0, None)  # 头结点
        while l1 is not None or l2 is not None:
            # False or 执行. True and 执行
            if l2 is None or l1 is not None and l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        return l3.next


l1 = ListNode(1, ListNode(2, ListNode(4, None)))
l2 = ListNode(1, ListNode(3, ListNode(4, None)))
l3 = Solution21().mergeTwoLists(l1, l2)
print_list(l3)

l1 = ListNode(1, ListNode(2, ListNode(4, None)))
l2 = ListNode(1, ListNode(3, ListNode(4, None)))
l3 = Solution21().mergeTwoLists2(l1, l2)
print_list(l3)


class Solution22:
    """括号生成"""

    def generateParenthesis(self, n: int) -> List[str]:
        pass
