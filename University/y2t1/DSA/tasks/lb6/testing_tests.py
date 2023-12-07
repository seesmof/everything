from collections import defaultdict, deque
from heapq import heappop, heappush
from json import dumps
import matplotlib.pyplot as plt
import networkx as nx
from numpy import average


def shortest_path_from_a_to_b():
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

        def dijkstra(self, start, end):
            # Initialize a priority queue with a tuple containing the cost, the current node, and the path taken so far
            queue = [(0, start, [])]

            # Create an empty set to keep track of visited nodes
            seen = set()

            # Continue looping while there are nodes in the queue
            while queue:
                # Pop the node with the lowest cost from the queue
                (cost, node, path) = heappop(queue)

                # Check if the node has been visited before
                if node not in seen:
                    # Mark the node as visited
                    seen.add(node)

                    # Append the current node to the path taken so far
                    path = path + [node]

                    # Check if the current node is the destination node
                    if node == end:
                        # Return the path taken
                        return path

                    # Iterate over the edges of the current node
                    for nextNode, c in self.edges[node]:
                        # Check if the next node has not been visited
                        if nextNode not in seen:
                            # Calculate the new cost by adding the cost of the current node and the cost of the edge to the next node
                            newCost = cost + c

                            # Add the next node to the queue with the updated cost and path
                            heappush(queue, (newCost, nextNode, path))

            # If the destination node cannot be reached, return an empty path
            return []

    GRAPH_FILE_PATH = "D:/code/everything/University/y2t1/DSA/tasks/lb6/data/roads.txt"
    g = Graph(directed=True)
    g.loadFromFile(GRAPH_FILE_PATH)
    # g.drawGraph(g.dijkstra(6, 5))

    while True:
        print("\nROUTE")
        print("1. Add Edge")
        print("2. Display Graph")
        print("3. Find Shortest Path")
        print("4. Exit")
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
            doesHaveTraffic = input("Does this road have a traffic jam? (y/n): ") == "y"

            weight += 5 if doesHaveTraffic else 0

            if isOneWay:
                g.addEdge(u, v, weight)
            else:
                g.addEdge(u, v, weight)
                g.addEdge(v, u, weight)

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
            end = int(input("Enter the destination vertex: "))
            res = g.dijkstra(start, end)
            print(res)
            g.drawGraph(res)


shortest_path_from_a_to_b()
