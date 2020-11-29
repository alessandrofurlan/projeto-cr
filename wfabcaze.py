import networkx as nx

from processa_grafo import G, index_to_string, string_to_index

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
