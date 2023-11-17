import networkx as nx
import sys


def dijkstra(graph, start):
    n = len(graph)
    dist = [sys.maxsize] * n
    dist[start] = 0
    queue = [start]
    while queue:
        u = min(queue, key=lambda x: dist[x])
        queue.remove(u)
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist


def floyd_warshall(graph):
    n = len(graph)
    dist = [[sys.maxsize] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


def bellman_ford(graph, start):
    n = len(graph)
    dist = [sys.maxsize] * n
    dist[start] = 0
    for _ in range(n - 1):
        for u in range(n):
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
    return dist


# Create an empty graph
G = nx.Graph()

# Add nodes to the graph
G.add_node(1)
G.add_node(2)
G.add_node(3)

# Add edges to the graph
G.add_edge(1, 2, weight=6)
G.add_edge(1, 3, weight=1)
G.add_edge(2, 3, weight=5)
# Get the adjacency list of the graph
graph = nx.to_dict_of_lists(G)

# Now you can use the graph in your algorithms
print(dijkstra(graph, 1))
print(floyd_warshall(graph))
print(bellman_ford(graph, 1))
