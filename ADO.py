import networkx as nx
import numpy as np
import pprint
SOURCE = "s"


class ADO(object):
    """

    """
    k = 5
    n = 5

    def compute_distance(self, u, v):
        """
        computes the distances according to the algorithm
        :param u: Integer representing node u
        :param v: Integer representing node v
        :returns: The distance
        """
        pass

    def pre_processing(self, G):
        """
        Gets an undirected positive weighted graph and computes:
            Lambda: array of arrays (length k * n) while Lambda[i][u] contains the distance A[i] to u.
            P: array of arrays (length k * n) while P[i][u] contains the closest node from A[i] to u.
            B: array of arrays the size of (n * len(B[v]) contains all nodes that belongs to B[v].
        :param G: A graph represented as networkx graph
        :returns: a tuple (Lambda, P, B):
        """
        A = self.generate_A(G)
        while not A[self.k - 1]:  # repeat until A[k-1] is not an empty set
            A = self.generate_A(G)
        # generating a list the size of (k * n) which will contain lambda(A[i], v) for any v in V initialized as -1
        # symbolising infinity
        distance_between_ais_and_nodes = [[-1 for i in range(len(G.nodes))] for i in range(self.k + 1)]

    def generate_A(self, G):
        A = [set() for i in range(self.k + 1)]  # initializing with k + 1 empty sets
        A[0] = set(G.nodes.keys())  # A[0] = V
        p = 1 / (self.n ** (1 / float(self.k)))  # assigning p with n^(-1/k)
        for i in xrange(1, self.k):
            for node in A[i - 1]:
                if np.random.binomial(1, p, 1)[0]:
                    A[i].add(node)
        return A

    def generate_Lambda_and_P(self, G, A):
        Lambda = self.generate_empty_k_over_n_array()
        P = self.generate_empty_k_over_n_array()
        for i in range(self.k - 1, -1, -1):
            G.add_weighted_edges_from([(j, SOURCE, 0) for j in A[i]])
            self.run_dijkstra_from_s_to_G_and_update_Lambda_and_P(G, Lambda, P, A, i)

            G.remove_node(SOURCE)
        return Lambda, P

    def run_dijkstra_from_s_to_G_and_update_Lambda_and_P(self, G, Lambda, P, A, i):
        path_lengths, paths = nx.single_source_dijkstra(G, SOURCE)
        self.update_Lambda(G, Lambda, i, path_lengths)
        self.update_P(A, G, P, i, paths)

    @staticmethod
    def update_P(A, G, P, i, paths):
        """
        inserts for all v in V the the node u closest to v so that u in A[i]
        :param A: the A array
        :param G: The graph
        :param P: the Lambda array
        :param i: current index of A currently iterated
        :param paths: paths from source node to all nodes
        """
        for v in set(G.nodes) - {SOURCE}:
            for predecessor in range(len(paths[v]) - 1, -1, -1):
                if paths[v][predecessor] in A[i]:
                    P[i][v] = paths[v][predecessor]
                    break

    @staticmethod
    def update_Lambda(G, Lambda, i, path_lengths):
        """
        inserts for all v in V the weighted distance from the closest u in A[i] to v
        :param G: The graph
        :param Lambda: the Lambda array
        :param i: current index of A currently iterated
        :param path_lengths: lengths of paths from source node to all nodes
        """
        for v in set(G.nodes) - {SOURCE}:
            Lambda[i][v] = path_lengths[v]

    def generate_empty_k_over_n_array(self):
        """
        generate a k * n matrix with infinity as initial value on each entry
        """
        array = []
        for j in xrange(self.k + 1):
            array.append([float('inf') for i in xrange(self.n)])
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
