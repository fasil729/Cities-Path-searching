import heapq
import time
import random
import networkx as nxter
from graph_Library.city_graph import cities_graph
def astar(graph,start_node , goal_node):
    start_time = time.time()
    frontier = []
    heapq.heappush(frontier, (0, start_node))
    came_from = {}
    cost_so_far = {}
    came_from[start_node] = None
    cost_so_far[start_node] = 0

    while frontier:
        current = heapq.heappop(frontier)[1]

        if current == goal_node:
            break

        for next_node in current.adjacent_nodes:
            new_cost = cost_so_far[current] + next_node[1]
            if next_node[0] not in cost_so_far or new_cost < cost_so_far[next_node[0]]:
                cost_so_far[next_node[0]] = new_cost
                priority = new_cost + heuristic(goal_node, next_node[0])
                heapq.heappush(frontier, (priority, next_node[0]))
                came_from[next_node[0]] = current


    # Print the shortest path from start node to goal node
    path = []
    current = goal_node
    while current != start_node:
        path.append(current.item)
        current = came_from[current]
    path.append(start_node.item)
    path.reverse()
    print(path)
    
    end_time = time.time()
    
    print( end_time - start_time)
    return len(path)
total_time_taken = 0
num_iterations = 10
def heuristic(a, b):
    return ((a.latitude - b.latitude) ** 2 + (a.longitude - b.longitude) ** 2) ** 0.5

arad = cities_graph.search_item('Arad')
zerind = cities_graph.search_item('Bucharest')
print(astar(cities_graph, arad,zerind ))

# random_cities = random.sample(list(cities_graph.graph), 4)
# print(random_cities)
# for city1 in random_cities:
#     for city2 in random_cities:
#         if city1 != city2:
            
#             astar_path = astar(cities_graph,city1, city2)
#             print(astar_path)
#             print("---------------------------------------------")


# Randomly pic
# random_cities = random.sample(list(cities_graph.graph), 10)
# start_city = random_cities[0]
# goal_city = random_cities[-1]

# print(astar(cities_graph,start_city, goal_city))


