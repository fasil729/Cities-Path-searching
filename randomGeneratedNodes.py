import random
import math
import heapq
# import matplotlib.pyplot as plt
import time

# import numpy as np

def create_graph(n, p):
    # Initialize an empty graph
    graph = {i: [] for i in range(n)}
    
    # Create edges between nodes with probability p
    for i in range(n):
        for j in range(i+1, n):
            if random.random() <= p:
                graph[i].append(j)
                graph[j].append(i)
    
    return graph
# def generate_random_graph(n, p):
#     """Generate a random undirected graph with n nodes and probability p of edge creation."""
#     graph = {node: set() for node in range(n)}
#     for i in range(n):
#         for j in range(i + 1, n):
#             if random.random() < p:
#                 graph[i].add(j)
#                 graph[j].add(i)
#     return graph

def create_random_coordinates(n):
    # Generate n random coordinates with values between 0 and 1
    coordinates = []
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        coordinates.append((x, y))
    return coordinates

def compute_distance(coord1, coord2):
    # Compute the Euclidean distance between two coordinates
    x1, y1 = coord1
    x2, y2 = coord2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def compute_heuristic(graph, coordinates):
    # Compute the heuristic function for each node
    heuristic = {}
    for node in graph:
        # Use A* algorithm to compute the shortest distance to all other nodes
        frontier = [(0, node)]
        visited = set()
        while frontier:
            cost, curr_node = heapq.heappop(frontier)
            if curr_node not in visited:
                visited.add(curr_node)
                heuristic[node] = max(heuristic.get(node, 0), cost)
                for neighbor in graph[curr_node]:
                    neighbor_coord = coordinates[neighbor]
                    new_cost = cost + compute_distance(coordinates[curr_node], neighbor_coord)
                    heapq.heappush(frontier, (new_cost, neighbor))
    return heuristic

def dfs(graph, start, end):
    # Depth-first search algorithm to find a path from start to end node
    visited = set()
    path = []
    stack = [start]
    while stack:
        curr_node = stack.pop()
        if curr_node == end:
            path.append(curr_node)
            return path
        if curr_node not in visited:
            visited.add(curr_node)
            path.append(curr_node)
            for neighbor in reversed(graph[curr_node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    return None

def bfs(graph, start, end):
    # Breadth-first search algorithm to find a path from start to end node
    visited = set()
    path = []
    queue = [(start, [start])]
    while queue:
        curr_node, curr_path = queue.pop(0)
        if curr_node == end:
            return curr_path
        if curr_node not in visited:
            visited.add(curr_node)
            for neighbor in graph[curr_node]:
                if neighbor not in visited:
                    queue.append((neighbor, curr_path + [neighbor]))
    return None



# Set the number of nodes and probabilities of edges
n_values = [10, 20, 30, 40]
p_values = [0.2, 0.4, 0.6, 0.8]

# Define the algorithms to use




# def time_algorithm(graph, algorithm_func, node_pairs):
#     times = []
#     for start, end in node_pairs:
#         start_time = time.monotonic()
#         path = algorithm_func(graph, start, end)
#         end_time = time.monotonic()
#         times.append(end_time - start_time)
#     return np.mean(times)

# algorithm_funcs = [bfs, dfs]
# n_values = [10, 20, 30, 40]
# p_values = [0.2, 0.4, 0.6, 0.8]

# results = {}
# for algorithm_func in algorithm_funcs:
#     results[algorithm_func.__name__] = {}
#     for n in n_values:
#         results[algorithm_func.__name__][n] = {}
#         for p in p_values:
#             graph = generate_random_graph(n, p)
#             node_pairs = random.sample(list(graph.keys()), 10)
#             times = []
#             for i in range(5):
#                 time_taken = time_algorithm(graph, algorithm_func, node_pairs)
#                 times.append(time_taken)
#             results[algorithm_func.__name__][n][p] = {"time": np.mean(times), "path_lengths": []}
#             for start, end in node_pairs:
#                 path = algorithm_func(graph, start, end)
#                 if path:
#                     results[algorithm_func.__name__][n][p]["path_lengths"].append(len(path) - 1)
#                 else:
#                     results[algorithm_func.__name__][n][p]["path_lengths"].append(None)





# Create 16 random graphs and compute their heuristic functions
for n in n_values:
    for p in p_values:
        # Create the graph and random coordinates
        graph = create_graph(n, p)
        coordinates = create_random_coordinates(n)
        
        # Compute the heuristic function
        heuristic = compute_heuristic(graph, coordinates)
        
        # Select 10 random node pairs to find paths
        node_pairs = []
        for i in range(10):
            start, end = random.sample(range(n), 2)
            node_pairs.append((start, end))
        
        # Find paths using DFS and BFS algorithms
        for start, end in node_pairs:
            dfs_path = dfs(graph, start, end)
            bfs_path = bfs(graph, start, end)
            print(f"Graph with n={n} and p={p}:")
            print(f"Start node: {start}, End node: {end}")
            print(f"DFS path: {dfs_path}")
            print(f"BFS path: {bfs_path}")
            print("--------------------")
