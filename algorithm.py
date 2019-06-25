import networkx as nx
import numpy as np

from common import modified_dijkstra, timeit

SOURCE = "s"


class ApproximateDistanceOracles(object):
    def __init__(self, G, k=3):
        self.G = G
        self.n = len(G)
        self.k = k
        self.B = None
        self.Lambda = None
        self.P = None

    def compute_distance(self, u, v, **kwargs):
        """
        computes the distances according to the algorithm
        :param u: Integer representing node u
        :param v: Integer representing node v
        :returns: The distance
        """
        w, i = u, 0
        while w not in self.B[v]:
            i += 1
            u, v = v, u
            w = self.P[i][u]
        return self.Lambda[i][u] + self.B[v][w]

    @timeit
    def pre_processing(self):
        """
        Gets an undirected positive weighted graph and computes:
            Lambda: array of arrays (length k * n) while Lambda[i][u] contains the distance A[i] to u.
            P: array of arrays (length k * n) while P[i][u] contains the closest node from A[i] to u.
            B: array of arrays the size of (n * len(B[v]) contains all nodes that belongs to B[v].
        :returns: a tuple (Lambda, P, B):
        """
        A = self.generate_A()
        while not A[self.k - 1]:  # repeat until A[k-1] is not an empty set
            A = self.generate_A()
        # generating a list the size of (k * n) which will contain lambda(A[i], v) for any v in V initialized as -1
        # symbolising infinity
        Lambda, P = self.generate_Lambda_and_P(A)
        B = self.generate_B(A, Lambda)
        self.B = B
        self.Lambda = Lambda
        self.P = P
        return Lambda, P, B

    @timeit
    def generate_B(self, A, Lambda):
        C = {}
        for i in range(self.k - 1, -1, -1):
            for w in A[i] - A[i + 1]:
                # running modified dijkstra algorithm to get paths lengths of w from all nodes in G
                # i.e path_lengths[v] = d(w,v)
                path_lengths = modified_dijkstra(self.G, w, i, Lambda)
                # constructing shortest path tree from w according to the modified dijkstra algorithm
                shortest_path_tree = self.G.subgraph(v for v in set(self.G) if path_lengths[v] < Lambda[i + 1][v])
                # storing in C[w] a dict of dicts in the form {w:{v1:d(w,v1)}, {v2: d(w,v2)}...}
                C[w] = {v: path_lengths[v] for v in shortest_path_tree}
        B = {}
        for v in self.G:
            # B[v] is now t 2-level hash table (look it up in the article) which contains for each v in G,
            # their the nodes the belong to v's bunch, and their distance from it as calculated in path_lengths
            # in a structure very similar to the one if C[w]
            B[v] = {w: C[w][v] for w in set(self.G) if v in C[w]}
        return B

    def generate_A(self):
        A = [set() for i in range(self.k + 1)]  # initializing with k + 1 empty sets
        A[0] = set(self.G)  # A[0] = V
        p = 1 / (self.n ** (1 / float(self.k)))  # assigning p with n^(-1/k)
        for i in range(1, self.k):
            for node in A[i - 1]:
                if np.random.binomial(1, p, 1)[0]:
                    A[i].add(node)
        return A

    def generate_Lambda_and_P(self, A):
        Lambda = self.generate_empty_k_over_n_array()
        P = self.generate_empty_k_over_n_array()
        for i in range(self.k - 1, -1, -1):
            self.G.add_weighted_edges_from([(j, SOURCE, 0) for j in A[i]])
            self.run_dijkstra_from_s_to_G_and_update_Lambda_and_P(Lambda, P, A, i)

            self.G.remove_node(SOURCE)
        return Lambda, P

    def run_dijkstra_from_s_to_G_and_update_Lambda_and_P(self, Lambda, P, A, i):
        path_lengths, paths = nx.single_source_dijkstra(self.G, SOURCE)
        self.update_Lambda(Lambda, i, path_lengths)
        self.update_P(A, P, i, paths)

    def update_P(self, A, P, i, paths):
        """
        inserts for all v in V the the node u closest to v so that u in A[i]
        :param A: the A array
        :param G: The graph
        :param P: the Lambda array
        :param i: current index of A currently iterated
        :param paths: paths from source node to all nodes
        """
        for v in set(self.G) - {SOURCE}:
            for predecessor in range(len(paths[v]) - 1, -1, -1):
                if paths[v][predecessor] in A[i]:
                    P[i][v] = paths[v][predecessor]
                    break

    def update_Lambda(self, Lambda, i, path_lengths):
        """
        inserts for all v in V the weighted distance from the closest u in A[i] to v
        :param G: The graph
        :param Lambda: the Lambda array
        :param i: current index of A currently iterated
        :param path_lengths: lengths of paths from source node to all nodes
        """
        for v in set(self.G) - {SOURCE}:
            Lambda[i][v] = path_lengths[v]

    def generate_empty_k_over_n_array(self):
        """
        generate a k * n matrix with infinity as initial value on each entry
        """
        array = []
        for j in range(self.k + 1):
            array.append([float('inf') for i in range(self.n)])
        return array

    def parse_graph(self, *argv, **kwargs):
        """
        parses the user arguments.
        :returns: k, and G
        Assumptions about the input:
        1) nodes hashes are integers
        2) weights are stored under 'weight' key in every edge.
        """
        pass

    def test(self):
        """
        TODO
        """
        pass
