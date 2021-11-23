# leetcode_notebook
leetcode 刷题笔记

## 文件夹介绍

- `src`: 可以在leetcode上通过的代码
- `template`: 模板


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
2. 子序列, 子串的区别