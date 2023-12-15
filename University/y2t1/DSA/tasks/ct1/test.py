import networkx as nx

G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(1, 4)
G.add_edge(1, 5)
import matplotlib.pyplot as plt

nx.draw(G, with_labels=True)
plt.savefig("filename.png")
nx.draw_circular(G, with_labels=True)
plt.savefig("filename1.png")
plt.clf()

nx.draw_planar(G, with_labels=True)
plt.savefig("filename2.png")
plt.clf()

nx.draw_random(G, with_labels=True)
plt.savefig("filename3.png")
plt.clf()

nx.draw_spectral(G, with_labels=True)
plt.savefig("filename4.png")
plt.clf()

nx.draw_spring(G, with_labels=True)
plt.savefig("filename5.png")
plt.clf()

nx.draw_shell(G, with_labels=True)
plt.savefig("filename6.png")
plt.clf()
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

pos = nx.spring_layout(G, dim=3, seed=779)
node_xyz = np.array([pos[v] for v in sorted(G)])
edge_xyz = np.array([(pos[u], pos[v]) for u, v in G.edges()])

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.scatter(*node_xyz.T, s=100, ec="w")

for vizedge in edge_xyz:
    ax.plot(*vizedge.T, color="tab:gray")

plt.show()
