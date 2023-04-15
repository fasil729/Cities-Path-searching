import numpy as np
from city_graph import cities_graph

graph = {}

for node in cities_graph.graph:
    neighbours = []
    for neighbour, cost in node.adjacent_nodes:
        neighbours.append(neighbour.item)
    graph[node.item] = neighbours

# Create a list of all unique nodes in the graph
nodes = sorted(graph.keys())

# Create an empty adjacency matrix filled with zeros
A = np.zeros((len(nodes), len(nodes)), dtype=int)

# Fill in the adjacency matrix based on the connections in the graph
for i, node in enumerate(nodes):
    for neighbor in graph[node]:
        j = nodes.index(neighbor)
        A[i, j] = 1

# Convert the matrix to integer type
A = A.astype(int)

# Compute the Katz centrality
alpha = 0.1  # set the damping parameter
n = len(nodes)
I = np.identity(n)
centrality = {}

# Compute (I - alpha * A)^-1 using the numpy.linalg.inv function
M = np.linalg.inv(I - alpha * A)

# Compute the Katz centrality for each node
for i, node in enumerate(nodes):
    # Compute the ith column of (I - alpha * A)^-1
    col_i = M[:, i]
    # Compute the Katz centrality of the ith node
    katz_centrality = alpha * sum(col_i)
    centrality[node] = katz_centrality

# Print the Katz centrality of each node
print(centrality)

centrality = dict(sorted(centrality.items(), key=lambda item: item[1], reverse=True)[:5])
 

print(centrality)