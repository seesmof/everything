from collections import defaultdict


class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def DFS(self, v, visited=None):
        if visited is None:
            visited = set()
        stack = [v]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex, end=" ")
                stack.extend(set(self.graph[vertex]) - visited)
        return visited

    def displayForest(self, v):
        print("Depth-first search forest:")
        self.DFS(v)
        print()
