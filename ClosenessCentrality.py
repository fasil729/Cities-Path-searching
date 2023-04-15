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

# Convert the adjacency matrix to a graph object
G = nx.DiGraph(A)

# Compute closeness centrality for each node in G and store in a dictionary
closeness_dict = nx.closeness_centrality(G)

# Create a dictionary that maps node indices to node names
node_names = {}
for i, node in enumerate(nodes):
    node_names[i] = node

# Convert closeness centrality dictionary to a dictionary with node names as keys
closeness_dict_with_names = {}
for i, closeness in closeness_dict.items():
    closeness_dict_with_names[node_names[i]] = closeness

print(closeness_dict_with_names)

top_5_closeness_dict_with_names = dict(sorted(closeness_dict_with_names.items(), key=lambda item: item[1], reverse=True)[:5])
 
print("Closeness_centrality values")
print(top_5_closeness_dict_with_names)

