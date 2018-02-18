import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
elist = [(1,2),(1,3),(1,5),(2,5),(2,4),(3,4)]

G.add_edges_from(elist)

C = nx.betweenness_centrality(G)
pos= nx.spring_layout(G)

nx.draw(G, pos,nodelist=[1,3,5], node_color='r', edge_color='b',node_size=[i*1000 for i in C.values()])
nx.draw(G, pos,nodelist=[2,4], node_color='g', edge_color='b',node_size=[i*1000 for i in C.values()])

labels = {}
maxium = max(C.values())
for i in C.keys() :
    if C[i] == maxium:
        labels[i] = i
        labels[i]=b'$MAX$'
nx.draw_networkx_labels(G,pos,labels,font_size=16)
plt.show()

K = nx.Graph()
elist2 = [(1,6),(1,4),(2,3),(2,4),(2,5),(2,6),(4,6),(3,4),(5,6)]

K.add_edges_from(elist2)

F = nx.betweenness_centrality(K)
pos2= nx.spring_layout(K)

nx.draw(K, pos2,nodelist = [1,3,5], node_color='r', edge_color='b',node_size=[i*1000 for i in F.values()])
nx.draw(K, pos2,nodelist=[2,4,6], node_color='y', edge_color='b',node_size=[i*1000 for i in F.values()])

labels2 = {}
maxium2 = max(F.values())
for d in F.keys() :
    if F[d] == maxium2:
        labels2[d] = d
        labels2[d]=b'$MAX$'
nx.draw_networkx_labels(K,pos2,labels2,font_size=16)
plt.show()