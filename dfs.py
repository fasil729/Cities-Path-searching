from graph_Library.city_graph import cities_graph
from graph_Library.graph import Node
import random
class Dfs:
  romania_graph =cities_graph
  def dfs(self,start,goal):
      print("Depth First Search: ")
      print("--------------------------")
      path=set()
      stack=[(start,0)]
      total_distance=0
      
    
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

      

      
      