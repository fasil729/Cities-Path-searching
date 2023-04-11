class Node:
    """
    consructs city nodes with adjacency list of the nodes
    """
    def __init__(self, item, latitude = None, longitude = None):
        self.item = item
        self.adjacent_nodes = []
        self.latitude = latitude
        self.longitude = longitude

    def add_adjacent_node(self, node, cost):
        self.adjacent_nodes.append((node, cost))
    def delete_adjacent_node(self, node):
        self.adjacent_nodes = [tup for tup in self.adjacent_nodes if node not in tup]
    

class Graph:
    def __init__(self):
        self.graph = set()
    
    def create_node(self, item, latitude = None, longitude = None):
        """
        create node
        """
        node = Node(item, latitude, longitude)
        return node
    
    def insert_node(self, node):
        """
        inserts the node to the graph
        """
        self.graph.add(node)
    
    def delete_node(self, node):
        """
        delete the node from the graph
        """
        self.graph.remove(node)
        del node
    
    def insert_edge(self, node_A, node_B, cost):
        """
        inserts the edge to beteween node_A and node_B
        """
        node_A.add_adjacent_node(node_B, cost)
        node_B.add_adjacent_node(node_A, cost)
        
    def display(self):
        return self.adjacent_nodes
    def insert_edge_by_item(self, item_A, cost, item_B):
        """
        inserts the edge to beteween item_A and item_B
        """
        node_A = self.search_item(item_A)
        node_B = self.search_item(item_B)
        if node_A and node_B:
            node_A.add_adjacent_node(node_B, cost)
            node_B.add_adjacent_node(node_A, cost)
        if not node_A:
            print(item_A, "is not found in the graph")
        if not node_B:
            print(item_B, "is not found in the graph")
        # print(node_A)

    
    def delete_edge(self, node_A, node_B):
        """
        deletes the edge beteween node_A and node_B
        """
        node_A.delete_adjacent_node(node_B)
        node_B.delete_adjacent_node(node_A)
        

    def search_item(self, item):
        """
        search for item in the graph and return it's node if it exists other wise None
        """
        for node in self.graph:
            if node.item == item:
                return node
        return None

    def has_path(self, src, dst, visited=set()):
      """
      checks if dst is approchable starting from src in given cyclic graph
      """
      if dst in src.adjacent_nodes:
          return True
      visited.add(src)
      res = False
      for neighbour, cost in src.adjacent_nodes:
          if neighbour not in visited:
              res = res or self.has_path(neighbour, dst, visited)
      return res
    
    def __str__(self):
        return "[" + ", ".join([node.item for node in self.graph]) + "]"







