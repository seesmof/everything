from collections import defaultdict, deque
import networkx as nx
import matplotlib.pyplot as plt

MAZE_FILE_PATH = "D:/code/everything/University/y2t1/DSA/tasks/lb5/maze.txt"


class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def loadFromFile(self, filename):
        with open(filename, "r") as file:
            for line in file:
                u, v = line.strip().split()
                self.addEdge(u, v)

    def drawGraph(self):
        G = nx.Graph()
        for node in self.graph:
            G.add_node(node)
        for node, edges in self.graph.items():
            for edge in edges:
                G.add_edge(node, edge)

        nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")
        plt.show()


def main():
    g = None
    while True:
        print("\nMAZE")
        print("1. Display the maze")
        print("2. Exit")
        choice = int(input(": "))
        print()

        if choice == 1:
            g = Graph()
            g.loadFromFile(MAZE_FILE_PATH)
            g.drawGraph()

        else:
            break


main()
