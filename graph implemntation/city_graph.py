from graph import Node, Graph
# import os
# print(os.getcwd())

cities = open("cities.txt", "r")
cities_graph = Graph()
for line in cities:
    arr = line.split()
    print(arr)
    if len(arr) == 3:
        city, latitude, longitude = arr
    else:
        latitude, longitude = arr[-2:]
        city = ""
        for _ in arr[:-2]:
            city += " " + _
    node = cities_graph.create_node(city, float(latitude), float(longitude))
    cities_graph.insert_node(node)
print(cities_graph)

        
