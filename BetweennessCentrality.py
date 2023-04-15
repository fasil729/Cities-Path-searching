import numpy as np
import networkx as nx
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

# Convert the node index to node name dictionary
index_to_node = {i: node for i, node in enumerate(nodes)}

# Create a graph from the adjacency matrix
G = nx.from_numpy_array(A)

# Compute betweenness centrality for each node in G and store in a dictionary
betweenness_dict = nx.betweenness_centrality(G)

# Convert betweenness centrality dictionary to a dictionary with node names as keys
betweenness_dict_with_names = {}
for i, betweenness in betweenness_dict.items():
    node = index_to_node[i]
    betweenness_dict_with_names[node] = betweenness

print(betweenness_dict_with_names)

betweenness_dict_with_names= dict(sorted(betweenness_dict_with_names.items(), key=lambda item: item[1], reverse=True)[:5])

print(betweenness_dict_with_names)
