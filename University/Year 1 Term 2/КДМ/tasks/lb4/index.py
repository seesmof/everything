import networkx as nx


def manual_max_flow(G, s, t):
    flow = {}
    for u in G.nodes:
        flow[u] = {}
        for v in G.nodes:
            flow[u][v] = 0
    while True:
        path = bfs(G, s, t, flow)
        if not path:
            break
        df = float("inf")
        for u, v in path:
            df = min(df, G[u][v]["capacity"] - flow[u][v])
        for u, v in path:
            flow[u][v] += df
            flow[v][u] -= df
    max_flow_value = sum(flow[s][v] for v in G.nodes)
    return max_flow_value


def bfs(G, s, t, flow):
    queue = [s]
    paths = {s: []}
    while queue:
        u = queue.pop(0)
        for v in G[u]:
            if G[u][v]["capacity"] - flow[u][v] > 0 and v not in paths:
                paths[v] = paths[u] + [(u, v)]
                if v == t:
                    return paths[v]
                queue.append(v)
    return None


def create_graph():
    G = nx.DiGraph()
    nodes = ['1', '2', '3', '4', '5', '6',
             '7', '8', '9', '10', '11', '12', '13']
    edges = [('1', '2', 11), ('1', '3', 15), ('1', '4', 11), ('1', '5', 15), ('2', '6', 7), ('2', '7', 9), ('3', '6', 4), ('4', '7', 8), ('4', '8', 9), ('4', '9', 4), ('5', '8', 9),
             ('5', '9', 5), ('6', '10', 8), ('7', '10', 13), ('7', '11', 7), ('8', '11', 4), ('8', '12', 4), ('9', '12', 12), ('10', '13', 20), ('11', '13', 10), ('12', '13', 13)]
    G.add_nodes_from(nodes)
    for edge in edges:
        G.add_edge(edge[0], edge[1], capacity=edge[2])
    return G


G = create_graph()

print()
print("Потік:")
for edge in G.edges():
    edge_str = edge[0] + " - " + edge[1] + " -- " + \
        str(G.get_edge_data(edge[0], edge[1])['capacity'])
    print(edge_str)

max_flow_value = manual_max_flow(G, "1", "13")
print("\nПовний потік:", max_flow_value)

max_flow_value, max_flow_dict = nx.maximum_flow(G, '1', '13')
print("\nМаксимальний потік:", max_flow_value)
print()
