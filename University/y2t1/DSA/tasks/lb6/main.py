"""
- Розробити програмне забезпечення, в якому реалізується алгоритми Дейкстри, Флойда-Уоршелла та Беллмана-Форда на основі створеного відповідного класу для виконання всіх необхідних обчислень, визначення параметрів (в тому числі безпосередньо визначення графа) та отримання та виведення результатів.
- Перелік завдань, які мають бути виконані в процесі роботи над деяким проєктом групою спеціалістів, та їх запланована тривалість визначаються користувачем. Після цього користувач визначає зв’язок між даними завданнями, визначаючи завдання, які мають завершитися до початку кожного завдання. Визначити мінімальний період часу, який знадобиться на виконання проєкту.
- Мапа визначає автомобільні шляхи деякої частини міста Запоріжжя. Деякі вулиці мають односторонній рух, а на деяких можуть зустрічатися затори. Використовуючи дану інформацію та враховуючи обмеження швидкості на вулицях, визначити найкоротший шлях, яким можна дістатися з однієї заданої точки у Запоріжжі до іншої в заданий момент часу.
- Визначити найкоротші шляхи між всіма точками на мапі міста Запоріжжя, використовуючи обмеження попереднього завдання.
"""


GRAPH_FILE_PATH = "D:/code/everything/University/y2t1/DSA/tasks/lb6/input.txt"


def dijkstra():
    from collections import defaultdict, deque

    class Graph:
        def __init__(self, directed=False):
            self.graph = defaultdict(list)
            self.directed = directed

        def addEdge(self, u, v):
            self.graph[u].append(v)
            if not self.directed:
                self.graph[v].append(u)

        def BFS(self, start):
            visited = set()
            queue = deque([start])

            while queue:
                vertex = queue.popleft()
                if vertex not in visited:
                    visited.add(vertex)
                    queue.extend(set(self.graph[vertex]) - visited)

            return visited

        def displayTree(self, start):
            visited = set()
            queue = deque([start])
            tree = defaultdict(list)

            while queue:
                vertex = queue.popleft()
                if vertex not in visited:
                    visited.add(vertex)
                    for neighbor in self.graph[vertex]:
                        if neighbor not in visited:
                            tree[vertex].append(neighbor)
                            queue.append(neighbor)

            return tree

        def displayResults(self, start):
            visited = self.BFS(start)
            print(f"BFS traversal: {visited}")

        def displayGraph(self):
            for key, value in self.graph.items():
                print(f"{key} 🔗 {', '.join(map(str, value))}")

        def loadFromFile(self, filename):
            with open(filename, "r") as file:
                for line in file:
                    u, v = line.strip().split()
                    self.addEdge(int(u), int(v))

    def main():
        g = None
        while True:
            print("\nBFS")
            print("1. Create a new graph")
            print("2. Add an edge")
            print("3. Display graph")
            print("4. Perform breadth-first search")
            print("5. Display breadth-first search tree")
            print("6. Exit")
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
                g.displayResults(v)

            elif choice == 5:
                v = int(input("Enter the starting vertex: "))
                print()
                tree = dict(g.displayTree(v))
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
