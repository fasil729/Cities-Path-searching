from graph_Library.city_graph import cities_graph
from graph_Library.graph import Node
import random
<<<<<<< HEAD
class Dfs:
  romania_graph =cities_graph
  def dfs(self,start,goal):
      print("Depth First Search: ")
      print("--------------------------")
      path=set()
      stack=[(start,0)]
      total_distance=0
      
=======
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

           

>>>>>>> f83ca3281f5888de8d80d4905bc9ae51d0c494c3
    
      print(f"Path from {start.item} to {goal.item} is :- ",end="")
      while stack!=[]:
          current_node=stack.pop()
          
          if current_node[0].item not in path:
              path.add(current_node[0].item)
              print(f"{current_node[0].item}-->",end=" ")
              total_distance+=current_node[1]
              if current_node[0].item==goal.item:
                  break
              
              for neighbour,cost in current_node[0].adjacent_nodes:
                  if neighbour.item not in path:
                 
                   stack.append((neighbour,cost))
              
                   
                   
      print()
      print(f"Total Distance: {total_distance}\n")
      print("Time complexity:", len(path))

      

      
      