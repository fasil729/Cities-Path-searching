from time import sleep
from graph_Library.city_graph import cities_graph
import heapq

def uniform_cost_search(graph, start, goal):
    visited = set()
    queue = [(0, start, [])]
    heapq.heapify(queue)

    while queue:
        (cost, node, path) = heapq.heappop(queue)
        # print("cost",start.item, goal.item, queue, "in ufs")
        if node not in visited:
            # sleep(3)
            visited.add(node)
            path = path + [node.item]

            if node == goal:
                return path, cost

            for neighbor, dist in node.adjacent_nodes:
                # print("here")
                if neighbor not in visited:
                    total_cost = cost + dist
                    heapq.heappush(queue, (total_cost, neighbor, path))

    return [], 0


# romania = cities_graph
# bucharest = cities_graph.search_item("Bucharest")
# arad = cities_graph.search_item("Arad")
# print(uniform_cost_search(romania, arad, bucharest))


    
