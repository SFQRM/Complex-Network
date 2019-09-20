import networkx as nx
from numpy import *
import math


global A_matrix                                             # 定义全局变量
A_matrix = zeros((8, 8), dtype=int)                         # 创建一个8x8的全零矩阵，数据类型为int型


# 从文件@filename中读取网络的adjacentMatrix，通过networkx的add_edges方法向对象G中添加边
def readNetwork(filename):
    fin = open(filename, 'r')                               # 读文件
    matrix_row = 0                                          # 定义矩阵的行，从第0行开始
    for line in fin.readlines():                            # 一次性读取所有行，并存储为字符串列表
        list = line.strip('\n').split(' ')                  # 处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，
        A_matrix[matrix_row] = list[0:8]                    # list[0:8]表示列表的0~7列数据放到矩阵中的matrix_row行
        matrix_row += 1


# 采用BFS算法，获取各个结点的最短线路
def get_minimumDistance(A_matrix, index):
    n = len(A_matrix)                                       # n为节点数
    minimumDistance = [0 for i in range(n)]                 # 每个节点第几步可以到达
    q = [index]                                             # 当前搜索的节点
    while len(q) > 0:
        f = q.pop()                                         # f就是from的结点
        s = minimumDistance[f] + 1                          # 路径长度
        for i in range(0, n):                               # 0是起点，不遍历
            if A_matrix[f][i] == 1:                         # 从结点f到结点i连通
                # i尚未可达或发现更快的路径（权值不同才有可能）
                if (minimumDistance[i] == 0) or (minimumDistance[i] > s):
                    minimumDistance[i] = s                  # 更新最短距离
                    q.insert(0, i)                          # 将前驱节点插入队列首位
        minimumDistance[index] = 0                          # 自己到达自己置0
    return minimumDistance


# 计算同构体
def isomorphism(i, j, theta):
    numerator = denominator0 = denominator1 = 0              # 初始化
    for k in range(0, A_matrix.shape[0]):
        numerator += A_matrix[i][k] * A_matrix[j][k]         # 计算分子
    numerator += 1
    for k in range(0, A_matrix.shape[0]):
        denominator0 += math.pow(A_matrix[i][k], 2)          # 计算分母0
    denominator0 += 1
    for k in range(0, A_matrix.shape[0]):
        denominator1 += math.pow(A_matrix[j][k], 2)          # 计算分母1
    denominator1 += 1
    denominator = math.pow(denominator0*denominator1, theta/2)
    result = numerator/denominator                          # 同构体结果
    return result


# 获取支持率
def get_supportRate(f_matrix):
    sum_attraction = 0                                      # 平均吸引力
    supportRate = [0 for i in range(len(A_matrix))]         # 支持率
    for i in range(0, len(f_matrix)):
        for j in range(i+1, len(f_matrix)):
            sum_attraction += f_matrix[i][j]                # 吸引力总和
    num = (1+len(f_matrix)-1)*(len(f_matrix)-1)/2           #
    average_attraction = sum_attraction/num                 # 平均吸引力
    for i in range(len(f_matrix)):
        count = 0                                           # 支持者数量
        for j in range(len(f_matrix)):
            if(f_matrix[i][j]>average_attraction):          # 若两节点之间的吸引力超过平均吸引力
                count += 1                                  # 则判定为支持者
        supportRate[i] = count/len(supportRate)             # 计算支持率
    return supportRate


# 程序入口
if __name__ == '__main__':

    G = nx.Graph()                                          # 定义图
    theta = 0.6                                             # 定义θ
    H_matrix = zeros((8, 8), dtype=float)                   # 定义同构体矩阵
    f_matrix = zeros((8, 8), dtype=float)                   # 定义吸引力矩阵
    d_matrix = zeros((8, 8), dtype=int)                     # 定义两点间最短距离矩阵
    P = [0 for i in range(len(A_matrix))]                   # 定义支持率list
    C = [0 for i in range(len(A_matrix))]                   # 定义置信度list
    I = [0 for i in range(len(A_matrix))]                   # 定义节点重要性list
    sum = [0 for i in range(len(A_matrix))]

    readNetwork("sf100.data")                               # 从数据文件中读取邻接矩阵
    # print(A_matrix)

    for i in range(0, len(d_matrix)):                       # 计算任意两点最短距离
        d_matrix[i] = get_minimumDistance(A_matrix, i)
    # print(d_matrix)

    for i in range(0, len(A_matrix)):
        for j in range(0, len(A_matrix)):
            H_matrix[i][j] = isomorphism(i,j, theta)        # 计算同构体H(i, j)
    # print('H(i,j)\n', H_matrix)

    for i in range(0, len(H_matrix)):
        for j in range(0, len(H_matrix)):
            if i != j:                                      # 根据吸引力f(i,j)的计算公式，分母d不能为0
                f_matrix[i][j] = H_matrix[i][j]/math.pow(d_matrix[i][j], 2)
    # print('f(i,j)\n', f_matrix)

    P = get_supportRate(f_matrix)                           # 获取支持率
    # print(P)

    for i in range(0, len(C)):
        C[i] = math.pow(e, P[i])                            # 计算置信值
    # print(C)

    for i in range(0, len(I)):
        for j in range(0, len(A_matrix)):
            sum[i] += f_matrix[i][j]
        I[i] = C[i]*sum[i]                                  # 计算节点重要性
    # print(sum)
    print(I)
