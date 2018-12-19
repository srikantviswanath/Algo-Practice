"""
4.1 Given a directed graph, design an algorithm to find out whether there is a route between 2 nodes.
If present, print out the path
"""
from functools import reduce

def is_route_present_bfs(graph, source, dest):
    from collections import deque

    if not graph or source not in graph or dest not in list(reduce(lambda s1, s2: s1.union(s2),graph.values())):
        return False
    Q = deque()
    seen = {source}
    Q.append(source)
    while Q:
        dqed = Q.popleft()
        leaf = dqed[-1]
        for nbr in graph.get(leaf, set()):
            if nbr == dest:
                return dqed + nbr
            if nbr not in seen:
                Q.append(dqed + nbr)
                seen.add(nbr)
    return False


if __name__ == '__main__':
    A, B, C, D, E = 'A', 'B', 'C', 'D', 'E'
    graph = {
        A: {B, C},
        B: {D, C, A},
        D: {E, C, B},
        E: {D},
        
    }
    print(is_route_present_bfs(graph, E, A))