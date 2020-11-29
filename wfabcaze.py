import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('edges_completo.csv')

lista_edges = ["{{source}} {{target}} {'weight': {{weight}}}".replace("{{source}}", str(v[0])).replace("{{target}}", str(v[1])).replace("{{weight}}", str(v[6])) for v in df.values.tolist()]

G = nx.parse_edgelist(lista_edges, nodetype=int)
list(G.edges(data=True))

nodes = pd.read_csv('nodes_completo.csv')
nodes = nodes[['Id','Label']]

depara_temp = nodes.to_dict()
string_to_index = {y:x for x,y in depara_temp["Label"].items()}
index_to_string = {x:y for x,y in depara_temp["Label"].items()}

def caminho(node1, node2):
    id_inicio = string_to_index[node1]
    id_fim = string_to_index[node2]
    path = nx.shortest_path(G, source=id_inicio, target=id_fim)
    path_string = [index_to_string[index] for index in path]
    return path_string


def calcularDistancia(node1, node2):
    id_inicio = string_to_index[node1]
    id_fim = string_to_index[node2]
    distancia = nx.dijkstra_path_length(G, source=id_inicio, target=id_fim)
    return distancia
