from collections import defaultdict
import time
import networkx as nx
import random
from A_Algorithm import astar
from bidirectional import bidirectional_search
from dfs import dfs
from graph_Library.graph import Graph
from iterative_deepening import iterative_deepening_search
from ucs import uniform_cost_search


def create_random_graph(n, p):
    nodes = []
    edges = []
    for i in range(1, n + 1):
        nodes.append(i)
        for j in range(1, n + 1):
            if i != j and random.random() < p:
                edges.append([i, j])
    return nodes, edges










def build_graph(nodes, edges):
    """
    build graph from randomly generated graph
    """
    graph = Graph()
    
    for val in nodes:
        x = random.randint(10, 100)
        y = random.randint(10, 100)
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
        # print("y", y) 
        graph.insert_edge(node_A, node_B, cost)

    return graph    


def test_algorithms(graph):
    random_nodes = random.sample(list(graph.graph), 10)
    # print(random_cities)
    start_time = time.time()
    iter_time = 0
    iter_cost = 0
    ufs_time = 0
    ufs_cost = 0
    a_time = 0
    a_cost = 0
    bi_time = 0
    bi_cost = 0
    dfs_time = 0
    dfs_cost = 0
    for node1 in random_nodes:
        dicti = defaultdict(int)
        # print("here")
        for node2 in random_nodes:
            if node1 != node2:
            # here is test for iterative_deepening_search 
                start_time = time.time()
                result, cost = iterative_deepening_search(graph, node1, node2)
                iter_cost += cost     
                iter_time += time.time() - start_time

            # here is test for uniform_cost_search 
                start_time = time.time()
                result, cost = uniform_cost_search(graph, node1, node2)
                ufs_cost += cost     
                ufs_time += time.time() - start_time
            

            # # here is test for a star search 
            #     start_time = time.time()
            #     result, cost = astar(graph, node1, node2)
            #     a_cost += cost     
            #     a_time += time.time() - start_time
            
            # # here is test for dfs 
            #     start_time = time.time()
            #     result, cost = dfs(graph, node1, node2)
            #     dfs_cost += cost     
            #     dfs_time += time.time() - start_time
                
            # # here is test for biderectional
            #     start_time = time.time()
            #     result, cost = bidirectional_search(graph, node1, node2)
            #     bi_cost += cost     
            #     bi_time += time.time() - start_time
        


                

    print("iteretive_deepining", iter_cost, "km", iter_time, "second")
    print("uniform_cost_search", ufs_cost, "km", ufs_time, "second")
    print("astar", a_cost, "km", a_time, "second")
    print("dfs", dfs_cost, "km", dfs_time, "second")
    print("biderectional_search", bi_cost, "km", bi_time, "second")

size_of_nodes = [10, 20, 30, 40]
probablity_of_edges = [0.2, 0.4, 0.6, 0.8]





for n in size_of_nodes:
    for p in probablity_of_edges:
        nodes, edges = create_random_graph(n, p)
        # print(nodes, edges)
        new_graph = build_graph(nodes, edges)
        # for node in new_graph.graph:
        #     print(node.item, node.adjacent_nodes)
        print()
        print(f"test algorthms for graph with {n} nodes, {p} probablity")
        test_algorithms(new_graph)





        # print(G.nodes, G.edges)


# i = 0
# graph = [node.item = i for node in G.nodes i+=1]
# print(graph[0])
# print("by iterative deepening", iterative_deepening_search(graph, graph[0], graph[2]))