# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

import json
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def tree_to_str(root: Optional[TreeNode]) -> str:
    if root is None:
        return "[]"

    ans = []
    q = deque([root])
    while len(q) > 0:
        all_None = True
        for i in range(len(q)):
            n = q.popleft()
            if n is None:
                ans.append(None)
                continue
            ans.append(n.val)
            q.append(n.left)
            q.append(n.right)
            if n.left or n.right:
                all_None = False
        if all_None:
            break
    while ans[-1] is None:
        ans.pop()

    return json.dumps(ans)


def build_tree(tree: str) -> Optional[TreeNode]:
    l = json.loads(tree)
    if len(l) == 0:
        return None

    root = TreeNode(l[0], None, None)
    q = deque([(root, "left"), (root, "right")])
    for i in range(1, len(l)):
        x = l[i]
        n = None if x is None else TreeNode(x, None, None)
        p, s = q.popleft()
        setattr(p, s, n)
        if n is not None:
            q.append((n, "left"))
            q.append((n, "right"))
    return root


# test
if __name__ == '__main__':
    tree = "[-10, 9, 20, null, null, 15, 7]"

    root = build_tree(tree)
    print(tree_to_str(root))  # [-10, 9, 20, null, null, 15, 7]
