# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date:

"""P64 回溯法
特点:
1. 类似枚举，一层层向下递归，尝试搜索答案
- 找到答案：返回答案 + 尝试别的可能
- 找不到答案：返回上一层递归 + 尝试别的可能
2. 递归，去掉不满足条件的可能 (剪枝)

题：22 78 77 46 51 52 36 37
"""

"""P67 深度优先搜索 DFS
用到递归的思想：
1. 分治法
2. 回溯法
3. DFS

DFS: 从root结点开始，尽可能深的搜索每一个分支，
  把一个分支的结果搜索完后，再去搜索下一个分支


主要应用：
1. 二叉树搜索
2. 图的搜索

DFS与回溯的区别：
1. 回溯 = DFS + 剪枝
2. DFS 有回溯的思想，例如函数环境的保存与恢复。
  但是没有像回溯算法那样显式的保存与恢复

题：938 78 200
"""

"""P70 广度优先搜索 BFS

主要应用：
1. 二叉树搜索
2. 图搜索

主要思想：一层层递进遍历

注意：
1. isVisited 数组一定要在加入队列/栈时 置为True

题：102 107 200
"""