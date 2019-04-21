class ADO(object):
    """

    """
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
        pass

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

