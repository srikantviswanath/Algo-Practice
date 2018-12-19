class GraphNode(object):

    def __init__(self, data):
        self.data = data
        self.in_degree = 0


class DirectedEdge(object):

    def __init__(self, source, dest, data=None):
        self.source = source
        self.dest = dest
        self.data = data


class Graph(object):
    pass


def calculate_in_degree(graph_dict):
    in_degree_dict = {n: 0 for n in graph_dict}
    for node, nbrs in graph_dict.items():
        for nbr in nbrs:
            in_degree_dict[nbr] += 1
    return in_degree_dict
