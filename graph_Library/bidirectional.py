from city_graph import cities_graph

def bidirectional_search(graph, start, goal):

    if goal not in graph:
        return None
    
    # initialize forward and backward search queues
    forward_queue = []
    backward_queue = []
    # initialize visited dictionaries for forward and backward search
    forward_visited = {start: None}
    backward_visited = {goal: None}
    # add start and goal nodes to their respective queues
    forward_queue.append(start)
    backward_queue.append(goal)
    
    while forward_queue and backward_queue:
        # get next node from forward and backward queues
        current_forward = forward_queue.pop(0)
        current_backward = backward_queue.pop(0)
        
        # check if current forward node is in backward visited set
        if current_forward in backward_visited:
            # path found, return path
            return path(current_forward, forward_visited, backward_visited)
        # check if current backward node is in forward visited set
        if current_backward in forward_visited:
            # path found, return path
            return path(current_backward, forward_visited, backward_visited)
        
        # add neighbors of current forward node to forward queue and visited dict
        for neighbor in graph[current_forward]:
            if neighbor not in forward_visited:
                forward_queue.append(neighbor)
                forward_visited[neighbor] = current_forward
        
        # add neighbors of current backward node to backward queue and visited dict
        for neighbor in graph[current_backward]:
            if neighbor not in backward_visited:
                backward_queue.append(neighbor)
                backward_visited[neighbor] = current_backward
        
        # check if any common node has been visited in forward and backward search
        common_nodes = set(forward_visited.keys()) & set(backward_visited.keys())
        if common_nodes:
            # path found, return path
            return path(common_nodes.pop(), forward_visited, backward_visited)
                
    # path not found
    return None

def path(node, forward_visited, backward_visited):
    # backtrack from node to start node using visited dict
    path = [node]
    while forward_visited[node] is not None:
        node = forward_visited[node]
        path.insert(0, node)
    # backtrack from node to goal node using visited dict
    node = backward_visited[path[-1]]
    while node is not None:
        path.append(node)
        node = backward_visited[node]
    return path

graph = {}

for node in cities_graph.graph:
    neighbours = []
    for neighbour, cost in node.adjacent_nodes:
        neighbours.append(neighbour.item)
    graph[node.item] = neighbours

start = "Bucharest"
goal = "Arad"

print(bidirectional_search(graph, start, goal))

