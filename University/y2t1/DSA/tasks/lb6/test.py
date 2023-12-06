from collections import defaultdict
from json import dumps


class Graph:
    def __init__(self, directed=False):
        self.edges = defaultdict(list)
        self.directed = directed

    def addEdge(self, u, v, weight):
        self.edges[u].append((v, weight))
        if not self.directed:
            self.edges[v].append((u, weight))

    def displayGraph(self):
        for key, value in self.edges.items():
            if self.directed:
                print(f"{key} → {', '.join(map(str, value))}")
            else:
                print(f"{key} 🔗 {', '.join(map(str, value))}")

    def loadFromFile(self, filename):
        with open(filename, "r") as file:
            for line in file:
                try:
                    u, v, w = line.strip().split()
                    self.addEdge(int(u), int(v), int(w))
                except ValueError:
                    print(f"Skipping line {line}")

    def bellmanFord(self, start):
        distance = {node: float("infinity") for node in self.edges}
        distance[start] = 0

        for _ in range(len(self.edges) - 1):
            for node in self.edges:
                for neighbour, weight in self.edges[node]:
                    if (
                        distance[node] != float("infinity")
                        and distance[node] + weight < distance[neighbour]
                    ):
                        distance[neighbour] = distance[node] + weight

        for node in self.edges:
            for neighbour, weight in self.edges[node]:
                if (
                    distance[node] != float("infinity")
                    and distance[node] + weight < distance[neighbour]
                ):
                    return "Graph contains a negative-weight cycle"

        return distance

    def getShortestPath(self, start, end, nextNode):
        if nextNode[start][end] is None:
            return f"There is no path from {start} to {end}"
        path = [start]
        while start != end:
            start = nextNode[start][end]
            path.append(start)
        return path


GRAPH_FILE_PATH = "D:/code/everything/University/y2t1/DSA/tasks/lb6/input.txt"
g = Graph()
g.loadFromFile(GRAPH_FILE_PATH)
g.displayGraph()

# ! OKAY DONT TOUCH THIS

start = 1
print(dumps(g.bellmanFord(start), indent=2))
