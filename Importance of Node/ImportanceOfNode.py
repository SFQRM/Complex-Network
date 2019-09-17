import networkx as nx
from numpy import *
import math


# 从文件@filename中读取网络的adjacentMatrix，通过networkx的add_edges方法向对象G中添加边
def readNetwork(filename):
    fin = open(filename, 'r')                               # 读文件
    global A_matrix                                         # 定义全局变量
    A_matrix = zeros((8, 8), dtype=int)                     # 创建一个8x8的全零矩阵，数据类型为int型
    matrix_row = 0                                          # 定义矩阵的行，从第0行开始
    for line in fin.readlines():                            # 一次性读取所有行，并存储为字符串列表
        list = line.strip('\n').split(' ')                  # 处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，
        A_matrix[matrix_row] = list[0:8]                    # list[0:8]表示列表的0~7列数据放到矩阵中的matrix_row行
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

    print(G.edges())


# 计算网络中的节点的介数中心性，并进行排序输出
def betweenessCentrality():
    score = nx.betweenness_centrality(G)                    # 使用networkx封装好的方法求介数中性数
    score = sorted(score.items(), key=lambda item: item[1], reverse=True)       # 对介数中心数排序
    print("betweenness_centrality: ", score)                                    # 输出二：排序后的介数中心数
    output = []
    for node in score:
        output.append(node[0])

    print(output)                                           # 输出三：介数中心数的节点编号
    '''
    fout = open("betweennessSorted.data", 'w')
    for target in output:
        fout.write(str(target) + " ")                       # 将输出三的结果写入文件
    '''


# 计算同构体
def isomorphism(i, j, theta):
    for k in range(0, A_matrix.shape[0]):
        numerator = A_matrix[i][k] * A_matrix[j][k]
    numerator += 1
    for k in range(0, A_matrix.shape[0]):
        result0 = pow(A_matrix[i][k], 2)
    result0 += 1
    for k in range(0, A_matrix.shape[0]):
        result1 = pow(A_matrix[j][k], 2)
    result1 += 1
    denominator = pow(result0*result1, theta/2)
    result = numerator/denominator
    return result


# 程序入口
if __name__ == '__main__':
    G = nx.Graph()                                          # 定义图
    readNetwork("sf100.data")                               # 从数据文件中读取邻接矩阵
    # betweenessCentrality()                                  # 求解介数中心数
    i = 0
    j = 0
    theta = 0.6
    H_matrix = zeros((8, 8), dtype=float)                   # 创建一个8x8的全零矩阵，数据类型为int型
    H_matrix[i][j] = isomorphism(i,j, 0.6)
    # print(A_matrix)
