# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

import json
from typing import List, Union, Optional, Deque, Tuple, Sequence
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # type: int
        self.left = left  # type: TreeNode
        self.right = right  # type: TreeNode


def tree_to_str(root: Optional[TreeNode]) -> str:
    ans = []
    if root is None:
        return json.dumps(ans)

    #
    def _all_None(x: Sequence[Optional[TreeNode]], start: int, end: int) -> bool:
        ans = True
        x = list(x)
        for i in range(start, end):
            node = x[i]
            if node is not None:
                ans = False
        return ans

    #
    q = deque([root])  # type: Deque[Optional[TreeNode]]
    #
    while len(q):
        sz = len(q)
        #
        if _all_None(q, 0, sz):
            break
        #
        for i in range(sz):
            node = q.popleft()  # type: TreeNode
            if node is None:
                ans.append(None)
                q.append(None)
                q.append(None)
            else:
                ans.append(node.val)
                q.append(node.left)
                q.append(node.right)
            #
    return json.dumps(ans)


def build_tree(tree: Union[str]) -> Optional[TreeNode]:
    tree = json.loads(tree)  # type: List[int]
    #
    if not len(tree):
        return
    #
    root = TreeNode(tree[0])
    q = deque([(root, "left"), (root, "right")])  # type: Deque[Tuple[TreeNode, str]]
    for node in tree[1:]:
        if node is None:
            q.popleft()
            continue
        #
        node = TreeNode(node)
        setattr(*q.popleft(), node)
        #
        q.append((node, "left"))
        q.append((node, "right"))
    return root


# test
tree = "[-10, 9, 20, null, null, 15, 7]"

root = build_tree(tree)
print(tree_to_str(root))  # [-10, 9, 20, null, null, 15, 7]
