from graphs import calculate_in_degree
from collections import deque


def topological_sort_stacks(graph_dict):
    start_nodes = [node for node, degree in calculate_in_degree(graph_dict).items() if degree == 0]
    if not start_nodes:
        raise ReferenceError('Circular dependency detected')
    stack1, stack2 = [], []
    stack1_track, stack2_track = set(), set()
    while start_nodes:
        new = start_nodes.pop()
        stack1.append(new)
        stack1_track.add(new)
        while stack1:
            top = stack1[-1]
            if graph_dict[top]:
                next_node = graph_dict[top].pop()
                if next_node in stack1_track:
                    raise ReferenceError('Circular dependency detected')
                elif next_node not in stack2_track:
                    stack1.append(next_node)
                    stack1_track.add(next_node)
            else:
                popped = stack1.pop()
                stack1_track.remove(popped)
                stack2.append(popped)
                stack2_track.add(popped)
    return stack2[::-1]


def topological_sort_bfs(graph_dict):
    in_degree_dict = calculate_in_degree(graph_dict)
    start_nodes = [node for node, degree in in_degree_dict.items() if degree == 0]
    if not start_nodes:
        raise ReferenceError('Circular dependency detected')
    q = deque()
    output = []
    for node in start_nodes:
        q.append(node)
    while q:
        popped = q.popleft()
        output.append(popped)
        q_count = len(q)
        for nbr in graph_dict[popped]:
            in_degree_dict[nbr] -= 1
            if in_degree_dict[nbr] == 0:
                q.append(nbr)
        if len(q) == q_count and graph_dict[popped]:
            raise ReferenceError('Circular dependency detected')
    return output




if __name__ == '__main__':
    a, b, c, d, e, f, g, h, i = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'
    # graph_dict = {
    #     a: [b, c],
    #     b: [e, f],
    #     c: [b, d],
    #     d: [b],
    #     e: [f],
    #     f: [],
    #     g: [h, i],
    #     h: [],
    #     i: []
    # }
    graph_dict = {
        a: [b],
        b: [c, d],
        c: [],
        d: [e],
        e: [b]
    }
    print(topological_sort_bfs(graph_dict))