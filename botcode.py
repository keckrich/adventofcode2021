import itertools

# define a class to represent a graph
class Graph:
    def __init__(self):
        # create an empty list of vertices and edges
        self.vertices = []
        self.edges = []
    
    # define a method to add a vertex to the graph
    def add_vertex(self, vertex):
        self.vertices.append(vertex)
    
    # define a method to add an edge to the graph
    def add_edge(self, edge):
        self.edges.append(edge)
    
    # define a method to check if the graph is connected
    def is_connected(self):
        # keep track of the visited vertices
        visited = set()
        
        # perform a depth-first search starting from the first vertex
        stack = [self.vertices[0]]
        while stack:
            vertex = stack.pop()
            visited.add(vertex)
            
            # add the unvisited neighbors of the vertex to the stack
            for neighbor in vertex.neighbors():
                if neighbor not in visited:
                    stack.append(neighbor)
        
        # check if all vertices have been visited
        return len(visited) == len(self.vertices)

# define a class to represent a vertex in the graph
class Vertex:
    def __init__(self, x, y):
        # store the coordinates of the vertex
        self.x = x
        self.y = y
        
        # create an empty list of edges
        self.edges = []
    
    # define a method to add an edge to the vertex
    def add_edge(self, edge):
        self.edges.append(edge)
    
    # define a method to get the neighbors of the vertex
    def neighbors(self):
        # create a list to store the neighbors
        neighbors = []
        
        # add the vertices at the ends of the edges to the list
        for edge in self.edges:
            if edge.start == self:
                neighbors.append(edge.end)
            elif edge.end == self:
                neighbors.append(edge.start)
        
        # return the list of neighbors
        return neighbors

# define a class to represent an edge in the graph
class Edge:
    def __init__(self, start, end):
        # store the vertices at the ends of the edge
        self.start = start
        self.end = end

# define a function that takes a net (represented as a string) and returns
# a graph that represents the net
def net_to_graph(net):
    # create an empty graph
    graph = Graph()
    
    # add the vertices and edges to the graph
    for i in range(len(net)):
        if net[i] == 'x':
            # get the coordinates of the cell
            x, y = i % 3, i // 3
            
            # add the cell as a vertex to the graph
            vertex = Vertex(x, y)
            graph.add_vertex(vertex)
            
            # add the edges that connect the cell to its neighbors
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                # get the coordinates of the neighbor
                nx, ny = x + dx, y + dy
                
                # check if the neighbor is within the bounds of the net
                if nx >= 0 and nx < 3 and ny >= 0 and ny < 3:
                    # get the index of the neighbor
                    ni = nx + 3 * ny
                    
                    # check if the neighbor is an 'x'
                    if net[ni] == 'x':
                        # add the edge that connects the cell to the neighbor
                        edge = Edge(vertex, Vertex(nx, ny))
                        graph.add_edge(edge)
    
    # return the graph
    return graph

# define a function that takes a graph and returns True if the graph is eulerian
# (i.e., if all vertices have even degree and the graph is connected), and False
# otherwise
def is_eulerian(graph):
    # check if all vertices have even degree
    for vertex in graph.vertices:
        if len(vertex.edges) % 2 != 0:
            return False
    
    # check if the graph is connected
    if not graph.is_connected():
        return False
    
    # if the graph passes all the checks, it is eulerian
    return True

# define a function that takes a net (represented as a string) and returns
# True if it can be folded into a cube, and False otherwise
def can_be_folded(net):
    # convert the net into a graph
    graph = net_to_graph(net)
    
    # check if the graph has 8 vertices and 12 edges
    if len(graph.vertices) != 8 or len(graph.edges) != 12:
        return False
    
    # check if the edges form a closed loop
    if not graph.is_eulerian():
        return False
    
    # if the net passes all the checks, it can be folded into a cube
    return True

# define a function that generates all the possible nets for a 1x1x1 cube
def generate_nets():
    # create a list to store the nets
    nets = []
    
    # generate all possible strings of length 9 that contain 6 'x' and any number of '-'
    for net in itertools.product(['x', '-'], repeat=9):
        # check if the net can be folded into a cube, and if it can, add it to the list
        if can_be_folded(net):
            nets.append(net)
    
    # return the list of nets
    return nets

# generate the nets and print them
nets = generate_nets()
for net in nets:
    print(net)