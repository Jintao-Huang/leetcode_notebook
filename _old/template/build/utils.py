# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import Optional, Union, List
import json


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def build_circle_list(list_: Union[str, List[int]], pos: int) -> Optional[ListNode]:
    """pos=-1: 没有环. 142."""
    list_ = json.loads(list_)  # type: List[int]
    if not len(list_):
        return
    #
    prev = dummy = ListNode(0)  # head = dummy.next. dummy node: 哑节点
    memo = None  # type: Optional[ListNode]
    #
    for i in range(len(list_)):
        node = list_[i]
        prev.next = ListNode(node)
        prev = prev.next
        #
        if i == pos:
            memo = prev
    #
    if memo is not None:
        prev.next = memo
    return dummy.next
