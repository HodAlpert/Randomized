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
    # Loading weighted graph with integer nodes
    G = nx.read_weighted_edgelist('graphs/les_miserables.edgelist', nodetype=int)
    # Extract max connected component if G isn't connected
    if not nx.is_connected(G):
        G = G.subgraph(max(nx.connected_components(G), key=len)).copy()
    # Some graphs node labels start at 1, reducing to 0
    if 0 not in G.nodes:
        G = nx.relabel_nodes(G, lambda x: x - 1)

    # Verifying all self loop edges weights are 0
    for u in nx.nodes_with_selfloops(G):
        G[u][u]['weight'] = 0

    # draw_graph.draw(G)  # how to draw the graph with it's weights
    t = ADO(G, k)
    t.pre_processing()

    # Computing average stretch out of 100 iterations
    total_average = 0.0
    max_average = 0.0
    min_average = float('inf')
    iterations = 10

    for _ in range(iterations):
        for node in G.nodes:
            path_lengths, paths = nx.single_source_dijkstra(G, node)
            path_lengths.pop(node)
            algorithm_distances = {v: t.compute_distance(1, v) for v in set(G) - {node}}
            # print("Dijkstra length: ", path_lengths)
            # print("Algorithm length: ", algorithm_distances)

            node_average = 0.0
            for i in set(G) - {node}:
                node_average += float(abs(path_lengths[i] - algorithm_distances[i]))
            node_average /= len(G) - 1
            # print("Node %d average stretch: %f" % (node, node_average))
            min_average = min(min_average, node_average)
            max_average = max(max_average, node_average)
            total_average += node_average
    total_average /= len(G) * iterations
    print(f'Total average stretch: {total_average}',
          f'Max stretch value: {max_average}',
          f'Min stretch value: {min_average}', sep='\n')
