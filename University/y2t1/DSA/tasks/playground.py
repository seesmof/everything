from collections import defaultdict

GRAPH_FILE_PATH = "D:/code/everything/University/y2t1/DSA/tasks/lb5/input.txt"


class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def findPaths(self, start, targetSum):
        visited = set()
        path = []
        self._findPathsHelper(start, targetSum, visited, path)

    def _findPathsHelper(self, vertex, targetSum, visited, path):
        visited.add(vertex)
        path.append(vertex)

        if sum(path) == targetSum:
            print(path)

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._findPathsHelper(neighbor, targetSum, visited, path)

        path.pop()
        visited.remove(vertex)

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
        print("4. Find paths to target sum")
        print("5. Exit")
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
            targetSum = int(input("Enter the target sum: "))
            g.findPaths(v, targetSum)

        else:
            break


main()
