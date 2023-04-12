import time
import networkx as nx
import random
from graph_Library.graph import Graph
from iterative_deepening import iterative_deepening_search
from ucs import uniform_cost_search


def build_graph(nodes, edges):
    """
    build graph from randomly generated graph
    """
    graph = Graph()
    x = random.randint(10, 100)
    y = random.randint(10, 100)
    for val in nodes:
        node = graph.create_node(val, x, y)
        graph.insert_node(node)
    for edge in edges:
        node_A = graph.search_item(edge[0])
        node_B = graph.search_item(edge[1])
        # i generate some random cost for edge depending on latitude and longitude
        x = abs(node_A.latitude - node_B.latitude) 
        y = abs(node_A.longitude - node_B.longitude)
        maxi = max(x, y)
        cost = random.randint(maxi, x + y)
        graph.insert_edge(node_A, node_B, cost)

    return graph    



def test_algorithms(graph):
    random_nodes = random.sample(list(graph.graph), 10)
    # print(random_cities)
    start_time = time.time()
    iter_time = 0
    iter_cost = 0
    for node1 in random_nodes:
        # print("here")
        for node2 in random_nodes:
            if node1 != node2:
                start_time = time.time()
                result, cost = uniform_cost_search(graph, node1, node2)

                iter_cost += cost     
                iter_time += time.time() - start_time
                
                # print()
    print("iterative_deepining", iter_cost, iter_time)

size_of_nodes = [10, 20, 30, 40]
probablity_of_edges = [0.2, 0.4, 0.6, 0.8]

for n in size_of_nodes:
    for p in probablity_of_edges:
        G = nx.gnp_random_graph(n, p)
        new_graph = build_graph(G.nodes, G.edges)
        for node in new_graph.graph:
            print(node.item, node.adjacent_nodes)
        print(f"test algorthms for graph with {n} nodes, {p} probablity")
        test_algorithms(new_graph)





        # print(G.nodes, G.edges)

# i = 0









# graph = [node.item = i for node in G.nodes i+=1]
# print(graph[0])
# print("by iterative deepening", iterative_deepening_search(graph, graph[0], graph[2]))
