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
# Av = np.round(Av, 3)

# Initialize an empty dictionary for the result
result_dict = {}

# Iterate over the graph and append the node-item and Av value to the result dictionary
j = 0
for node_item in graph:
    result_dict[node_item] = Av[j]
    j += 1

# Print the result dictionary
print(result_dict)

top_5_result_dict= dict(sorted(result_dict.items(), key=lambda item: item[1], reverse=True)[:5])
 

print(top_5_result_dict)