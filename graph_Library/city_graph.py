from  .graph import Graph
# import os
# print(os.getcwd())

cities = open("cities.txt", "r")
cities_graph =Graph()

for line in cities:
    arr = line.split()
    # print("arr",arr)
    if len(arr) == 3:
        city, latitude, longitude = arr
    else:
        latitude, longitude = arr[-2:]
        city = ""
        for _ in arr[:-3]:
            city += _ +  " "
        city += arr[-3]
    node = cities_graph.create_node(city, float(latitude), float(longitude))
    cities_graph.insert_node(node)


# manually adding edges beteween the cities in romania from page 83rd of the textbook


cities_graph.insert_edge_by_item('Oradea',151,'Sibiu')
cities_graph.insert_edge_by_item('Oradea',71,'Zerind')
cities_graph.insert_edge_by_item('Zerind',75,'Arad')
cities_graph.insert_edge_by_item('Arad',140,'Sibiu')
cities_graph.insert_edge_by_item('Arad',118,'Timisoara')
cities_graph.insert_edge_by_item('Sibiu',99,'Fagaras')
cities_graph.insert_edge_by_item('Sibiu',80,'Rimnicu Vilcea')
cities_graph.insert_edge_by_item('Timisoara',111,'Lugoj')
cities_graph.insert_edge_by_item('Lugoj',70,'Mehadia')
cities_graph.insert_edge_by_item('Mehadia',75,'Drobeta')
cities_graph.insert_edge_by_item('Drobeta',120,'Craiova')
cities_graph.insert_edge_by_item('Craiova',138,'Pitesti')
cities_graph.insert_edge_by_item('Rimnicu Vilcea',97,'Pitesti')
cities_graph.insert_edge_by_item('Rimnicu Vilcea',146,'Craiova')
cities_graph.insert_edge_by_item('Fagaras',211,'Bucharest')
cities_graph.insert_edge_by_item('Pitesti',101,'Bucharest')
cities_graph.insert_edge_by_item('Bucharest',90,'Urziceni')
cities_graph.insert_edge_by_item('Urziceni',98,'Hirsova')
cities_graph.insert_edge_by_item('Urziceni',142,'Vaslui')
cities_graph.insert_edge_by_item('Hirsova',86,'Eforie')
cities_graph.insert_edge_by_item('Vaslui',92,'Iasi')
cities_graph.insert_edge_by_item('Iasi',87,'Neamt')

# print(cities_graph)


        
