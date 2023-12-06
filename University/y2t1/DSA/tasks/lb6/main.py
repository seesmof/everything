"""
- Розробити програмне забезпечення, в якому реалізується алгоритми Дейкстри, Флойда-Уоршелла та Беллмана-Форда на основі створеного відповідного класу для виконання всіх необхідних обчислень, визначення параметрів (в тому числі безпосередньо визначення графа) та отримання та виведення результатів.
- Перелік завдань, які мають бути виконані в процесі роботи над деяким проєктом групою спеціалістів, та їх запланована тривалість визначаються користувачем. Після цього користувач визначає зв’язок між даними завданнями, визначаючи завдання, які мають завершитися до початку кожного завдання. Визначити мінімальний період часу, який знадобиться на виконання проєкту.
- Мапа визначає автомобільні шляхи деякої частини міста Запоріжжя. Деякі вулиці мають односторонній рух, а на деяких можуть зустрічатися затори. Використовуючи дану інформацію та враховуючи обмеження швидкості на вулицях, визначити найкоротший шлях, яким можна дістатися з однієї заданої точки у Запоріжжі до іншої в заданий момент часу.
- Визначити найкоротші шляхи між всіма точками на мапі міста Запоріжжя, використовуючи обмеження попереднього завдання.
"""


from collections import defaultdict, deque
import heapq

GRAPH_FILE_PATH = "D:/code/everything/University/y2t1/DSA/tasks/lb6/input.txt"


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

    def dijkstra(self, start, end):
        shortestPaths = {start: (None, 0)}
        currentNode = start
        visited = set()

        while currentNode != end:
            visited.add(currentNode)
            destinations = self.edges[currentNode]
            currentWeight = shortestPaths[currentNode][1]

            for nextNode, weight in destinations:
                weight += currentWeight
                if nextNode not in shortestPaths:
                    shortestPaths[nextNode] = (currentNode, weight)
                else:
                    currentShortestWeight = shortestPaths[nextNode][1]
                    if currentShortestWeight > weight:
                        shortestPaths[nextNode] = (currentNode, weight)

            nextDestinations = {
                node: shortestPaths[node]
                for node in shortestPaths
                if node not in visited
            }
            if not nextDestinations:
                break
            currentNode = min(nextDestinations, key=lambda k: nextDestinations[k][1])

        if end not in shortestPaths:
            return f"There is no path from {start} to {end}"

        path = []
        while currentNode is not None:
            path.append(currentNode)
            nextNode = shortestPaths[currentNode][0]
            currentNode = nextNode
        path = path[::-1]
        return path

    def floydWarshall(self):
        distance = {
            node: {neighbor: float("inf") for neighbor in self.edges}
            for node in self.edges
        }
        nextNode = {
            node: {neighbor: None for neighbor in self.edges} for node in self.edges
        }

        for node in self.edges:
            distance[node][node] = 0
            for neighbor, weight in self.edges[node]:
                distance[node][neighbor] = weight
                nextNode[node][neighbor] = neighbor

        for k in self.edges:
            for i in self.edges:
                for j in self.edges:
                    if distance[i][k] + distance[k][j] < distance[i][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]
                        nextNode[i][j] = nextNode[i][k]

        return distance, nextNode

    def getShortestPath(self, start, end, nextNode):
        path = [start]
        while start != end:
            start = nextNode[start][end]
            path.append(start)
        return path

    def bellmanFord(self, start):
        pass


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
                dist = g.dijkstra(start, end)
                print(dist)

            elif choice == 5:
                # TODO implement floyd-warshall
                print("WHAT?")

            elif choice == 6:
                # TODO implement bellman-ford
                print("WHUT?")

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


# menu()
g = Graph()
g.loadFromFile(GRAPH_FILE_PATH)

print()
print(f"{g.dijkstra(1, 6)}\n")
print(f"{g.dijkstra(1, 8)}\n")
print(f"{g.dijkstra(1, 10)}\n")
print(f"{g.dijkstra(3, 8)}\n")

print()
print(f"{g.floydWarshall()}\n")
print(f"{g.getShortestPath(1, 6, g.floydWarshall()[1])}\n")
