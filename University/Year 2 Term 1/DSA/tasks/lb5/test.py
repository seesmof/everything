class Graph:
    def __init__(self, directed=False):
        self.adj = {}
        self.directed = directed

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def dfs(self, start):
        stack = [start]
        parent = {start: None}
        result = []
        while stack:
            v = stack.pop()
            result.append(v)
            for u in self.adj[v]:
                if u not in parent:
                    parent[u] = v
                    stack.append(u)
        return result, parent

    def display_dfs_forest(self, parent):
        roots = []
        for v in parent:
            if parent[v] is None:
                roots.append(v)
        for r in roots:
            print(r)
            self.display_dfs_subtree(r, parent, 1)

    def display_dfs_subtree(self, v, parent, level):
        for u in self.adj[v]:
            if parent[u] == v:
                print("  " * level, u)
                self.display_dfs_subtree(u, parent, level + 1)

    def bfs(self, start):
        queue = [start]
        parent = {start: None}
        result = []
        while queue:
            v = queue.pop(0)
            result.append(v)
            for u in self.adj[v]:
                if u not in parent:
                    parent[u] = v
                    queue.append(u)
        return result, parent

    def display_bfs_tree(self, parent):
        roots = []
        for v in parent:
            if parent[v] is None:
                roots.append(v)
        for r in roots:
            print(r)
            self.display_bfs_subtree(r, parent, 1)

    def display_bfs_subtree(self, v, parent, level):
        children = []
        for u in self.adj[v]:
            if parent[u] == v:
                children.append(u)
        children.sort()
        for u in children:
            print("  " * level, u)
            self.display_bfs_subtree(u, parent, level + 1)

    def find_paths(self, start, end, target):
        path = [start]
        sum = values[start]
        self.find_paths_helper(start, end, target, path, sum)

    def find_paths_helper(self, v, end, target, path, sum):
        if v == end:
            if sum == target:
                print(path)
        elif sum < target:
            for u in self.adj[v]:
                if u not in path:
                    path.append(u)
                    sum += values[u]
                    self.find_paths_helper(u, end, target, path, sum)
                    path.pop()
                    sum -= values[u]


g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")
g.add_edge("E", "F")
g.add_edge("F", "G")

result, parent = g.dfs("A")
print(f"\nDFS order: {result}")
g.display_dfs_forest(parent)

result, parent = g.bfs("A")
print(f"\nBFS order: {result}")
g.display_bfs_tree(parent)

values = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7}
