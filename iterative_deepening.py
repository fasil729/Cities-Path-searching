from graph_Library.city_graph import cities_graph

def iterative_deepening_search(graph, start, goal):
    depth = 0
    while True:
        result, cost = depth_limited_search(graph, start, goal, depth)
        if result != 'cutoff':
            return result, cost
        depth += 1

def depth_limited_search(graph, node, goal, depth):
    if node == goal:
        return [node.item], 0
    if not node.adjacent_nodes:
        return None, 0
    if depth == 0:
        return 'cutoff', 0
    
    cutoff_occurred = False
    for neighbor, cost in node.adjacent_nodes:
        result, prev_cost = depth_limited_search(graph, neighbor, goal, depth - 1)
        if result == 'cutoff':
            cutoff_occurred = True
        elif result is not None:
            return [node.item] + result, prev_cost + cost
    return 'cutoff' if cutoff_occurred else None, 0


# romania = cities_graph
# bucharest = cities_graph.search_item("Bucharest")
# arad = cities_graph.search_item("Arad")
# print("by iterative deepening", iterative_deepening_search(romania, arad, bucharest))


