import networkx as nx
from matplotlib import pyplot as plt

from algorithm import ApproximateDistanceOracles
from common import timeit, average_difference, avg


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
    total_average = 0.0
    max_average = 0.0
    min_average = float('inf')
    average_query_time = 0.0

    for i in range(iterations):
        # Iterating each node and its shortest paths distances
        for source_node, dijkstra_distances in nx.all_pairs_dijkstra_path_length(G):
            # Querying & timing our algorithm
            times = {}
            algo_distances = [timeit(algo.compute_distance)(source_node, target_node,
                                                            log_name=f'{source_node, target_node}',
                                                            log_time=times)
                              for target_node in G]
            # Comparing result
            node_stretch = average_difference(dijkstra_distances.values(), algo_distances)

            min_average = min(min_average, node_stretch)
            max_average = max(max_average, node_stretch)
            total_average += node_stretch
            average_query_time += avg(times.values())

    total_average /= len(G) * iterations
    average_query_time /= len(G) * iterations
    print(f'Total average stretch: {total_average}',
          f'Average query time: {average_query_time}',
          f'Max stretch value: {max_average}',
          f'Min stretch value: {min_average}', sep='\n')


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
    algo = ApproximateDistanceOracles(G)
    print('Pre-processing..')
    algo.pre_processing()

    print('Running algorithm')
    run(G, iterations=50)
