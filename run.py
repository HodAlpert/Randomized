import os
from datetime import datetime

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
def run(G, k, iterations=5):
    total_average = 0.0
    max_average = 0.0
    min_average = float('inf')
    average_query_time = 0.0
    average_dijkstra_time = 0.0

    with open(f'results/{k}_{graph_name}', 'w') as output:

        print(f'Running algorithm on {graph_name}, k={k}', file=output)
        # draw_graph.draw(G)  # how to draw the graph with it's weights
        algo = ApproximateDistanceOracles(G, k=k)
        print('Pre-processing..', file=output)
        algo.pre_processing()

        print('Running algorithm', file=output)
        for i in range(iterations):
            # Iterating each node and its shortest paths distances
            start = datetime.now()
            for source_node, dijkstra_distances in nx.all_pairs_dijkstra_path_length(G):
                average_dijkstra_time += (datetime.now() - start).total_seconds()

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

        d = len(G) * iterations
        total_average /= d
        average_query_time /= d
        average_dijkstra_time /= d
        print(f'Total average stretch: {total_average}',
              f'Average query time: {average_query_time}',
              f'Average dijkstra time: {average_dijkstra_time}',
              f'Max stretch value: {max_average}',
              f'Min stretch value: {min_average}', sep='\n',
              file=output)


if __name__ == '__main__':
    # Loading weighted graph with integer nodes
    for graph_name in os.listdir('graphs'):
        print(f'--------- {graph_name} ---------')
        G = nx.read_weighted_edgelist(f'graphs/{graph_name}', nodetype=int)
        # Extract max connected component if G isn't connected
        if not nx.is_connected(G):
            print('G is not connected, extracting max connected subgraph..')
            G = G.subgraph(max(nx.connected_components(G), key=len))
            print('Relabeling..')
            G = nx.relabel_nodes(G, dict(zip(G, range(len(G)))))
        # Relabeling nodes if not are not consecutively numbered
        elif not all(n in G.nodes for n in range(len(G))):
            G = nx.relabel_nodes(G, dict(zip(G, range(len(G)))))

        # Removing self-loop edges
        G.remove_edges_from(list(nx.selfloop_edges(G)))

        print(f'Nodes: {len(G)}, Edges: {len(G.edges)}')

        ks = [3, 10, 50]
        for k in ks:
            run(G, k)
