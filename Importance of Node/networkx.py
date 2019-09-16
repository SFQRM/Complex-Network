import networkx as nx
import matplotlib.pyplot as plt

# g = nx.Graph()
# g.clear()                 # 清空操作

G = nx.Graph()              # 创建一个空图

# 节点的操作-start #
G.add_node(1)               # 增加一个节点
G.add_nodes_from([2, 3])    # 增加一个节点列表
H = nx.path_graph(10)
G.add_nodes_from(H)         # 将H作为节点G的节点
# 节点的操作-end #

# 边的操作-start #
G.add_edge(1, 2)            # 方式一：增加边，以任意的方式
e = (2, 3)                  # 方式二：增加边，以打包的方式
G.add_edge(*e)
G.add_edges_from([(3,4), (5,6)])        # 方式三：增加边列表
# 边的操作-end #


# example-start #
G.add_edges_from([(1,2), (1, 3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam")
G.add_nodes_from("spam")
G.add_edge(3, 'm')
# example-end #

# 统计边点信息-start #
print(G.number_of_nodes())
print(G.number_of_edges())
# 统计边点信息-end #

# 绘图-start #
nx.draw(G)
plt.show()
# 绘图-end #
