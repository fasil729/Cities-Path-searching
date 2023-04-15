
import dfs
import bfs
import random
B=bfs.Bfs()
D=dfs.Dfs()
random_cities = random.sample(list(D.romania_graph.graph), 4)
for city1 in random_cities:
    for city2 in random_cities:
        if city1 != city2:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            D.dfs(city1, city2)
            B.bfs(city1, city2)
            print()
       
print("================================================")