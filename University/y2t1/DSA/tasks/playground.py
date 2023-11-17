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
