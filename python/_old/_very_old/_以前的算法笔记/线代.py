# Author: Jintao Huang
# Email: hjt_study@qq.com
# Date: 

# 线代
## 矩阵


### 增广矩阵 -> 行阶梯形和行最简形


import numpy as np
from fractions import Fraction

mat = [[1, 1, 1, 1, 1], [2, 0, -3, 2, 1], [1, 3, 6, 1, 2], [4, 2, 6, 4, 3]]


# mat = [[2, 3], [1, -1], [-1, 2]]
# mat = [[1, 2, -3, 2], [3, 2, 1, 1], [4, 4, -2, 3]]
# mat = [[3, 2, 1, 1], [1, 2, -3, 2], [4, 4, -2, 3]]


def transform(mat, detail=False):
    """transform(mat: Union[Iterable, ndarray]) -> tuple[ndarray, ndarray]

    将增广矩阵转换成行阶梯形和行最简形。

    :param detail: 是否输出中间过程
    :return：返回一个二元组，第一个元素是矩阵的行阶梯形，第二个元素是矩阵的行最简形"""

    str_format = "%s:\n%s\n---------------------------------------------"

    def elimination(mat):
        mat = mat.copy()
        i = 0
        j = 0
        while i < mat.shape[0] and j < mat.shape[1]:
            # for i in range(mat.shape[0]):  # 0, 1, 2
            # 1. 每排重要系数化1
            if mat[i, j] < 1e-10:
                if j + 1 >= mat.shape[1] and i + 1 < mat.shape[0]:
                    # j要超出，i还未超出的情况：将下方矩阵上移
                    j = i
                    mat[i:-1, :] = mat[i + 1:, :]
                else:
                    # 当前位置 为 0，有效系数在右边
                    j += 1
                continue
            # 系数化1
            mat[i, :] /= mat[i, j]

            # 2. 各排多余系数化0
            for i2 in range(i + 1, mat.shape[0]):
                mat[i2, :] += mat[i, :] * -(mat[i2, j] / mat[i, j])
            i += 1
            j += 1

        return mat

    def substitute(mat):
        mat = mat.copy()
        # 1. 获取j列 从下往上数的第一个1的 i
        i = mat.shape[0] - 1
        while i > -1:
            # 查找  该排最前面的1的索引
            index = np.where(mat[i] == 1)[0]
            # 该排 无1(即全0)
            if len(list(index)) == 0:
                i -= 1
                continue

            # 该排 有1
            j = index[0]
            for i2 in range(0, i):
                mat[i2, :] += mat[i, :] * -(mat[i2, j] / mat[i, j])
            i -= 1
        return mat

    # 1. 预处理
    # 1.1 mat -> ndarray
    mat = np.array(mat, dtype=np.float)
    # 1.2 设置输出
    np.set_printoptions(formatter={'all': lambda x: "%8s" % Fraction(x).limit_denominator()})

    # 2. 操作过程
    if detail:
        print(str_format % ("1. 原矩阵", mat))
    # 2.1 消元过程
    mat1 = elimination(mat)
    if detail:
        print(str_format % ("2. 行阶梯形矩阵", mat1))
    # 2.2 代入过程
    mat2 = substitute(mat1)
    if detail:
        print(str_format % ("3. 行最简形矩阵", mat2))
    return mat1, mat2


mat = np.array(mat, dtype=np.float)
transform(mat, True)

### 矩阵乘法

"""不使用numpy"""


def matmul(a, b):
    """matmul(a: List[List], b: List[List]) -> List[List]

    返回 a矩阵与b矩阵的矩阵乘积"""
    # 1. 判断 a, b 是矩阵
    # if not (is_mat(a) and is_mat(b)):
    # exit(0)
    a_shape = (len(a), len(a[0]))
    b_shape = (len(b), len(b[0]))
    # 2. 判断 a, b 矩阵相乘的 条件
    if a_shape[1] != b_shape[0]:
        exit(0)
    # 3. 矩阵相乘
    dest_list = []
    for i in range(a_shape[0]):
        child_list = []
        for j in range(b_shape[1]):
            sum_ = 0
            for k in range(a_shape[1]):
                sum_ += a[i][k] * b[k][j]
            child_list.append(sum_)
        dest_list.append(child_list)
    return dest_list


a = [[1, 2, 3], [4, 5, 6]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matmul(a, b))

# import numpy as np
#
# a = np.array([[1, 2, 3], [4, 5, 6]])  # shape = (2, 3)
# b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # shape = (3, 3)
# print(a, b, sep="\n")
# """[[30, 36, 42], [66, 81, 96]]"""
# print(np.matmul(a, b))  # shape = (2, 3)


"""使用numpy"""
import numpy as np


def matmul(mat1, mat2):
    """matmul(mat1: Union[Iterable, ndarray], mat2: Union[Iterable, ndarray]) -> ndarray

    返回 mat1矩阵与mat2矩阵的矩阵乘积"""
    # 1. 预处理
    mat1 = np.array(mat1)
    mat2 = np.array(mat2)

    # 2. 判断 a, b 矩阵相乘的 条件
    if mat1.shape[1] != mat2.shape[0]:
        exit(0)
    # 3. 矩阵相乘
    dest_mat = np.zeros(shape=(mat1.shape[0], mat2.shape[1]))
    for i in range(dest_mat.shape[0]):
        for j in range(dest_mat.shape[1]):
            dest_mat[i, j] = np.sum(mat1[i, :] * mat2[:, j])

    return dest_mat


a = [[1, 2, 3], [4, 5, 6]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matmul(a, b))  # [[30. 36. 42.]\n [66. 81. 96.]]
print(np.matmul(a, b))  # [[30 36 42]\n [66 81 96]]

### 矩阵的幂

"""使用自己的matmul"""


# from utils import *


def power(mat, n):
    """power(mat: Union[Iterable, ndarray], n: int) -> ndarray

    返回 mat ^ n"""
    # 递归基
    if n == 1:
        return mat
    # 分治法
    mid = n // 2
    return matmul(power(mat, mid), power(mat, n - mid))


print(power([[2, 0], [0, 2]], 10))

### 转置矩阵

"""不使用numpy"""


def transpose(mat):
    """transpose(mat: List[List]) -> List[List]

    Returns the transpose of `mat`.
    """
    # 1. 判断mat是矩阵
    # if not is_mat(mat):
    # exit(0)

    # 2. 转置mat
    mat_shape = len(mat), len(mat[0])
    dest_list = []
    for j in range(mat_shape[1]):
        child_list = []
        for i in range(mat_shape[0]):
            child_list.append(mat[i][j])
        dest_list.append(child_list)
    return dest_list


print(transpose([[1, 2], [4, 5]]))  # [[1, 4], [2, 5]]
print(transpose([[1, 2, 3], [4, 5, 6]]))  # [[1, 4], [2, 5], [3, 6]]

"""使用numpy"""


def transpose(mat):
    """transpose(mat: Union[Iterable, ndarray]) -> ndarray

    Returns the transpose of `mat`.
    """
    # 1. 预处理
    mat = np.array(mat)

    # 2. 转置mat
    dest_mat = np.zeros((mat.shape[1], mat.shape[0]))
    for i in range(dest_mat.shape[0]):
        dest_mat[i, :] = mat[:, i]
    return dest_mat


## 行列式

### 行列式求值


"""通过代数余子式求解"""
import numpy as np

mat = [[2, -5, 1, 2], [-3, 7, -1, 4], [5, -9, 2, 7], [4, -6, 1, 2]]  # -9


# mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 0


def det(mat):
    """det(mat: Union[Iterable, ndarray]) -> Union[int, float]

    计算mat的行列式

    算法：通过代数余子式求解"""

    def _det(mat):
        # 递归基
        if mat.shape[0] == 1:
            return mat[0, 0]

        sum_ = 0
        j = 0
        for i in range(mat.shape[0]):
            c = 1 if (i + j) % 2 == 0 else -1
            sum_ += mat[i, j] * c * _det(np.delete(np.delete(mat, i, 0), j, 1))
        return sum_

    # 1. 预处理
    # 1.1 -> ndarray
    mat = np.array(mat, dtype=np.float64)
    # 1.2 判断是方阵
    if mat.shape[0] != mat.shape[1]:
        exit(0)

    # 2. 计算
    return _det(mat)


print(det(mat))  # -9
print(np.linalg.det(mat))

"""使用行列式性质求值"""

import numpy as np

# mat = [[2, -5, 1, 2], [-3, 7, -1, 4], [5, -9, 2, 7], [4, -6, 1, 2]]  # -9
# mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 0
mat = [[103, 100, 204], [199, 200, 395], [301, 300, 600]]


def det2(mat):
    """det(mat: Union[Iterable, ndarray]) -> Union[int, float]

    计算mat的行列式

    算法：通过行列式性质"""

    def transform(mat):
        mat = mat.copy()

        for i in range(mat.shape[0]):
            j = i
            # 1. 判断是否关键对角线元素为0
            if mat[i, j] == 0:
                index = np.where(mat[i] != 0)[0]
                # 一列全是0，则整个行列式为0
                if len(list(index)) == 0:
                    return
                else:
                    # 交换律
                    mat[:, j], mat[:, index[0]] = -mat[:, index[0]], mat[:, i].copy()
            # 2. 其他行非三角区域元素化0
            for i2 in range(i + 1, mat.shape[0]):
                mat[i2, :] += mat[i, :] * -(mat[i2, j] / mat[i, j])
        return mat

    def calculate(mat):
        sum_ = 1
        # 主对角线元素相乘
        for i in range(mat.shape[0]):
            j = i
            sum_ *= mat[i][j]
        return sum_

    # 1. 预处理
    # 1.1 -> ndarray
    mat = np.array(mat, dtype=np.float64)
    # 1.2 判断是方阵
    if mat.shape[0] != mat.shape[1]:
        exit(0)
    # 2. 操作过程
    # 2.1 使用行列式的性质进行变换
    mat1 = transform(mat)
    if mat1 is None:
        return 0
    else:
        # 2.2 计算
        return calculate(mat1)


print(det2(mat))
print(np.linalg.det(mat))
