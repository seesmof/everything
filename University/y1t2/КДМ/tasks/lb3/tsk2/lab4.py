from collections import defaultdict


def ford_fulkerson(graph, source, sink):
    # Create residual graph with same edges as original graph
    residual_graph = defaultdict(dict)
    for u, v, capacity in graph:
        residual_graph[u][v] = capacity
        residual_graph[v][u] = 0

    # Find augmenting paths and increase flow
    while True:
        # Find augmenting path using BFS
        parent = {}
        queue = [(source, float('inf'))]
        parent[source] = None
        while queue:
            u, flow = queue.pop(0)
            for v, capacity in residual_graph[u].items():
                if v not in parent and capacity > 0:
                    parent[v] = u
                    new_flow = min(flow, capacity)
                    if v == sink:
                        # Augmenting path found, increase flow and return to step 2
                        while v != source:
                            u = parent[v]
                            residual_graph[u][v] -= new_flow
                            residual_graph[v][u] += new_flow
                            v = u
                        break
                    queue.append((v, new_flow))
            else:
                continue
            break
        else:
            # No augmenting path found, terminate algorithm
            break

    # Calculate maximum flow
    max_flow = sum(residual_graph[source].values())
    return max_flow


graph = [
    (0, 1, 16),
    (0, 2, 13),
    (1, 2, 10),
    (1, 3, 12),
    (2, 1, 4),
    (2, 4, 14),
    (3, 2, 9),
    (3, 5, 20),
    (4, 3, 7),
    (4, 5, 4),
]

source = 0
sink = 5

max_flow = ford_fulkerson(graph, source, sink)
print("Maximum flow:", max_flow)
