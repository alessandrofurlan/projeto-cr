import networkx as nx
import pandas as pd
df = pd.read_csv('edges_completo.csv')
lista_edges = ["{{source}} {{target}} {'weight': {{weight}}}".replace("{{source}}", str(v[0])).replace("{{target}}", str(v[1])).replace("{{weight}}", str(v[6])) for v in df.values.tolist()]

G = nx.parse_edgelist(lista_edges, nodetype=int)
list(G.edges(data=True))

nodes = pd.read_csv('nodes_completo.csv')
nodes = nodes[['Id','Label']]

depara_temp = nodes.to_dict()
string_to_index = {y:x for x,y in depara_temp["Label"].items()}
index_to_string = {x:y for x,y in depara_temp["Label"].items()}