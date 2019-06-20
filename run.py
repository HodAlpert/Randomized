import networkx as nx
from matplotlib import pyplot as plt

from algorithm import ApproximateDistanceOracles
from common import timeit


def draw(G):
    pos = nx.spring_layout(G)  # positions for all nodes
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=300)
    # edges
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(data=True), width=6)
    # weights
    nx.draw_networkx_edge_labels(G, pos, edge_labels={k: v["weight"] for k, v in G.edges.items()})
    nx.draw_networkx_labels(G, pos, font_family='sans-serif')

    plt.axis('off')
    plt.show()


@timeit
def run(G, iterations=100):
    total_avg = 0.0
    max_avg = 0.0
    min_avg = float('inf')
    times = {}
    for i in range(iterations):
        for node in G.nodes:
            max_avg, min_avg, total_avg = run_node(G, max_avg, min_avg, node, total_avg,
                                                   log_name=f'{i}_{node}', log_time=times)
    total_avg /= len(G) * iterations
    print(f'Total average stretch: {total_avg}',
          f'Total average node stretch: {sum(times.values()) / len(times)}',
          f'Max stretch value: {max_avg}',
          f'Min stretch value: {min_avg}', sep='\n')


@timeit
def run_node(G, max_average, min_average, node, total_average, **kwargs):
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
    return max_average, min_average, total_average


if __name__ == '__main__':
    # Loading weighted graph with integer nodes
    G = nx.read_weighted_edgelist('graphs/les_miserables.edgelist', nodetype=int)
    # Extract max connected component if G isn't connected
    if not nx.is_connected(G):
        print('G is not connected, extracting max connected subgraph..')
        G = G.subgraph(max(nx.connected_components(G), key=len))
        print('Relabeling..')
        G = nx.relabel_nodes(G, dict(zip(G, range(len(G)))))
    # Relabeling nodes if not are not consecutively numbered
    elif not all(n in G.nodes for n in range(len(G))):
        G = nx.relabel_nodes(G, dict(zip(G, range(len(G)))))

    # Verifying all self loop edges weights are 0
    for u in nx.nodes_with_selfloops(G):
        G[u][u]['weight'] = 0

    # draw_graph.draw(G)  # how to draw the graph with it's weights
    t = ApproximateDistanceOracles(G)
    print('Pre-processing..')
    t.pre_processing()

    print('Running algorithm')
    run(G, iterations=5)
