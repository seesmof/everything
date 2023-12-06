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

    def floydWarshall(self):
        distance = {
            node: {neighbor: float("inf") for neighbor in self.edges}
            for node in self.edges
        }
        for node in self.edges:
            distance[node][node] = 0
            for neighbor, weight in self.edges[node]:
                distance[node][neighbor] = weight

        # Update the distance matrix
        for k in self.edges:
            for i in self.edges:
                for j in self.edges:
                    distance[i][j] = min(
                        distance[i][j], distance[i][k] + distance[k][j]
                    )

        return distance


GRAPH_FILE_PATH = "D:/code/everything/University/y2t1/DSA/tasks/lb6/input.txt"


g = Graph()
g.loadFromFile(GRAPH_FILE_PATH)
g.displayGraph()

res = g.floydWarshall()
# Define your points
pointA = 1
pointB = 5

# Get the shortest path from point A to point B
shortest_path = res[pointA][pointB]

print(f"The shortest path from point {pointA} to point {pointB} is {shortest_path}")
