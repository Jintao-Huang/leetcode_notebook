# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
*1. 加入头结点
2. 先捋顺所有的分支(if else), 再优化
  e.g. 缩减分支(pass)/相同代码块外提
*3. 插入、删除都需要prev
"""


class Solution203:
    """移除链表元素"""

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """Ot(N) Os(1)"""
        head = ListNode(0, head)  # 添加头结点, val无意义
        prev = head
        while prev.next is not None:
            p = prev.next
            if p.val == val:
                prev.next = p.next
            else:  # 注意!
                prev = p

        return head.next


def print_list(head):
    """head不含头结点"""
    items = []
    p = head
    while p is not None:
        items.append(str(p.val))
        p = p.next
    print("LinkedList([%s])" % ', '.join(items))


# [1, 2, 6, 3, 4, 5, 6]
head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))))
head = Solution203().removeElements(head, 6)  # [1, 2, 3, 4, 5]

print_list(head)
print("-----------------")

head = ListNode(7, ListNode(7, ListNode(7, ListNode(7, None))))
head = Solution203().removeElements(head, 7)  # []

print_list(head)

"""
1. 省略pre指针不要在前面做。在优化阶段做/不做
*2. 双指针思想
3. 判断条件为索引越界/属性访问服务
"""


class Solution206:
    """反转链表"""

    def reverseList(self, head: ListNode) -> ListNode:
        """Ot(N) Os(N). 创建新列表."""
        p = head
        ans = None
        while p is not None:
            ans = ListNode(p.val, ans)
            p = p.next
        return ans

    def reverseList2(self, head: ListNode) -> ListNode:
        """Ot(N) Os(1). 双指针. 不需要头结点"""
        p_new = None
        p = head
        while p is not None:
            n = p.next
            p.next = p_new
            p_new = p
            p = n
        return p_new

    def reverseList3(self, head: ListNode) -> ListNode:
        """Ot(N) Os(1). 推荐 含头结点"""
        p = head
        head = ListNode(0, None)  # 头结点(for return)
        while p is not None:
            n = p.next
            p.next = head.next
            head.next = p
            p = n
        return head.next

    def reverseList4(self, head: ListNode) -> ListNode:
        """递归. Ot(N) Os(N)"""

        def _reverseList(_head: ListNode) -> ListNode:
            if _head is None or _head.next is None:
                return _head
            n = _head.next
            p = _head
            _head = _reverseList(p.next)
            n.next = p
            p.next = None
            return _head

        return _reverseList(head)


# [1, 2, 3, 4, 5]
print("-----------------")
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
head = ListNode(1, ListNode(2, None))
print_list(head)  # [5, 4, 3, 2, 1]
head = Solution206().reverseList4(head)
print_list(head)  # [5, 4, 3, 2, 1]

head = None
head = Solution206().reverseList(head)
head = Solution206().reverseList2(head)
head = Solution206().reverseList3(head)
head = Solution206().reverseList4(head)
