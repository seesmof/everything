from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.container = defaultdict(list)

    def addNode(self, parent, child):
        self.container[parent].append(child)

    def DFS(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for neighbor in self.container[start]:
            if neighbor not in visited:
                self.DFS(neighbor, visited)

    def outputGraph(self):
        # output the graph to console
        for key, value in self.container.items():
            print(f"{key}: {', '.join(sorted(value))}")

    def drawGraph(self):
        # declare a networkx graph and add all the edges to it
        networkGraph = nx.Graph()
        for node, edges in self.container.items():
            for edge in edges:
                networkGraph.add_edge(node, edge)
        # define a node size based on the degree
        degree = dict(networkGraph.degree())
        # draw a graph and show it
        nx.draw(
            networkGraph,
            with_labels=True,
            node_size=[v * 100 for v in degree.values()],
            font_weight="bold",
            node_color="lightblue",
        )
        # as a plot
        plt.show()


g = Graph()
g.addNode(1, 2)
g.addNode(1, 3)
g.addNode(1, 4)
g.addNode(2, 3)
g.addNode(2, 4)
g.addNode(3, 4)
g.addNode(5, 3)
g.addNode(5, 4)
g.addNode(6, 1)
g.addNode(6, 2)
g.addNode(7, 6)
g.addNode(7, 2)
g.addNode(7, 5)
g.addNode(8, 6)
g.addNode(8, 3)
g.addNode(8, 1)
g.addNode(8, 7)

print("Depth First Traversal (starting from vertex 2):")
g.DFS(8)
