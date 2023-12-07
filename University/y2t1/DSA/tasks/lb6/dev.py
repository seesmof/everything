from collections import defaultdict, deque
from heapq import heappop, heappush
from json import dumps
import matplotlib.pyplot as plt
import networkx as nx
from numpy import average


def shortest_path_from_all_points():
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
            G = nx.DiGraph() if self.directed else nx.Graph()
            for u, edges in self.edges.items():
                for v, weight in edges:
                    G.add_edge(u, v, weight=weight)
            pos = nx.spring_layout(G, k=0.5)

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
            nx.draw_networkx_edges(
                G, pos, arrowstyle="->"
            ) if self.directed else nx.draw_networkx_edges(G, pos)
            nx.draw_networkx_labels(G, pos, font_weight="bold")

            if shortest_path:
                edges = [
                    (shortest_path[i], shortest_path[i + 1])
                    for i in range(len(shortest_path) - 1)
                ]
                nx.draw_networkx_edges(
                    G, pos, edgelist=edges, edge_color="red", arrowstyle="->", width=2
                ) if self.directed else nx.draw_networkx_edges(
                    G, pos, edgelist=edges, edge_color="red", width=2
                )

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
                        pass

        def floydWarshall(self):
            # Initialize a defaultdict to store the shortest distances between nodes
            dist = defaultdict(lambda: defaultdict(lambda: float("inf")))
            # Initialize a defaultdict to store the next node in the shortest path
            nextNode = defaultdict(dict)

            # Iterate over each node in the graph
            for u in self.edges:
                # Set the distance from a node to itself as 0
                dist[u][u] = 0
                # Iterate over each neighbor of the current node
                for v, weight in self.edges[u]:
                    # Set the distance to the neighbor node
                    dist[u][v] = weight
                    # Set the next node in the shortest path to be the neighbor node
                    nextNode[u][v] = v

            # Iterate over each intermediate node
            for k in self.edges:
                # Iterate over each source node
                for i in self.edges:
                    # Iterate over each destination node
                    for j in self.edges:
                        # If the distance from i to k plus the distance from k to j is smaller than the current distance from i to j
                        if dist[i][k] + dist[k][j] < dist[i][j]:
                            # Update the distance from i to j
                            dist[i][j] = dist[i][k] + dist[k][j]
                            # Update the next node in the shortest path from i to j
                            nextNode[i][j] = nextNode[i][k]

            # Return the shortest distances and next nodes
            return dist, nextNode

        def shortestPath(self, start, end):
            # Run the Floyd-Warshall algorithm to get the nextNode matrix
            distances, nextNode = self.floydWarshall()

            # If there is no path from start to end, return None
            if nextNode[start][end] is None:
                return None

            # Create a list to store the path
            path = [start]

            # Traverse the nextNode matrix to find the shortest path from start to end
            while start != end:
                start = nextNode[start][
                    end
                ]  # Update the current node to the next node in the path
                path.append(start)  # Add the current node to the path

            # Return the shortest path
            return path

    def main():
        g = Graph()
        g.loadFromFile(
            "D:/code/everything/University/y2t1/DSA/tasks/lb6/data/simple.txt"
        )
        while True:
            print("\nALL THE ROUTES")
            print("1. Add Edge")
            print("2. Display Graph")
            print("3. Display Shortest Paths")
            print("4. Exit")
            choice = int(input("Enter your choice: "))
            print()

            if choice == 1:
                print("How to add an edge?")
                print("1. Manually")
                print("2. From File")
                choice = int(input("Enter your choice: "))
                print()

                if choice == 1:
                    print(
                        "Enter the starting node, ending node and weight. Separate them with a space"
                    )
                    u, v, weight = map(
                        int,
                        input(": ").split(),
                    )

                    isOneWay = input("Is this a one-way road? (y/n): ") == "y"
                    doesHaveTraffic = (
                        input("Does this road have a traffic jam? (y/n): ") == "y"
                    )

                    weight += 5 if doesHaveTraffic else 0

                    if isOneWay:
                        g.addEdge(u, v, weight)
                    else:
                        g.addEdge(u, v, weight)
                        g.addEdge(v, u, weight)

                elif choice == 2:
                    filename = input("Enter the filename: ")
                    g.loadFromFile(filename)

            elif choice == 2:
                print("How to display?")
                print("1. Console")
                print("2. Graph")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    g.displayGraph()

                elif choice == 2:
                    g.drawGraph()

            elif choice == 3:
                start = int(input("Enter the starting node: "))

                for currentNode in g.edges:
                    if start != currentNode:
                        res = g.shortestPath(start, currentNode)
                        print(f"{start} -> {currentNode}: {res}")
                        g.drawGraph(res)

    main()


shortest_path_from_all_points()
