from collections import defaultdict, deque


class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def BFS(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(set(self.graph[vertex]) - visited)

        return visited

    def displayTree(self, start):
        visited = set()
        queue = deque([start])
        tree = defaultdict(list)

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        tree[vertex].append(neighbor)
                        queue.append(neighbor)

        return tree

    def displayResults(self, start):
        visited = self.BFS(start)
        print(f"BFS traversal: {visited}")


g = Graph()

# Add edges to the graph
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(3, 6)
g.addEdge(3, 7)
# Perform a BFS traversal starting from vertex 1
g.displayResults(1)
# Display the BFS tree
tree = dict(g.displayTree(1))
for key, value in tree.items():
    print(f"{key}: {value}")
