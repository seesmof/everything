"""
- Розробити програмне забезпечення, в якому реалізується алгоритми Дейкстри, Флойда-Уоршелла та Беллмана-Форда на основі створеного відповідного класу для виконання всіх необхідних обчислень, визначення параметрів (в тому числі безпосередньо визначення графа) та отримання та виведення результатів.
- Перелік завдань, які мають бути виконані в процесі роботи над деяким проєктом групою спеціалістів, та їх запланована тривалість визначаються користувачем. Після цього користувач визначає зв’язок між даними завданнями, визначаючи завдання, які мають завершитися до початку кожного завдання. Визначити мінімальний період часу, який знадобиться на виконання проєкту.
- Мапа визначає автомобільні шляхи деякої частини міста Запоріжжя. Деякі вулиці мають односторонній рух, а на деяких можуть зустрічатися затори. Використовуючи дану інформацію та враховуючи обмеження швидкості на вулицях, визначити найкоротший шлях, яким можна дістатися з однієї заданої точки у Запоріжжі до іншої в заданий момент часу.
- Визначити найкоротші шляхи між всіма точками на мапі міста Запоріжжя, використовуючи обмеження попереднього завдання.
"""

GRAPH_FILE_PATH = "D:/code/everything/University/y2t1/DSA/tasks/lb6/input.txt"


def dijkstra():
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

        def dijkstra(self, start):
            n = len(self.graph)
            dist = [sys.maxsize] * n
            dist[start] = 0
            queue = [start]
            while queue:
                u = min(queue, key=lambda x: dist[x])
                queue.remove(u)
                for v, w in self.graph[u].items():
                    if dist[u] + w["weight"] < dist[v]:
                        dist[v] = dist[u] + w["weight"]
            return dist

        def floyed_warshall(self):
            n = len(self.graph)
            dist = [[sys.maxsize] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if i == j:
                        dist[i][j] = 0
                    elif self.graph[i][j] != 0:
                        dist[i][j] = self.graph[i][j]
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            return dist

        def bellman_ford(self, start):
            n = len(self.graph)
            dist = [sys.maxsize] * n
            dist[start] = 0
            for _ in range(n - 1):
                for u in range(n):
                    for v, w in self.graph[u].items():
                        if dist[u] + w["weight"] < dist[v]:
                            dist[v] = dist[u] + w["weight"]
            return dist

    def main():
        g = None
        while True:
            print("\nAlgorithms")
            print("1. Create graph")
            print("2. Add edge")
            print("3. Display graph")
            print("4. Dijkstra")
            print("5. Floyd-Warshell")
            print("6. Bellman-Ford")
            print("7. Exit")
            choice = int(input(": "))
            print()

            if choice == 1:
                print("1. Load from file")
                print("2. Create a new graph")
                # choice = int(input(": "))
                choice = 1
                print()

                if choice == 1:
                    # filename = input("Enter filename: ")
                    filename = GRAPH_FILE_PATH
                    g = Graph()
                    g.loadFromFile(filename)
                elif choice == 2:
                    directed = input("Is the graph directed? (y/n): ") == "y"
                    g = Graph(directed)

            elif choice == 2:
                u = input("Enter first vertex: ")
                v = input("Enter second vertex: ")
                w = int(input("Enter weight: "))
                g.addEdge(u, v, w)

            elif choice == 3:
                g.displayGraph()

            elif choice == 4:
                start = int(input("Enter start vertex: "))
                g.dijkstra(start)

            elif choice == 5:
                g.floyd_warshell()

            elif choice == 6:
                start = int(input("Enter start vertex: "))
                g.bellman_ford(start)

            else:
                break

    main()


def project_minimal_times():
    pass


def shortest_path_from_a_to_b():
    pass


def shortest_path_from_all_points():
    pass


def menu():
    while True:
        print("\nMake your choice")
        print("1. See Dijkstra, Floyd-Warshell or Bellman-Ford")
        print("2. Project minimal times")
        print("3. Shortest path from A to B")
        print("4. Shortest path from all points")
        print("5. Exit")
        choice = int(input(": "))

        if choice == 1:
            dijkstra()
        elif choice == 2:
            project_minimal_times()
        elif choice == 3:
            shortest_path_from_a_to_b()
        elif choice == 4:
            shortest_path_from_all_points()
        else:
            break


menu()
