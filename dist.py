import random

import networkx as nx

from ADO import ADO
import draw_graph

P = [[]]
Lambda = [[]]
B = []
k = 3
G = nx.complete_graph(5, nx.Graph())


def compute_distance(u, v):
    w = u
    i = 0
    while w not in B[v]:
        i += 1
        temp = u
        u = temp
        v = u
        w = P[i][u]
    return Lambda[w][u] + Lambda[w][v]


if __name__ == '__main__':
    G = nx.complete_graph(6, nx.Graph())
    for v in G.nodes:
        for u in G.nodes:
            if (u, v) in G.edges:
                G[u][v]['weight'] = 0 if u == v else int(random.random() * 40)

    draw_graph.draw(G)
    ADO().pre_processing(G)
