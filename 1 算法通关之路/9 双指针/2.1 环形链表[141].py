# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 


from template.build.other import ListNode, build_circle_list


class Solution:
    """双指针-快慢. Ot(N) Os(1).
    同类型题目见 `3.2回文链表[234]`"""

    def hasCycle(self, head: ListNode) -> bool:
        p, p2 = head, head
        # 也可以是 while p2.next is not None and p2.next.next is not None:
        # 但需要在上面对 head is None 进行测试.
        while p2 is not None and p2.next is not None:
            p = p.next
            p2 = p2.next.next
            if p == p2:
                return True
        return False


class Solution2:
    """哈希表. Ot(N) Os(N)"""

    def hasCycle(self, head: ListNode) -> bool:
        p = head
        s = set()
        while p is not None:
            s.add(p)
            p = p.next
            if p in s:
                return True
        return False
