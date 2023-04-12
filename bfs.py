from graph_Library.city_graph import cities_graph
from graph_Library.graph import Node
import random
class Bfs:
  romania_graph =cities_graph
  def bfs(self,start,goal):
    visited=set()
    queue=[(start,0)]
    print("Breadth First Search: ")
    print("--------------------------")
    print(f"The path from {start.item} to {goal.item} is:- ",end='')
    total_disance=0
    while queue!=[]:
      current_node=queue.pop()
      if current_node[0].item not in visited:
      
       print(f" {current_node[0].item}-->",end='')
       total_disance+=current_node[1]
      
       visited.add(current_node[0].item)
       if current_node[0].item==goal.item:
            break;
      
       for neighbour ,cost in  current_node[0].adjacent_nodes:
        
          
         
         
          queue.insert(0,(neighbour,cost))
          
    print()
    print(f"Total_Distance: {total_disance}")
    print("Time complexity:", len(visited))
         

# print(B.romania_graph)

    
