# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 
"""P1 学到什么
1. 常用的数据结构
2. 常用的算法
3. 每个知识点，各个击破
"""

"""P2 算法的时间复杂度
1. 大O表示法
"""

"""OLogN
2 ** t = N
t = log2(N)
"""


def OLogN(num):
    i = 1
    while i < num:
        i = i * 2
    return i


def OMAddN(num1, num2):
    """O(M+N)"""
    for i in range(num1):
        pass
    for j in range(num2):
        pass


"""P3空间复杂度
1. 大O表示法
(注意递归)
"""

"""P4 数组
1. 连续 相同类型
2. 适合读、不适合写

区分:
1. 元素、索引
2. 数组访问、数组搜索

四种操作与时间复杂度
1. 访问 access O(1)
2. 搜索 search O(N)
3. 插入 insert O(N)
4. 删除 delete O(N)

常用操作:
1. 创建 数组长度
2. 访问 搜索 添加 修改 删除
3. 遍历 排序

题：483 283 27
"""

"""P10 链表
区别：
1. 可以不连续
2. 写快，读慢

分为:
1. 单端链表（力扣够用了）
2. 双端链表(有指向前后的指针)

四种操作与时间复杂度
1. 访问 access O(N)
2. 搜索 search O(N)
3. 插入 insert O(1)
4. 删除 delete O(1)

常用操作:
1. 创建 数组长度
2. 访问 搜索 添加 修改 删除
3. 遍历

题：203 206
"""

"""P15 队列
队列的特点
1. 可以由deque实现  (双端队列-两个口子都可以进/出)
2. 先进先出

四种操作与时间复杂度
1. 访问(顶) access O(1) / O(N)内部
2. 搜索 search O(N)
3. 插入 insert O(1)
4. 删除 delete O(1)

常用操作:
1. 创建 数组长度 是否为空
2. 访问 添加 删除
3. 遍历（边删除边遍历）

题：933 239(困难)
"""

"""P19 栈
1. 先进先出
2. 可由list实现

四种操作与时间复杂度
1. 访问(顶) access O(1)
2. 搜索 search O(N)
3. 插入 insert O(1)
4. 删除 delete O(1)

常用操作:
1. 创建 数组长度 是否为空
2. 访问 添加 删除
3. 遍历（边删除边遍历）

题：20 496(栈+hashMap)
"""
