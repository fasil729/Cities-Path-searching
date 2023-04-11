from graph_Library.city_graph import cities_graph
from graph_Library.graph import Node
import random
class Dfs:
  romania_graph =cities_graph
  def dfs(self,start,goal):
      path=[]
      stack=[start]
      total_distance=0
      print(f"Path from {start.item} to {goal.item} is :- ",end="")
      while stack!=[]:
          current_node=stack.pop()
          if current_node.item not in path:
              path.append(current_node.item)
              print(f"{current_node.item}-->",end=" ")
              if current_node.item==goal.item:
                  break
              for neighbour,cost in current_node.adjacent_nodes:
                  stack.append(neighbour)
              total_distance+=cost
                  
      print()
      print(f"Total Distance: {total_distance}")
D=Dfs()
random_cities = random.sample(list(D.romania_graph.graph), 4)
for city1 in random_cities:
    for city2 in random_cities:
        if city1 != city2:
            
            dfs_path = D.dfs(city1, city2)
            print()
      
      