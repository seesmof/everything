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
        else:
            nx.draw_networkx_nodes(G, pos, node_color="lightblue")
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos, font_weight="bold")
        labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        if shortest_path:
            edges = [
                (shortest_path[i], shortest_path[i + 1])
                for i in range(len(shortest_path) - 1)
            ]
            nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color="red", width=2)

        plt.show()

    def loadFromFile(self, filename):
        with open(filename, "r") as file:
            for line in file:
                try:
                    u, v, w = line.strip().split()
                    self.addEdge(int(u), int(v), int(w))
                except ValueError:
                    print(f"Skipping line {line}")


GRAPH_FILE_PATH = "D:/code/everything/University/y2t1/DSA/tasks/lb6/data/graph.txt"
g = Graph(directed=True)
g.loadFromFile(GRAPH_FILE_PATH)
g.displayGraph()
g.drawGraph()
g.drawGraph([0, 1, 2])

# ! OKAY DONT TOUCH THIS
