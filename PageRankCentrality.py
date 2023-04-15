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

# Create a graph from the adjacency matrix
G = nx.from_numpy_array(A)

# Calculate PageRank centrality of each node
pagerank_centrality = nx.pagerank(G)

# Attach names to PageRank centrality values
pagerank_centrality_with_names = {}
for i, node in enumerate(nodes):
    pagerank_centrality_with_names[node] = pagerank_centrality[i]

print(pagerank_centrality_with_names)

pagerank_centrality_with_names = dict(sorted(pagerank_centrality_with_names.items(), key=lambda item: item[1], reverse=True)[:5])
 

print(pagerank_centrality_with_names)

