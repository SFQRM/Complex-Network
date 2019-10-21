# @author: SFQRM
# first edit date: 2019-10-21
# function:
#     利用邻接矩阵使用networkx画出拓扑图。

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


# 从文件@filename中读取网络的adjacentMatrix，通过networkx的add_edges方法向对象G中添加边
def readNetwork(filename, N):
    fin = open(filename, 'r')                               # 读文件
    A_matrix = np.zeros((N, N), dtype=int)                  # 创建一个8x8的全零矩阵，数据类型为int型
    matrix_row = 0                                          # 定义矩阵的行，从第0行开始
    for line in fin.readlines():                            # 一次性读取所有行，并存储为字符串列表
        list = line.strip('\n').split(' ')                  # 处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，
        # list = line.strip('\n').split('\t')
        A_matrix[matrix_row] = list[0:N]                    # list[0:8]表示列表的0~7列数据放到矩阵中的matrix_row行
        matrix_row += 1

    # print(martrix)
    rowCount = 1                                            # 行数初始化
    colCount = 1                                            # 列数初始化
    for line in A_matrix:
        for node in line:
            if node == 1:
                G.add_edge(rowCount, colCount)              # 节点间连一条边
            colCount += 1
        colCount = 1
        rowCount += 1

    # print(G.edges())
    return A_matrix


# 向函数传入图结构后根据matplotlib画出拓扑图
def plotGraph(matrix):
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()


if __name__ == '__main__':
    G = nx.Graph()                                           # G: 定义一个空的图结构
    N = 8                                                    # N: 邻接矩阵的维度
    A_matrix = readNetwork('sf100.data', N)                  # 从外部文件读取邻接矩阵
    plotGraph(A_matrix)                                      # 画出拓扑图
    # print(A_matrix)