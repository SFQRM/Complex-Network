import numpy as np
import networkx as nx


global N                                                    # 定义全局变量
N = 8                                                       # N代表矩阵的维度


# 从文件@filename中读取网络的adjacentMatrix，通过networkx的add_edges方法向对象G中添加边
def readNetwork(filename):
    fin = open(filename, 'r')                               # 读文件
    global A_matrix                                         # 定义全局变量
    A_matrix = np.zeros((N, N), dtype=int)                  # 创建一个8x8的全零矩阵，数据类型为int型
    matrix_row = 0                                          # 定义矩阵的行，从第0行开始
    for line in fin.readlines():                            # 一次性读取所有行，并存储为字符串列表
        # list = line.strip('\n').split(' ')                  # 处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，
        list = line.strip('\n').split(' ')
        A_matrix[matrix_row] = list[0: N]                   # list[0:N]表示列表的0~N-1列数据放到矩阵中的matrix_row行
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


if __name__ == '__main__':
    G = nx.Graph()                              # 定义图
    readNetwork("sf100.data")                   # 读取数据文件
    eig_cen = nx.eigenvector_centrality(G)      # 求特征向量中心性
    print("ec:\n", eig_cen)                      # 输出特征向量结果


'''
OUTPUT
ec:
 {1: 0.09144839506821373, 2: 0.09144839506821373, 3: 0.2156073111153089, 4: 0.3254455096745499, 5: 0.5516961368282031, 6: 0.5205239606588591, 7: 0.4547721085708779, 8: 0.22077499396454175}

'''
