# leetcode_notebook
leetcode 刷题笔记(基于python3)

## 文件夹介绍

- `src`: 可以在leetcode上通过的代码. (frozen)
- `dev`: 开发中的代码. (active)
- `template`: 复用模板.


## 易错(重点)

1. 在`q.append()` or `ans.append()`时, 注意copy.
\[46, 752\]
2. 左右(对撞)双指针对于\[lo, hi\]还是\[lo, hi)的选择.
    - \[lo, hi\]: `hi`作为索引时.
\[167, 快排partition()\]
    - \[lo, hi): `len()`的概念出现较多时.
\[105\, template>binary_search.py]


## 易错(细节)

1. 请写成`mid = lo + (hi - lo) // 2`. 避免`lo + hi`整形溢出 (C++中)
2. 子序列(不连续), 子串(连续)的区别.


## 分类(src中)
1. dfs/递归(除回溯):
\[105, 124\]
2. 回溯:
\[46, 47, 52\]
3. bfs:
\[111, 752\]
4. 双指针(除滑动窗口):
    - 快慢:
\[142\]
    - 左右:
\[167\]
5. 滑动窗口:
6. 动态规划:
7. 二分搜索:
