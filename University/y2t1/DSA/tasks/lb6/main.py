"""
- Розробити програмне забезпечення, в якому реалізується алгоритми Дейкстри, Флойда-Уоршелла та Беллмана-Форда на основі створеного відповідного класу для виконання всіх необхідних обчислень, визначення параметрів (в тому числі безпосередньо визначення графа) та отримання та виведення результатів.
- Перелік завдань, які мають бути виконані в процесі роботи над деяким проєктом групою спеціалістів, та їх запланована тривалість визначаються користувачем. Після цього користувач визначає зв’язок між даними завданнями, визначаючи завдання, які мають завершитися до початку кожного завдання. Визначити мінімальний період часу, який знадобиться на виконання проєкту.
- Мапа визначає автомобільні шляхи деякої частини міста Запоріжжя. Деякі вулиці мають односторонній рух, а на деяких можуть зустрічатися затори. Використовуючи дану інформацію та враховуючи обмеження швидкості на вулицях, визначити найкоротший шлях, яким можна дістатися з однієї заданої точки у Запоріжжі до іншої в заданий момент часу.
- Визначити найкоротші шляхи між всіма точками на мапі міста Запоріжжя, використовуючи обмеження попереднього завдання.
"""


GRAPH_FILE_PATH = "D:/code/everything/University/y2t1/DSA/tasks/lb6/input.txt"


def algorithms():
    from collections import defaultdict, deque
    import heapq

    class Graph:
        def __init__(self, directed=False):
            self.graph = defaultdict(list)
            self.directed = directed

        def addEdge(self, u, v, w):
            self.graph[u].append((v, w))
            if not self.directed:
                self.graph[v].append((u, w))

        def displayGraph(self):
            for key, value in self.graph.items():
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

        def dfs(self, start):
            visited = set()
            stack = [start]
            while stack:
                vertex = stack.pop()
                if vertex not in visited:
                    visited.add(vertex)
                    stack.extend(set(self.graph[vertex]) - visited)
            return visited

        def dijkstra(self, start):
            distances = {vertex: float("inf") for vertex in self.graph}
            distances[start] = 0
            queue = [(0, start)]
            while queue:
                currentDistance, currentVertex = heapq.heappop(queue)
                if currentDistance > distances[currentVertex]:
                    continue
                for neighbor, weight in self.graph[currentVertex]:
                    distance = currentDistance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(queue, (distance, neighbor))
            return distances

    def main():
        g = None
        while True:
            print("\nALGORITHMS")
            print("1. Create a new graph")
            print("2. Add an edge")
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

                if choice == 1:
                    # filename = input("Enter the filename: ")
                    filename = GRAPH_FILE_PATH
                    g = Graph()
                    g.loadFromFile(filename)
                elif choice == 2:
                    directed = input("Is the graph directed? (y/n): ") == "y"
                    g = Graph(directed)

            elif choice == 2:
                u = int(input("Enter the first vertex: "))
                v = int(input("Enter the second vertex: "))
                g.addEdge(u, v)

            elif choice == 3:
                g.displayGraph()

            elif choice == 4:
                v = int(input("Enter the starting vertex: "))
                print()
                tree = dict(g.dijkstra(v))
                for key, value in tree.items():
                    print(f"{key}: {value}")

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
