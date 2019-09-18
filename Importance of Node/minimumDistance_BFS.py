import numpy as np


global A_matrix, D_matrix                                   # 定义全局变量
A_matrix = np.zeros((8, 8), dtype=int)                      # 创建一个8x8的全零矩阵，数据类型为int型
D_matrix = np.zeros((8, 8), dtype=int)                      # 创建一个8x8的全零矩阵，数据类型为int型


# 从文件@filename中读取网络的adjacentMatrix，通过networkx的add_edges方法向对象G中添加边
def readNetwork(filename):
    fin = open(filename, 'r')                               # 读文件
    matrix_row = 0                                          # 定义矩阵的行，从第0行开始
    for line in fin.readlines():                            # 一次性读取所有行，并存储为字符串列表
        list = line.strip('\n').split(' ')                  # 处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，
        A_matrix[matrix_row] = list[0:8]                    # list[0:8]表示列表的0~7列数据放到矩阵中的matrix_row行
        matrix_row += 1
    # print(A_matrix)


# 获取到各个结点的最短线路
def get_minimumDistance(A_matrix, index):
    n = len(A_matrix)                                       # n为节点数
    minimumDistance = [0 for i in range(n)]                            # 每个节点第几步可以到达
    q = [index]                                             # 当前搜索的节点
    while len(q) > 0:
        f = q.pop()                                         # f就是from的结点
        s = minimumDistance[f] + 1                                     # 路径长度
        for i in range(0, n):                               # 0是起点，不遍历
            if A_matrix[f][i] == 1:                         # 从结点f到结点i连通
                # i尚未可达或发现更快的路径（权值不同才有可能）
                if (minimumDistance[i] == 0) or (minimumDistance[i] > s):
                    minimumDistance[i] = s                  # 更新最短距离
                    q.insert(0, i)                          # 将前驱节点插入队列首位

        minimumDistance[index] = 0                                         # 自己到达自己置0
    return minimumDistance


if __name__ == '__main__':
    readNetwork("sf100.data")                               # 读取数据
    for i in range(0, len(D_matrix)):                       # 计算任意两点最短距离
        D_matrix[i] = get_minimumDistance(A_matrix, i)

    print(D_matrix)
