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

# Define the adjacency matrix
# A = np.array([
#     [0, 1, 0, 1, 0, 0],
#     [1, 0, 1, 0, 1, 0],
#     [0, 1, 0, 0, 1, 1],
#     [1, 0, 0, 0, 1, 0],
#     [0, 1, 1, 1, 0, 1],
#     [0, 0, 1, 0, 1, 0]
# ])

#Initialize vector v
v = np.ones(A.shape[0])

#Multiply vector v by the adjacency matrix
Av = A.dot(v)

#Normalize Av
Av = Av / np.linalg.norm(Av, ord=2)

# Repeat until convergence
for i in range(100):
    v_new = A.dot(Av)
    v_new = v_new / np.linalg.norm(v_new, ord=2)
    if np.allclose(v_new, Av):
        break
    Av = v_new
Av = np.round(Av, 3)

# The final vector Av is the dominant eigenvector of the adjacency matrix
result = []
j = 0
for i in graph:
    result.append([i, Av[j]])
    j += 1
print(result)
