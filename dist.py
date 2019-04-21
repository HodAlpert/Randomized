import networkx as nx

P = [[]]
Lambda = [[]]
B = []
k = 3
G = nx.complete_graph(100, nx.Graph())


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
    compute_distance(1, 1)
