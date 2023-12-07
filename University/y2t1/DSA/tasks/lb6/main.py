"""
- Розробити програмне забезпечення, в якому реалізується алгоритми Дейкстри, Флойда-Уоршелла та Беллмана-Форда на основі створеного відповідного класу для виконання всіх необхідних обчислень, визначення параметрів (в тому числі безпосередньо визначення графа) та отримання та виведення результатів.
- Перелік завдань, які мають бути виконані в процесі роботи над деяким проєктом групою спеціалістів, та їх запланована тривалість визначаються користувачем. Після цього користувач визначає зв’язок між даними завданнями, визначаючи завдання, які мають завершитися до початку кожного завдання. Визначити мінімальний період часу, який знадобиться на виконання проєкту.
- Мапа визначає автомобільні шляхи деякої частини міста Запоріжжя. Деякі вулиці мають односторонній рух, а на деяких можуть зустрічатися затори. Використовуючи дану інформацію та враховуючи обмеження швидкості на вулицях, визначити найкоротший шлях, яким можна дістатися з однієї заданої точки у Запоріжжі до іншої в заданий момент часу.
- Визначити найкоротші шляхи між всіма точками на мапі міста Запоріжжя, використовуючи обмеження попереднього завдання.
"""


from collections import defaultdict
from heapq import heappop, heappush
from json import dumps
import matplotlib.pyplot as plt
import networkx as nx

GRAPH_FILE_PATH = "D:/code/everything/University/y2t1/DSA/tasks/lb6/data/graph.txt"
ROADS_FILE_PATH = "D:/code/everything/University/y2t1/DSA/tasks/lb6/data/roads.txt"


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

    def floydWarshall(self):
        dist = defaultdict(lambda: defaultdict(lambda: float("inf")))
        next_node = defaultdict(dict)
        for u in self.edges:
            dist[u][u] = 0
            for v, weight in self.edges[u]:
                dist[u][v] = weight
                next_node[u][v] = v

        for k in self.edges:
            for i in self.edges:
                for j in self.edges:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_node[i][j] = next_node[i][k]

        return dist, next_node

    def shortestPath(self, start, end):
        _, next_node = self.floydWarshall()
        if next_node[start][end] is None:
            return None  # No path exists

        path = [start]
        while start != end:
            start = next_node[start][end]
            path.append(start)

        return path

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
                for nextNode, c in self.edges[node]:
                    if nextNode not in seen:
                        heappush(queue, (cost + c, nextNode, path))
        return []

    def bellmanFord(self, start, end):
        distance = {node: float("infinity") for node in self.edges}
        distance[start] = 0
        predecessor = {node: None for node in self.edges}

        for _ in range(len(self.edges) - 1):
            for node in self.edges:
                for neighbour, weight in self.edges[node]:
                    if distance[node] + weight < distance[neighbour]:
                        distance[neighbour] = distance[node] + weight
                        predecessor[neighbour] = node

        for node in self.edges:
            for neighbour, weight in self.edges[node]:
                assert (
                    distance[node] + weight >= distance[neighbour]
                ), "Graph contains a negative-weight cycle"

        path = []
        current_node = end
        while current_node is not None:
            path.append(current_node)
            current_node = predecessor[current_node]
        path.reverse()

        return path


def algorithms():
    def main():
        g = None
        while True:
            print("\nALGORITHMS")
            print("1. Create a new graph")
            print("2. Add an edge")
            print("3. Display graph")
            print("4. Dijkstra")
            print("5. Floyd-Warshall")
            print("6. Bellman-Ford")
            print("7. Exit")
            choice = int(input(": "))
            print()

            if choice == 1:
                print("1. Load from file")
                print("2. Create a new graph")
                # choice = int(input(": "))
                choice = 1

                if choice == 1:
                    # filename = input("Enter the filename: ")
                    filename = GRAPH_FILE_PATH
                    g = Graph()
                    g.loadFromFile(filename)
                elif choice == 2:
                    directed = input("Is the graph directed? (y/n): ") == "y"
                    g = Graph(directed)
                g.displayGraph()

            elif choice == 2:
                u = int(input("Enter the first vertex: "))
                v = int(input("Enter the second vertex: "))
                g.addEdge(u, v)

            elif choice == 3:
                g.displayGraph()

            elif choice == 4:
                start = int(input("Enter the source vertex: "))
                end = int(input("Enter the destination vertex: "))
                res = g.dijkstra(start, end)
                g.drawGraph(res)

            elif choice == 5:
                start = int(input("Enter the source vertex: "))
                end = int(input("Enter the destination vertex: "))
                res = g.shortestPath(start, end)
                g.drawGraph(res)

            elif choice == 6:
                start = int(input("Enter the source vertex: "))
                end = int(input("Enter the destination vertex: "))
                res = g.bellmanFord(start, end)
                g.drawGraph(res)

            else:
                break

    main()


def project_minimal_times():
    # create graph
    g = Graph()
    # take in the number of tasks
    numTasks = int(input("Enter the number of tasks: "))
    # define the connections between tasks and time to complete each
    # find the shortest path among all paths
    # print the total time it takes to complete all tasks


def shortest_path_from_a_to_b():
    # create a graph
    g = Graph()
    # take in the graph of roads


def shortest_path_from_all_points():
    pass


def menu():
    while True:
        print("\nMake your choice")
        print("1. See Dijkstra, Floyd-Warshall or Bellman-Ford")
        print("2. Project minimal times")
        print("3. Shortest path from A to B")
        print("4. Shortest path from all points")
        print("5. Exit")
        # choice = int(input(": "))
        choice = 1

        if choice == 1:
            algorithms()
        elif choice == 2:
            project_minimal_times()
        elif choice == 3:
            shortest_path_from_a_to_b()
        elif choice == 4:
            shortest_path_from_all_points()
        else:
            break


menu()
