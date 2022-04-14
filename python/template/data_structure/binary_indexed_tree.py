# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
class BinaryIndexedTree:
    def __init__(self, nums, is_zeros=False):
        n = len(nums)
        self.tree = [0] * n
        if not is_zeros:
            self._build_tree(nums)

    def lowbit(self, x):
        # return x & (~x + 1)
        # because of index 0
        x += 1
        return x & (-x)

    def _build_tree(self, nums):
        n = len(self.tree)
        for i in range(n):
            self.tree[i] += nums[i]
            p = i + self.lowbit(i)
            if p < n:
                self.tree[p] += self.tree[i]

    def prefix_sum(self, hi):
        ans = 0
        while hi >= 0:
            ans += self.tree[hi]
            hi -= self.lowbit(hi)
        return ans

    def sumRange(self, lo, hi):
        ans = self.prefix_sum(hi)
        if lo > 0:
            ans -= self.prefix_sum(lo)
        return ans

    def update(self, key, diff):
        n = len(self.tree)
        while key < n:
            self.tree[key] += diff
            key += self.lowbit(key)


if __name__ == '__main__':
    bit = BinaryIndexedTree([1, 2, 3, 4])
    print(bit.tree)
    bit.update(0, 1)
    print(bit.tree)
    print(bit.prefix_sum(3))
    print(bit.prefix_sum(0))
