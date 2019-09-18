import numpy as np
from copy import deepcopy


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


# 获取到各个结点的最短线路
def get_path(A_matrix):
    n = len(A_matrix)                                       # n为节点数
    global step
    step = [0 for i in range(n)]                            # 每个节点第几步可以到达
    step_path = [[] for i in range(n)]                      # 到每个节点的走法
    step_path[0] = [[0]]                                    # 到节点0有1种走法
    q = [0]                                                 # 当前搜索的节点
    # print(q)
    while len(q) > 0:
        f = q.pop()                                         # f就是from的结点
        s = step[f] + 1                                     # 路径长度
        for i in range(1, n):                               # 0是起点，不遍历
            if A_matrix[f][i] == 1:                         # 从结点f到结点i连通
                # i尚未可达或发现更快的路径（权值不同才有可能）
                if (step[i] == 0) or (step[i] > s):
                    step[i] = s
                    q.insert(0, i)
                    step_path[i] = deepcopy(step_path[f])
                    # print(len(step_path[i]))
                    if len(step_path[i]) > 0:
                        for j in range(len(step_path[i])):
                            step_path[i][j].append(i)       # 线路中添加结点i

                elif step[i] == s:  # 发现相同长度的路径
                    dp = deepcopy(step_path[f])
                    if len(dp) > 0:
                        for j in range(len(dp)):
                            dp[j].append(i)  # 线路中添加结点i
                    step_path[i] += dp

    return step_path


if __name__ == '__main__':
    # 初始化图的数据，连通的标记为1
    readNetwork("sf100.data")
    step_path = get_path(A_matrix)

    # 输出结果
    for i in range(len(step_path)):
        size = len(step_path[i])
        print('到结点%s的最短路径%s条：' % (i, size))
        for j in range(size):
            print(step_path[i][j])
            print('步长为：%d' % step[i])
