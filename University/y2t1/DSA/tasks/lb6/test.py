from collections import defaultdict
from heapq import heappop, heappush
from json import dumps
import matplotlib.pyplot as plt
import networkx as nx


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

    def drawGraph(self, shortest_path=None):
        G = nx.Graph()
        for u, edges in self.edges.items():
            for v, weight in edges:
                G.add_edge(u, v, weight=weight)
        pos = nx.spring_layout(G)

        if shortest_path:
            node_colors = [
                "red"
                if node == shortest_path[-1]
                else "lightgreen"
                if node == shortest_path[0]
                else "lightgray"
                for node in G.nodes()
            ]
            nx.draw_networkx_nodes(G, pos, node_color=node_colors)

            plt.text(
                0.00,
                1.13,
                "Red: End",
                transform=plt.gca().transAxes,
                fontsize=10,
                verticalalignment="top",
                bbox=dict(boxstyle="round", facecolor="red", alpha=0.5),
            )
            plt.text(
                0.00,
                1.06,
                "Green: Start",
                transform=plt.gca().transAxes,
                fontsize=10,
                verticalalignment="top",
                bbox=dict(boxstyle="round", facecolor="lightgreen", alpha=0.5),
            )
        else:
            nx.draw_networkx_nodes(G, pos, node_color="lightblue")
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos, font_weight="bold")

        if shortest_path:
            edges = [
                (shortest_path[i], shortest_path[i + 1])
                for i in range(len(shortest_path) - 1)
            ]
            nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color="red", width=2)

        labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

    def loadFromFile(self, filename):
        with open(filename, "r") as file:
            for line in file:
                try:
                    u, v, w = line.strip().split()
                    self.addEdge(int(u), int(v), int(w))
                except ValueError:
                    print(f"Skipping line {line}")

    def dijkstra(self, start, end):
        queue = [(0, start, [])]
        seen = set()
        while queue:
            (cost, node, path) = heappop(queue)
            if node not in seen:
                seen.add(node)
                path = path + [node]
                if node == end:
                    return path
                for next_node, c in self.edges[node]:
                    if next_node not in seen:
                        heappush(queue, (cost + c, next_node, path))
        return []

    def floyd_warshall(self, start, end):
        dist = defaultdict(lambda: defaultdict(lambda: float("inf")))
        next_node = defaultdict(dict)

        for node in self.edges:
            dist[node][node] = 0

        for node, edges in self.edges.items():
            for neighbor, weight in edges:
                dist[node][neighbor] = weight
                next_node[node][neighbor] = neighbor

        for k in self.edges:
            for i in self.edges:
                for j in self.edges:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_node[i][j] = next_node[i][k]

        if next_node[start][end] is None:
            return []
        path = [start]
        while start != end:
            start = next_node[start][end]
            path.append(start)
        return path


GRAPH_FILE_PATH = "D:/code/everything/University/y2t1/DSA/tasks/lb6/data/graph.txt"
ROADS_FILE_PATH = "D:/code/everything/University/y2t1/DSA/tasks/lb6/data/roads.txt"

"""
g = Graph(directed=True)
g.loadFromFile(GRAPH_FILE_PATH)
g.displayGraph()
g.drawGraph()
res = g.dijkstra(0, 2)
g.drawGraph(res)
"""

g = Graph(directed=False)
g.loadFromFile(ROADS_FILE_PATH)
g.displayGraph()
g.drawGraph()
res = g.dijkstra(3, 2)
g.drawGraph(res)
res = g.floyd_warshall(3, 2)
g.drawGraph(res)

# ! OKAY DONT TOUCH THIS
