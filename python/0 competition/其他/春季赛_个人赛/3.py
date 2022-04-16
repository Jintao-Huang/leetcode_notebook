# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:
from typing import List, Optional
from python.template.build.build_tree import TreeNode, build_tree
from python.template.data_structure.segment_tree import SegmentTree


class Solution:
    def dfs(self, n: TreeNode, ans: List):
        if n is None:
            return
        self.dfs(n.left, ans)
        ans.append(n.val)
        self.dfs(n.right, ans)

    def getNumber(self, root: Optional[TreeNode], ops: List[List[int]]) -> int:
        ans = []
        self.dfs(root, ans)
        d = {}
        for i, x in enumerate(ans):
            d[x] = i
        st = SegmentTree([0] * len(ans))
        for o in ops:
            v, lo, hi = o
            st.update(d[lo], d[hi], v)
        return st.sumRange(0, len(ans) - 1)


root = build_tree("[1,null,2,null,3,null,4,null,5]")
ops = [[1, 2, 4], [1, 1, 3], [0, 3, 5]]
print(Solution().getNumber(root, ops))

# root = build_tree("[4,2,7,1,null,5,null,null,null,null,6]")
# ops = [[0, 2, 2], [1, 1, 5], [0, 4, 5], [1, 5, 7]]
# print(Solution().getNumber(root, ops))

root = build_tree("[4]")
ops = [[1, 4, 4]]
print(Solution().getNumber(root, ops))
