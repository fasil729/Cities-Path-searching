def bulidUndirectedGraph(edges):
    """
    builds undirected graph using the given edges
    """
    graph = defaultdict(list)
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)
    return graph

def connected_components_count(graph):
    """
    Count connected compenents in graph
    """
    visited = set()
    count = 0
    for node in graph:
      if node in visited:
        continue
      traverse(graph, node, visited)
      count += 1
    return count
  
 # needs to fix what to be returned 
def traverse(graph, src, visited):
  """traverse through the graph using dfs traverse"""
  if src in visited:
    return   #visited
  visited.add(src)
  for neighbour in graph[src]:
    traverse(graph, neighbour, visited)
  return      #visited    

def largest_component(graph):
    """
    find largest compenent of the graph interms of
    the number of nodes the compenent contains
    
    """
    visited = set()
    count = 0
    for node in graph:
      if node in visited:
        continue
      count = max(count, num_of_nodes(graph, node, visited))
    return count
  
 
def num_of_nodes(graph, src, visited):
  """ calculates number of nodes in given graph compenent"""
  if src in visited:
    return 0
  visited.add(src)
  res = 1
  for neighbour in graph[src]:
    res += num_of_nodes(graph, neighbour, visited)
  return res

def shortest_path(edges, node_A, node_B):
  """ 
  calculates the shortest num of edges from node_A to node_B and return it if 
  node_B exitst otherwise return -1
  """
  graph = bulidUndirectedGraph(edges)
  visited = set()
  start = [[node_A, 0]]
  queue = deque(start)
  print(graph)
  while queue:
    
    curr, dist = queue.popleft()
    print(queue, curr, visited, graph[curr])
    if curr == node_B:
      return dist
    if curr in visited:
      continue
    
    visited.add(curr)
    for neighbour in graph[curr]:
      queue.append([neighbour, dist + 1])
  return -1