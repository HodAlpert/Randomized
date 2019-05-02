import numpy as np


class ADO(object):
    """

    """
    k = 0

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
            Lambda: (array of arrays containing shortest paths between indices (Lambda[u][v]),
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
        n = len(G.nodes)  # assigning n with # nodes
        p = 1 / (n ** (1 / float(self.k)))  # assigning p with n^(-1/k)
        for i in xrange(1, self.k):
            for node in A[i - 1]:
                if np.random.binomial(1, p, 1)[0]:
                    A[i].add(node)
        return A

    def parse_graph(self, *argv, **kwargs):
        """
        parses the user arguments.
        :returns: k, and G
        """
        pass

    def test(self):
        """
        TODO
        """
        pass
