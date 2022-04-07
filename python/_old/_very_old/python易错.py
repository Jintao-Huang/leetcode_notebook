
# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

"""1. list的`*`只复制视图"""
res = [[0] * 3] * 3  # error. 这是视图
print(res)
res[0][0] = 1
print(res)
"""
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[1, 0, 0], [1, 0, 0], [1, 0, 0]]
"""