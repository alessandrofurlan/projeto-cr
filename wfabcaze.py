import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gephi_data_edges.csv')
nodes = pd.read_csv('gephi_data_nodes.csv')
nodes = nodes[['Id','Label']]

G = nx.parse_edgelist(lista_edges, nodetype=int)
plt.subplot(121)
nx.draw(G, node_color='r', edge_color='b')