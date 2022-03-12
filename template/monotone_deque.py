# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

from typing import List


# 单调栈

# ge -> le: > <. 递减栈 -> 递增栈
# ge -> gt: > >=
# next -> prev: reverse -> no reverse, lo -> hi

def next_ge(nums: List[int]) -> List[int]:
    ans = [-1] * len(nums)
    st = []
    for lo in reversed(range(len(nums))):
        while len(st) > 0 and nums[lo] > nums[st[-1]]:  # gt: >=
            st.pop()
        if len(st) > 0:
            ans[lo] = nums[st[-1]]  # st可存数字
        st.append(lo)
    return ans


def next_le(nums: List[int]) -> List[int]:
    ans = [-1] * len(nums)
    st = []
    for lo in reversed(range(len(nums))):
        while len(st) > 0 and nums[lo] < nums[st[-1]]:  # lt: <=
            st.pop()
        if len(st) > 0:
            ans[lo] = nums[st[-1]]  # st可存数字
        st.append(lo)
    return ans


def prev_ge(nums: List[int]) -> List[int]:
    ans = [-1] * len(nums)
    st = []
    for hi in range(len(nums)):
        while len(st) > 0 and nums[hi] > nums[st[-1]]:  # gt: >=
            st.pop()
        if len(st) > 0:
            ans[hi] = nums[st[-1]]  # st可存数字
        st.append(hi)
    return ans


if __name__ == '__main__':
    nums = [3, 4, 2, 2, 5, 4]
    print(next_ge(nums))
    print(next_le(nums))
    print(prev_ge(nums))
    """
    [4, 5, 2, 5, -1, -1]
    [2, 2, 2, -1, 4, -1]
    [-1, -1, 4, 2, -1, 5]
    """


# next: ge_min -> le_max: arg: 递增序 -> 递减序
# ge_min: next -> prev:
#   arg: 递增序 -> 递减序
#   next_ge -> prev_le. (索引)


# 下一个最小的>=nums[i]的nums[j]
def next_ge_min(nums: List[int]) -> List[int]:
    arg = sorted(range(len(nums)), key=lambda i: nums[i])
    ans = [-1] * len(arg)
    st = []
    for lo in reversed(range(len(arg))):
        x = arg[lo]
        while len(st) > 0 and x >= arg[st[-1]]:  # 队列内无相等元素.
            st.pop()
        if len(st) > 0:
            ans[x] = nums[arg[st[-1]]]  # ans[hi] = nums[st[-1]]  # st可存数字
        st.append(lo)
    return ans


def next_le_max(nums: List[int]) -> List[int]:
    arg = sorted(range(len(nums)), key=lambda i: -nums[i])
    ans = [-1] * len(arg)
    st = []
    for lo in reversed(range(len(arg))):
        x = arg[lo]
        while len(st) > 0 and x >= arg[st[-1]]:  # 队列内无相等元素.
            st.pop()
        if len(st) > 0:
            ans[x] = nums[arg[st[-1]]]  # ans[hi] = nums[st[-1]]  # st可存数字
        st.append(lo)
    return ans


def prev_ge_min(nums: List[int]) -> List[int]:
    arg = sorted(range(len(nums)), key=lambda i: -nums[i])
    ans = [-1] * len(arg)
    st = []
    for lo in range(len(arg)):
        x = arg[lo]
        while len(st) > 0 and x <= arg[st[-1]]:  # 队列内无相等元素.
            st.pop()
        if len(st) > 0:
            ans[x] = nums[arg[st[-1]]]  # ans[hi] = nums[st[-1]]  # st可存数字
        st.append(lo)
    return ans


if __name__ == '__main__':
    nums = [3, 4, 2, 2, 5, 4]

    print(next_ge_min(nums))
    print(next_le_max(nums))
    print(prev_ge_min(nums))
    """
    [4, 4, 2, 4, -1, -1]
    [2, 4, 2, -1, 4, -1]
    [-1, -1, 3, 2, -1, 4]
    """

# 单调队列
from collections import deque


# next -> prev: reverse -> no reverse, lo -> hi
# max -> min: >= <=

# 含自己: q.append()在ans前
def next_max_k(nums: List[int], k: int) -> List[int]:
    ans = [-1] * len(nums)
    q = deque()  # 递减队列. 存索引. 可存数
    #
    for lo in reversed(range(len(nums))):
        while len(q) > 0 and nums[lo] >= nums[q[-1]]:
            q.pop()
        q.append(lo)  # 含hi.
        if len(q) > 0 and q[0] + 1 - lo > k:
            q.popleft()
        if len(q) > 0:  #
            ans[lo] = nums[q[0]]
        #
    return ans


def prev_max_k(nums: List[int], k: int) -> List[int]:
    ans = [-1] * len(nums)
    q = deque()  # 递减队列. 存索引. 可存数
    #
    for hi in range(len(nums)):
        while len(q) > 0 and nums[hi] >= nums[q[-1]]:
            q.pop()
        q.append(hi)  # 含hi.
        if len(q) > 0 and hi + 1 - q[0] > k:
            q.popleft()
        if len(q) > 0:  #
            ans[hi] = nums[q[0]]
        #
    return ans


def next_min_k(nums: List[int], k: int) -> List[int]:
    ans = [-1] * len(nums)
    q = deque()  # 递减队列. 存索引. 可存数
    #
    for lo in reversed(range(len(nums))):
        while len(q) > 0 and nums[lo] <= nums[q[-1]]:
            q.pop()
        q.append(lo)  # 含hi.
        if len(q) > 0 and q[0] + 1 - lo > k:
            q.popleft()
        if len(q) > 0:  #
            ans[lo] = nums[q[0]]
        #
    return ans


if __name__ == '__main__':
    nums = [3, 4, 2, 2, 5, 4]
    print(prev_max_k(nums, 2))
    print(next_max_k(nums, 2))
    print(next_min_k(nums, 2))
    """
    [3, 4, 4, 2, 5, 5]
    [4, 4, 2, 5, 5, 4]
    [3, 2, 2, 2, 4, 4]
    """
