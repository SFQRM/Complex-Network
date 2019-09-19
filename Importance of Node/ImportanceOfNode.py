import networkx as nx
from numpy import *
import math


global A_matrix                                         # 定义全局变量
A_matrix = zeros((8, 8), dtype=int)                     # 创建一个8x8的全零矩阵，数据类型为int型


# 从文件@filename中读取网络的adjacentMatrix，通过networkx的add_edges方法向对象G中添加边
def readNetwork(filename):
    fin = open(filename, 'r')                               # 读文件
    matrix_row = 0                                          # 定义矩阵的行，从第0行开始
    for line in fin.readlines():                            # 一次性读取所有行，并存储为字符串列表
        list = line.strip('\n').split(' ')                  # 处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，
        A_matrix[matrix_row] = list[0:8]                    # list[0:8]表示列表的0~7列数据放到矩阵中的matrix_row行
        matrix_row += 1

    '''
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
    '''


# 计算网络中的节点的介数中心性，并进行排序输出
def betweenessCentrality():
    score = nx.betweenness_centrality(G)                    # 使用networkx封装好的方法求介数中性数
    score = sorted(score.items(), key=lambda item: item[1], reverse=True)       # 对介数中心数排序
    # print("betweenness_centrality: ", score)                                    # 输出二：排序后的介数中心数
    output = []
    for node in score:
        output.append(node[0])

    # print(output)                                           # 输出三：介数中心数的节点编号
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
        denominator0 = math.pow(A_matrix[i][k], 2)
    denominator0 += 1
    for k in range(0, A_matrix.shape[0]):
        denominator1 = math.pow(A_matrix[j][k], 2)
    denominator1 += 1
    denominator = math.pow(denominator0*denominator1, theta/2)
    result = numerator/denominator
    return result


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


# 获取平均支持率
def get_supportRate(f_matrix):
    sum_supportRate = 0
    supportRate = [0 for i in range(len(A_matrix))]

    for i in range(0, len(f_matrix)):
        for j in range(i+1, len(f_matrix)):
            sum_supportRate += f_matrix[i][j]

    num = (1+len(f_matrix)-1)*(len(f_matrix)-1)/2
    average_supportRate = sum_supportRate/num
    for i in range(len(f_matrix)):
        count = 0
        for j in range(len(f_matrix)):
            if(f_matrix[i][j]>average_supportRate):
                count += 1
        supportRate[i] = count/len(supportRate)

    return supportRate


# 程序入口
if __name__ == '__main__':

    G = nx.Graph()                                          # 定义图
    theta = 0.6                                             # 定义θ
    H_matrix = zeros((8, 8), dtype=float)                   # 创建一个8x8的全零矩阵，数据类型为float型
    f_matrix = zeros((8, 8), dtype=float)                   # 创建一个8x8的全零矩阵，数据类型为float型
    d_matrix = zeros((8, 8), dtype=int)                     # 创建一个8x8的全零矩阵，数据类型为int型
    P = [0 for i in range(len(A_matrix))]
    C = [0 for i in range(len(A_matrix))]

    readNetwork("sf100.data")                               # 从数据文件中读取邻接矩阵
    # print(A_matrix)
    betweenessCentrality()                                  # 求解介数中心数
    for i in range(0, len(d_matrix)):                       # 计算任意两点最短距离
        d_matrix[i] = get_minimumDistance(A_matrix, i)
    # print(d_matrix)
    for i in range(0, len(A_matrix)):
        for j in range(0, len(A_matrix)):
            H_matrix[i][j] = isomorphism(i,j, 0.6)          # 计算同构体
            if i != j:                                      # 根据f(i,j)的计算公式，分母d不为0
                f_matrix[i][j] = H_matrix[i][j]/math.pow(d_matrix[i][j], 2)
    # print('H(i,j)\n', H_matrix)
    # print('\n')
    # print('f(i,j)\n', f_matrix)
    P = get_supportRate(f_matrix)         # 获取支持率
    # print(P)
    for i in range(0,len(C)):
        C[i] = math.pow(e, P[i])

    # print(C)
