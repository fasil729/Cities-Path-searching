import heapq

def uniform_cost_search(graph, start, goal):
    visited = set()
    queue = [(0, start, [])]
    heapq.heapify(queue)

    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]

            if node == goal:
                return path

            for neighbor, dist in node.adjacent_nodes:
                if neighbor not in visited:
                    total_cost = cost + dist
                    heapq.heappush(queue, (total_cost, neighbor, path))

    return []



    
