from collections import defaultdict

from tasks.lb5.main import GRAPH_FILE_PATH


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
        print("\nDFS")
        print("1. Create a new graph")
        print("2. Add an edge")
        print("3. Display graph")
        print("3. Perform depth-first search")
        print("4. Display depth-first search forest")
        print("5. Exit")
        choice = int(input(": "))
        print()

        if choice == 1:
            print("1. Load from file")
            print("2. Create a new graph")
            choice = int(input(": "))

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
            g.DFS(v)
            print()
        elif choice == 5:
            v = int(input("Enter the starting vertex: "))
            print()
            g.displayForest(v)
        else:
            break


main()
