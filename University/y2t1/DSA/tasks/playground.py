import networkx as nx


class Graph:
    def __init__(self, directed=False):
        self.graph = nx.Graph() if not directed else nx.DiGraph()
        self.directed = directed

    def addEdge(self, u, v, w):
        if not self.graph.has_node(u):
            self.graph.add_node(u)
        if not self.graph.has_node(v):
            self.graph.add_node(v)
        self.graph.add_edge(u, v, weight=w)
        if not self.directed:
            self.graph.add_edge(v, u, weight=w)

    def loadFromFile(self, filename):
        with open(filename, "r") as file:
            for line in file:
                u, v, w = line.strip().split()
                self.addEdge(int(u), int(v), int(w))

    def displayGraph(self):
        print("Nodes:")
        for node in self.graph.nodes():
            print(node)
        print("\nEdges:")
        for u, v, data in self.graph.edges(data=True):
            print(f"{u} 🔗 {v} - {data['weight']}")
