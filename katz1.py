# Define the graph as a dictionary of node neighbors

"""_summary_
  
   We then set the parameters for the Katz centrality calculation, including the attenuation factor, damping factor, maximum number of iterations, and convergence tolerance.

We initialize the centrality values for each city to 1, and then iterate until convergence or the maximum number of iterations are reached. In each iteration, we update the centrality value for each city based on the centrality values of its neighboring cities and the attenuation and damping factors.

Finally, we print the centrality values for each city in the graph.
  """





from graph_Library.city_graph import cities_graph
class Katz:
  graph=cities_graph.graph
  for city in graph:
   print(city.item)
  def katz_centrality_cities(self):
    # Set the parameters for the Katz centrality calculation
     alpha = 0.1  # attenuation factor
     beta = 0.5   # damping factor
     max_iterations = 1000  # maximum number of iterations
     tolerance = 1e-6   # tolerance for convergence

     # Initialize the centrality values
     centrality = {node: 1 for node in self.graph}

     # Iterate until convergence or maximum iterations are reached
     for i in range(max_iterations):
       prev_centrality = centrality.copy()
       for node in self.graph:
          centrality[node] = beta * sum([centrality[neighbor] for neighbor,cost in node.adjacent_nodes])
          centrality[node] += alpha
       # Check for convergence
       max_delta = max([abs(centrality[node] - prev_centrality[node]) for node in self.graph])
       if max_delta < tolerance:
          break
        
        
     min_centrality = min(centrality.values())
     max_centrality = max(centrality.values())
     centrality = {node: (centrality[node] - min_centrality) / (max_centrality - min_centrality) for node in centrality}
     
     
     # Print the centrality values for each city
     for city in centrality:
      print(f"City {city.item}: Katz centrality = {centrality[city]}")
K=Katz()
K.katz_centrality_cities()