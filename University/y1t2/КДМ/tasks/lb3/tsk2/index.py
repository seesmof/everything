import networkx as nx
graph = nx.Graph()

''''''
num_vertices = int(input("\nВведіть кількість вершин: "))
print()

for i in range(1, num_vertices+1):
    for j in range(i+1, num_vertices+1):
        if i != j:
            weight = int(
                input(f"Введіть вагу між вершиною {i} та {j}: "))
            if weight != 0:
                graph.add_edge(i, j, weight=weight)

'''
graph.add_edge(1, 2, weight=4)
graph.add_edge(1, 3, weight=3)
graph.add_edge(1, 4, weight=2)
graph.add_edge(2, 5, weight=2)
graph.add_edge(2, 7, weight=1)
graph.add_edge(3, 5, weight=6)
graph.add_edge(3, 6, weight=7)
graph.add_edge(4, 6, weight=2)
graph.add_edge(4, 7, weight=4)
graph.add_edge(5, 8, weight=7)
graph.add_edge(5, 9, weight=5)
graph.add_edge(6, 8, weight=4)
graph.add_edge(6, 10, weight=3)
graph.add_edge(7, 9, weight=4)
graph.add_edge(7, 10, weight=5)
graph.add_edge(8, 11, weight=7)
graph.add_edge(9, 11, weight=1)
graph.add_edge(10, 11, weight=3)
'''

T = nx.minimum_spanning_tree(graph)
print(f"\nМінімальне остовне дерево:")

total_weight = 0
for u, v, data in T.edges(data=True):
    weight = data['weight']
    print(f"{u} -- {v} = {weight}")
    total_weight += weight
print(f"Вага дерева = {total_weight}")


def dijkstra(graph, start, end):
    dist = {v: float('inf') for v in graph.nodes()}
    dist[start] = 0
    prev = {}
    unvisited = set(graph.nodes())
    while unvisited:
        current = min(unvisited, key=lambda v: dist[v])
        unvisited.remove(current)
        if dist[current] == float('inf'):
            break
        for neighbor in graph.neighbors(current):
            tentative_dist = dist[current] + graph[current][neighbor]['weight']
            if tentative_dist < dist[neighbor]:
                dist[neighbor] = tentative_dist
                prev[neighbor] = current
    path = []
    current = end
    while current != start:
        path.append(current)
        current = prev[current]
    path.append(start)
    path.reverse()
    path_str = " -> ".join(str(v) for v in path)
    return path_str


start = list(graph.nodes())[0]
end = list(graph.nodes())[-1]
shortest_path = dijkstra(graph, start, end)
print(f"\nНайкоротший шлях: {shortest_path}\n")
