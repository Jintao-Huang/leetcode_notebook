# leetcode_notebook
leetcode 刷题笔记(基于python3)



## 易错(重点)

1. 在`q.append()` or `ans.append()`时, 注意copy.
2. 左右(对撞)双指针对于\[lo, hi\]还是\[lo, hi)的选择.
    - \[lo, hi\]: `hi`作为索引时.
    - \[lo, hi): `len()`的概念出现较多时.


## 易错(细节)

1. 请写成`mid = lo + (hi - lo) // 2`. 避免`lo + hi`整形溢出 (C++中)
2. 子序列(不连续), 子串(连续)的区别.

