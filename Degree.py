from graph_Library.city_graph import cities_graph
import networkx as nx
def graph_to_dict(graph):
    graph_dict = {}
    for node in graph.graph:
      edges_dict = {}
      for adjacent_node in node.adjacent_nodes:
          edges_dict[adjacent_node[0].item] = adjacent_node[1]
      graph_dict[node.item] = edges_dict
    return graph_dict
graph_dict = graph_to_dict(cities_graph)
def closeness_centrality(edge):

    G = nx.Graph()
    G.add_edges_from(edge)
    degree_dict = nx.degree_centrality(G)
    for node, degree in degree_dict.items():
        print("Node:", node, "Degree Centrality:", degree)

def ShowEdges(graphs):
        edges = []
        for i in graphs:
            for j in graphs[i]:
                if (j, i) not in edges:
                    edges.append((i, j))
        return edges
edges = ShowEdges(graph_dict)



degree_centrality = closeness_centrality(edges)
print(closeness_centrality)

