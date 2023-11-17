from collections import defaultdict


class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed
        self.sums = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def DFS(self, v, visited=None, path=None, sum=0):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        stack = [(v, visited, path, sum)]
        while stack:
            vertex, visited, path, sum = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                path.append(vertex)
                sum += vertex
                stack.extend(
                    (u, visited.copy(), path.copy(), sum)
                    for u in set(self.graph[vertex]) - visited
                )
                self.sums[v].append((sum, path))
        return visited

    def displayForest(self, v):
        print("Depth-first search forest:")
        self.DFS(v)
        print()

    def findPaths(self, v, target):
        paths = []
        for sum, path in self.sums[v]:
            if sum == target:
                paths.append(path)
        return paths
