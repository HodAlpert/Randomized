import matplotlib.pyplot as plt
import networkx as nx


def draw(G):
    pos = nx.spring_layout(G)  # positions for all nodes

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=300)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(data=True),
                           width=6)

    # weights
    nx.draw_networkx_edge_labels(G, pos, edge_labels={k: v["weight"] for k, v in G.edges.iteritems()})
    nx.draw_networkx_labels(G, pos, font_family='sans-serif')

    plt.axis('off')
    plt.show()
