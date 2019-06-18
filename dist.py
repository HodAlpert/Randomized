import random

import networkx as nx

from ADO import ADO

P = [[]]
Lambda = [[]]
B = []
k = 3


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
    number_of_nodes = 200
    k = 4
    G = nx.complete_graph(number_of_nodes, nx.Graph())
    for v in G.nodes:
        for u in G.nodes:
            if (u, v) in G.edges:
                G[u][v]['weight'] = 0 if u == v else int(random.random() * 40)

    # draw_graph.draw(G)  # how to draw the graph with it's weights
    t = ADO(G, k)
    t.pre_processing()
    path_lengths, paths = nx.single_source_dijkstra(G, 1)
    path_lengths.pop(1)
    algorithm_distances = {v: t.compute_distance(1, v) for v in set(G) - {1}}
    print("dijkstra length: ", path_lengths)
    print("algorithm length: ", algorithm_distances)
    average = 0.0
    for i in set(G) - {1}:
        average += float(abs(path_lengths[i] - algorithm_distances[i]))
    average /= len(G) - 1
    print("average stretch is ", average)
