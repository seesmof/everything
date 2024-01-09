import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Create a graph object
G = nx.Graph()

# Generate a larger range of nodes for a more complex graph and add them.
nodes = range(20)
G.add_nodes_from(nodes)

# Generate a more complex set of edges, connecting each node with next 2 nodes, creating a more complex and layered graph.
edges = [(i, j % 20) for i in range(20) for j in range(i + 1, i + 3)]
G.add_edges_from(edges)

# Apply a colormap to the nodes for a prettier look
cmap = ListedColormap(plt.cm.tab10.colors)

# draw the graph using matplotlib, with parameters for a more visually engaging graphic.
plt.figure(figsize=(10, 10))
nx.draw(
    G,
    with_labels=True,
    node_color=range(20),
    cmap=cmap,
    edge_color="gray",
    linewidths=0.3,
    node_size=500,
    alpha=0.7,
)
plt.title("Complex network")
plt.show()
