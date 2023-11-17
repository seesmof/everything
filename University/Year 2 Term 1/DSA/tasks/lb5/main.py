"""
- Розробити програмне забезпечення, в якому реалізується алгоритм обходу графу на основі пошуку в глибину. Передбачити, що граф може бути як орієнтований, так і неорієнтований. В процесі пошуку має бути сформовано ліс пошуку в глибину. Для реалізації має використовуватися стек. Програмне забезпечення має бути побудовано на основі відповідного класу, який повинен дозволяти визначати граф, виконувати пошук в глибину, виводити побудований ліс пошуку в глибину, виводити результат обходу тощо.
- Розробити програмне забезпечення, в якому реалізується алгоритм обходу графу на основі пошуку в ширину. Передбачити, що граф може бути як орієнтований, так і неорієнтований. В процесі пошуку має бути сформовано дерево пошуку в ширину. Для реалізації має використовуватися черга. Програмне забезпечення має бути побудовано на основі відповідного класу, який повинен дозволяти визначати граф, виконувати пошук в ширину, виводити побудоване дерево пошуку в ширину, виводити результат обходу тощо.
- У заданому користувачем графі поставлено у відповідність кожній вершині деяке ціле число (може бути як від’ємним, так і додатним). Визначити такі шляхи між парами вершин, які в результаті додавання всіх чисел з кожної вершини дозволяють отримати задане користувачем значення.
- Задано деякий набір арифметичних операцій (наприклад, додати 3, помножити на 2), які можуть бути виконані над операндом. Визначити мінімальний набір операцій, за допомогою якого можна отримати з одного заданого числа а число b. Якщо таке перетворення за допомогою заданого користувачем набору операцій виконати неможливо, то вивести відповідне повідомлення.
- Гемптон-Кортський лабіринт площею у 60 акрів привертає увагу багатьох туристів. Ваш товариш перед тим, як потрапити до одного з таких лабіринтів і продемонструвати свої здібності, вирішив вивчити план лабіринту та запитав Вас про допомогу, яким чином знайти шлях у лабіринті. Змоделюйте лабіринт за допомогою вершин, що відповідають входу в лабіринт, виходу, глухим кутам, всім точкам лабіринту, в яких є можливість вибору шляху, та з’єднань даних вершин ребрами, що відповідають шляхам у лабіринті
"""


def breadthFirstSearch():
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

    def main():
        g = None
        while True:
            print("\nBFS")
            print("1. Create a new graph")
            print("2. Add an edge")
            print("3. Perform breadth-first search")
            print("4. Display breadth-first search tree")
            print("5. Exit")
            choice = int(input(": "))
            print()

            if choice == 1:
                directed = input("Is the graph directed? (y/n): ") == "y"
                g = Graph(directed)
            elif choice == 2:
                u = int(input("Enter the first vertex: "))
                v = int(input("Enter the second vertex: "))
                g.addEdge(u, v)
            elif choice == 3:
                v = int(input("Enter the starting vertex: "))
                g.displayResults(v)
            elif choice == 4:
                v = int(input("Enter the starting vertex: "))
                print()
                tree = dict(g.displayTree(v))
                for key, value in tree.items():
                    print(f"{key}: {value}")
            else:
                break

    main()


def depthFirstSearch():
    from collections import defaultdict

    class Graph:
        def __init__(self, directed=False):
            self.graph = defaultdict(list)
            self.directed = directed

        def addEdge(self, u, v):
            self.graph[u].append(v)
            if not self.directed:
                self.graph[v].append(u)

        def DFS(self, v, visited=None):
            if visited is None:
                visited = set()
            stack = [v]
            while stack:
                vertex = stack.pop()
                if vertex not in visited:
                    visited.add(vertex)
                    print(vertex, end=" ")
                    stack.extend(set(self.graph[vertex]) - visited)
            return visited

        def displayForest(self, v):
            print("Depth-first search forest:")
            self.DFS(v)
            print()

    def main():
        g = None
        while True:
            print("\nDFS")
            print("1. Create a new graph")
            print("2. Add an edge")
            print("3. Perform depth-first search")
            print("4. Display depth-first search forest")
            print("5. Exit")
            choice = int(input(": "))
            print()

            if choice == 1:
                directed = input("Is the graph directed? (y/n): ") == "y"
                g = Graph(directed)
            elif choice == 2:
                u = int(input("Enter the first vertex: "))
                v = int(input("Enter the second vertex: "))
                g.addEdge(u, v)
            elif choice == 3:
                v = int(input("Enter the starting vertex: "))
                g.DFS(v)
                print()
            elif choice == 4:
                v = int(input("Enter the starting vertex: "))
                print()
                g.displayForest(v)
            else:
                break

    main()


def getNumberBySumOfPaths():
    pass


def getMinimalNumberOfOperations():
    pass


def hamptonMaze():
    pass


def menu():
    while True:
        print("\nMake your choice")
        print("1. Show Breadth-First Search demonstration")
        print("2. Show Depth-First Search demonstration")
        print("3. Get the specified number by sum of paths")
        print("4. Get minimal number of operations")
        print("5. Hampton Court Maze")
        print("6. Exit")
        choice = int(input(": "))

        if choice == 1:
            breadthFirstSearch()
        elif choice == 2:
            depthFirstSearch()
        elif choice == 3:
            getNumberBySumOfPaths()
        elif choice == 4:
            getMinimalNumberOfOperations()
        elif choice == 5:
            hamptonMaze()
        else:
            break


menu()
