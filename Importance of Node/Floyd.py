import numpy as np
from pylab import *

# 从文件@filename中读取网络的adjacentMatrix，通过networkx的add_edges方法向对象G中添加边
def readNetwork(filename):
    fin = open(filename, 'r')                               # 读文件
    global A_matrix                                         # 定义全局变量
    A_matrix = np.zeros((8, 8), dtype=int)                  # 创建一个8x8的全零矩阵，数据类型为int型
    matrix_row = 0                                          # 定义矩阵的行，从第0行开始
    for line in fin.readlines():                            # 一次性读取所有行，并存储为字符串列表
        list = line.strip('\n').split(' ')                  # 处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，
        A_matrix[matrix_row] = list[0:8]                    # list[0:8]表示列表的0~7列数据放到矩阵中的matrix_row行
        matrix_row += 1
    # print(A_matrix)


def floyd():
    # print(A_matrix)
    #path_matrix = np.zeros((8, 8), dtype=int)               # 创建一个8x8的全零矩阵，数据类型为int型
    p = list(range(8))
    P = []
    for i in range(0, A_matrix.shape[0]):
        P.append(p)
    P = array(P)

    for i in range(0, A_matrix.shape[0]):
        for j in range(0, A_matrix.shape[0]):
            for k in range(0, A_matrix.shape[1]):
                if A_matrix[i][j] > A_matrix[i][k] + A_matrix[j][k]:
                    P[i,j] = P[j,k]

    print(P)


if __name__ == "__main__":
    readNetwork("sf100.data")
    floyd()

'''

import numpy as np

N = 8
M = 100
edge = np.mat([[0,0,1,0,0,0,0,0], [0,0,1,0,0,0,0,0], [1,1,0,1,0,0,0,0], [0,0,1,0,1,0,0,0],
               [0,0,0,1,0,1,1,0], [0,0,0,0,1,0,1,1], [0,0,0,0,1,1,0,0], [0,0,0,0,0,1,0,0]])
A = edge[:]
path = np.zeros((N, N))


def Floyd():
    for i in range(N):
        for j in range(N):
            if (edge[i, j] != M and edge[i, j] != 0):
                path[i][j] = i

    print('init:')
    print(A, '\n', path)

    for a in range(N):
        for b in range(N):
            for c in range(N):
                if (A[b, a] + A[a, c] < A[b, c]):
                    A[b, c] = A[b, a] + A[a, c]
                    path[b][c] = path[a][c]

    print('result:')
    print(A, '\n', path)


if __name__ == "__main__":
    Floyd()

'''
