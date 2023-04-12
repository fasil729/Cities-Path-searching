from graph_Library.city_graph import cities_graph
import random
# romania_file = open("romania.txt", "r")
romania_graph = cities_graph

# for line in romania_file:
#     city1, city2, distance = line.split()
#     print( city1,city2, distance)
#     romania_graph.add_edge(city1, city2, weight=int(distance))
# # print(romania_graph.nodes,romania_graph.edges)

def dfs(start, goal):
    stack = [(start, [start])]
    print(f"Path From {start} to {goal} is:- {start}",end="")
    while stack:
        (vertex, path) = stack.pop()
        
        for next_node in vertex.adjacent_nodes:
            
            if next_node not in path:
                print(f"-->{next_node}",end="")
               
                if next_node == goal:
                    return path + [next_node]
                else:
                    stack.append((next_node, path + [next_node]))

           

    
