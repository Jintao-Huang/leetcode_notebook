# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import Optional, List
import json


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next

    def __str__(self):
        return list_to_str(self)


def list_to_str(head: Optional[ListNode]) -> str:
    ans = []
    #
    while head is not None:
        ans.append(head.val)
        head = head.next

    return json.dumps(ans)


def build_list(list_: str) -> Optional[ListNode]:
    if isinstance(list_, str):
        list_ = json.loads(list_)  # type: List[int]
    if not len(list_):
        return
    prev = head = ListNode(list_[0])
    for node in list_[1:]:
        prev.next = ListNode(node)
        prev = prev.next
    return head


if __name__ == '__main__':
    list_ = "[3,2,0,-4]"
    head = build_list(list_)
    print(list_to_str(head))  # [3, 2, 0, -4]
