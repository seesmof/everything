from collections import defaultdict, deque
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

    def loadFromFile(self, filename):
        with open(filename, "r") as file:
            for line in file:
                try:
                    u, v, w = line.strip().split()
                    self.addEdge(int(u), int(v), int(w))
                except ValueError:
                    print(f"Skipping line {line}")

    def drawGraph(self, shortest_path=None):
        G = nx.Graph()
        for u, edges in self.edges.items():
            for v, weight in edges:
                G.add_edge(u, v, weight=weight)
        pos = nx.spring_layout(G, k=0.15)

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
                "Red: Last Task",
                transform=plt.gca().transAxes,
                fontsize=10,
                verticalalignment="top",
                bbox=dict(boxstyle="round", facecolor="red", alpha=0.5),
            )
            plt.text(
                0.00,
                1.06,
                "Green: First Task",
                transform=plt.gca().transAxes,
                fontsize=10,
                verticalalignment="top",
                bbox=dict(boxstyle="round", facecolor="lightgreen", alpha=0.5),
            )
        else:
            nx.draw_networkx_nodes(G, pos, node_color="lightblue")
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos, font_weight="bold")
        labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

    def calculateMinimumTime(self):
        totalTime = 0
        for edges in self.edges.values():
            for edge in edges:
                totalTime += edge[1]
        return totalTime


GRAPH_FILE_PATH = "D:/code/everything/University/y2t1/DSA/tasks/lb6/data/tasks.txt"


def project_minimal_times():
    g = Graph(directed=True)
    ADD_TASKS_MESSAGE = "Please add tasks first. The graph is empty now."

    while True:
        print("\nTASKS")
        print("1. Add tasks")
        print("2. Display graph")
        print("3. Calculate minimal time")
        print("4. Exit")
        choice = int(input(": "))
        print()

        if choice == 1:
            print("How would you like to add tasks?")
            print("1. Manually")
            print("2. Load from file")
            choice = int(input(": "))
            print()

            if choice == 1:
                print("Enter the total number of tasks the team has to complete")
                numberOfTasks = int(input(": "))
                for i in range(numberOfTasks):
                    taskNumber = i + 1
                    timeToComplete = int(
                        input(f"Enter time it takes to complete task {taskNumber}: ")
                    )
                    g.addEdge(taskNumber, taskNumber + 1, timeToComplete) if i != (
                        numberOfTasks - 1
                    ) else g.addEdge(taskNumber, 0, timeToComplete)
            elif choice == 2:
                filename = input("Enter the filename: ")
                g.loadFromFile(filename)

        elif choice == 2:
            if not g.edges:
                print(ADD_TASKS_MESSAGE)
                continue

            print("Where to display?")
            print("1. Console")
            print("2. Graph")
            choice = int(input(": "))

            if choice == 1:
                g.displayGraph()
            elif choice == 2:
                g.drawGraph([1, 0])

        elif choice == 3:
            if not g.edges:
                print(ADD_TASKS_MESSAGE)
                continue

            res = g.calculateMinimumTime()
            print(
                f"The minimum time it will take to complete all tasks is {res} hours."
            )

        else:
            break


project_minimal_times()
