"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

# Part 1: Graph Class
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        # create a dictionary(hastable) to hold the vertices of the graph
        # adjacent lists {}
        # adjacent matrix []
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # create an empty set to hold the vertices
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # self.vertices = {"A": set("B"), "B": set()}
        
        # add an edge value to the set in each vertex
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # function to calculate all edges of a vertex
        return self.vertices[vertex_id]

    # Part II: Implement Breadth-First Traversal
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #s1
        # make a queue
        q  = Queue()
        # enqueue our start node
        q.enqueue(starting_vertex)
        # make a set to track visited nodes
        visited = set()
        # while queue still has things in items
        while q.size() > 0:
        ## dq from front of the line, this is our current node
            current_node = q.dequeue()
        ## check if we've visited, if not:
            if current_node not in visited:
        ### mark it as visited
                visited.add(current_node)
                print('visited_bft', current_node)
        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### iterate over neighbors,
                for neighbor in neighbors:
        #### add ot queue
                    q.enqueue(neighbor)

        # walk through
        # https://github.com/gmgower/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
        
        '''
        starting_vertex = 1

        q = Queue() # Queue(1),Queue(2),Queue(4,3) Queue(4),Queue(5,4) Queue(5),Queue(7,6,5) Queue(7,6),Queue(3,7,6),Queue(3, 3,7,) Queue(6,1,3),Queue(6,1),Queue(6),Queue(), empty Queue()
        visited = set() # set(1,2,3,4,5,6,7 )

        current_node = 2 # 1, 2, 3, 4, 5,6,7, 3,1,6

        neighbors = set(2) #set(2), set(3,4), set(5). set(6,7), set(3), set(3), set(1,6)
        '''


    # Part 3: Implement Depth-First Traversal with a Stack
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #s2
        # make a stack
        s = Stack()
        # push our starting node onto the Stack
        s.push(starting_vertex)        
        # make a set to track the nodes we've visited
        visited = set()
        
        # as long as our stack isn't empty
        while s.size() > 0:
        ## pop off the top, this is our current nodes
            current_node = s.pop()    
            
        ## check if we have visited this before, and if not:
            if current_node not in visited:
        ### mark it as visited
                visited.add(current_node)
        ### print it(in this case)
                print('visited_dft', current_node)
        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### iterate over neighbors
                for neighbor in neighbors:
        #### and add them to our stack
                    s.push(neighbor)

    '''
    https://raw.githubusercontent.com/LambdaSchool/Graphs/master/objectives/breadth-first-search/img/bfs-visit-order.png
    s = Stack(
        1 #2, 4, 3, 6, 6, 1, 6, 6, 3, 5, 3, 6, 3, empty stack
        #   3     7  3  6  6, 3  6  6  6  3
        #         3     6  3     3  3  3
        #               3
    )
    visited = set() #set(1,2,4,7, 6, 3, 5)
    
    current_node = 1 #2, 4, 7, 1, 6, 3, 5, 3, 6, 3
    neighbors = set(2) # set(2), set(3,4), set(6,7), set(6,1), set(3), set(5), set(3)
    '''

    # Part 4: Implement Depth-First Traversal using Recursion
    def dft_recursive(self, vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        '''
        # Base case:
        # Progress toward the case 
        # call itself
        # don't need a stack, when we end up with no neighbors and will recurs back up
        '''
        if visited == None:
            visited = set()
        # Check if we have been visited
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
        # Base case: if no neighbors
            neighbors = self.get_neighbors(vertex)
            if len(neighbors) == 0:
                return visited
        # If we do have neighbors, iterate over them and recurse for each one
            for neighbor in neighbors:
                self.dfs_recursive(neighbor, visited)

    
    # Part 5: Implement Breadth-First Search
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.

        1. Find the target node 
        2. Keep track of how you got there
        """
        # make a queue
        q = Queue()
        # make a set to track visited
        visited = set()
        # enqueue a PATH TO the starting vertex
        path = [starting_vertex]
        q.enqueue(path)
        ## as long as our queue isn't empty,
        while q.size() > 0:
        ### dequeue from the front of the line, this is our current path: []
            current_path = q.dequeue()
        ### current_node is the last thing in the path
            current_node = current_path[-1]
        ### check if this is the target node
            if current_node == destination_vertex:
        #### if so return 
                return current_path
        ### check if we'vertex visited yet, if not:
            if current_node not in visited:
        #### mark as visited
                visited.add(current_node)
        #### get the current node's neighbors
                neighbors = self.get_neighbors(current_node)
        #### iterate over the neighbors
                for neighbor in neighbors:
        #### add the neighbors to the path_copy
                    neighbor_path = current_path.copy()
                    neighbor_path.append(neighbor)
        #### enqueue the neighbor's path
                    q.enqueue(neighbor_path)
        

    # Part 6: Implement Depth-First Search
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass
   
    ## in dfs_recursive, when we hit our base case, we need to return it all the way up 

    ## When do we want to return from dfs
    ### When we hit the destination vertex:
    # Part 7: Implement Depth-First Search using Recursion
    def dfs_recursive(self, current_vertex, destination_vertex, path = [], visited = None):
        """
        Return a list containing a path from
        current_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()

        if current_vertex not in visited:
            visited.add(current_vertex)

        if len(path) == 0:
            path.append(current_vertex)

        if current_vertex == destination_vertex:
            return path
        
        neighbors = self.get_neighbors(current_vertex)

        for neighbor in neighbors:
            if neighbor not in visited:
                #recurse 
                self.dfs_recursive(neighbor, destination_vertex, path + [neighbor], visited)



       

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print('graph.vertices', graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
