import networkx as nx

G = nx.Graph()


# 从文件@filename中读取网络的adjacentMatrix，通过networkx的add_edges方法向对象G中添加边
def readNetwork(filename):
    fin = open(filename, 'r')                               # 读文件
    # for line in fin:
    # 	for node in line:
    # 		print(node, end="")

    # lines = fin.readlines()
    # print(len(lines))

    rowCount = 1;                                           # 行数
    colCount = 1;                                           # 列数
    for line in fin.readlines():                            # 一次性读取所有行，并存储为字符串列表
        line = line.split(" ")                              # 每一行以空格分割
        for node in line:                                   # 每一行的每一列，即节点
            if node == '1':
                G.add_edge(rowCount, colCount)              # 节点间连一条边
            colCount = colCount + 1                         # 列数加一，即下一个节点
        colCount = 1                                        # 一行结束后，返回列指针返回
        rowCount += 1

    print(G.edges())                                        # 输出一：边集


# 计算网络中的节点的介数中心性，并进行排序输出
def BetweenessCentrality():
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


# 程序入口
readNetwork("sf100.data")                                   # 从数据文件中读取邻接矩阵
BetweenessCentrality()                                      # 求解介数中心数
