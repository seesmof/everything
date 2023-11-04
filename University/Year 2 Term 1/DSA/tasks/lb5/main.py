from collections import deque


class Graph:
    def __init__(self, edges, directed=False):
        self.adj_list = {}
        self.directed = directed

        for u, v in edges:
            if u not in self.adj_list:
                self.adj_list[u] = []
            if v not in self.adj_list:
                self.adj_list[v] = []
            self.add_edge(u, v)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        if not self.directed:
            self.adj_list[v].append(u)

    def depth_first_search(self, start):
        visited = {node: False for node in self.adj_list}
        traversal = []
        forest = []

        def dfs(node):
            visited[node] = True
            traversal.append(node)

            for neighbour in self.adj_list[node]:
                if not visited[neighbour]:
                    forest.append((node, neighbour))
                    dfs(neighbour)

        dfs(start)
        return traversal, forest

    def breadth_first_search(self, start):
        visited = {node: False for node in self.adj_list}
        traversal = []
        tree = []
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if visited[node]:
                continue

            visited[node] = True
            traversal.append(node)

            for neighbour in self.adj_list[node]:
                if not visited[neighbour]:
                    tree.append((node, neighbour))
                    queue.append(neighbour)

        return traversal, tree


edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]

g = Graph(edges, directed=True)
traversal, forest = g.depth_first_search(1)

print(f"\nDFS traversal: {traversal}")
print(f"\nDFS forest: {forest}")


g = Graph(edges, directed=True)
traversal, tree = g.breadth_first_search(1)

print(f"\nBFS traversal: {traversal}")
print(f"\nBFS tree: {tree}")
