from graph_Library.city_graph import cities_graph
from graph_Library.graph import Node
import random
class Bfs:
  romania_graph =cities_graph
  def bfs(self,start,goal):
    visited=set()
    queue=[start]
    print(f"The path from {start.item} to {goal.item} is:- ",end='')
    total_disance=0
    while queue!=[]:
      current_node=queue.pop()
      if current_node.item not in visited:
       print(f" {current_node.item}-->",end='')
      
       visited.add(current_node.item)
       if current_node.item==goal.item:
            break;
      
       for neighbour ,cost in  current_node.adjacent_nodes:
        
          
          total_disance+=cost
         
          queue.insert(0,neighbour)
          
    print()
    print(f"Total_Distance: {total_disance}")
         
B=Bfs()

random_cities = random.sample(list(B.romania_graph.graph), 4)
for city1 in random_cities:
    for city2 in random_cities:
        if city1 != city2:
            
            dfs_path = B.bfs(city1, city2)
            print()
# print(B.romania_graph)

    
