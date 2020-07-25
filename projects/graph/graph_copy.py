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
                print('visited', current_node)
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

        q = Queue() # Queue(1),Queue(2),Queue(4,3) Queue(4),Queue(5,4) Queue(5),Queue(7,6,5) Queue(7,6),Queue(3,7,6),Queue(3, 3,7,) Queue(6,1,3),Queue(6,1),Queue(6),Queue()
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
        pass

    # Part 4: Implement Depth-First Traversal using Recursion
    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        '''
        # Base case:
        # Progress toward the case 
        # call itself
        '''
        # base case:
        # if visited doesn't exits
        if not visited:
        # create a new set
            visited = set()
        # and add the starting vertex
        visited.add(starting_vertex)
        print(starting_vertex)

        # loop through all the vertices,
        for vert in self.vertices[starting_vertex]:
        # and if it hasn't been visited,
            if vert not in visited:
        # recursively call DFT
                self.dft_recursive(vert, visited)
    
    # Part 5: Implement Breadth-First Search
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        

    # Part 6: Implement Depth-First Search
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #s2
        # make a stack 
        s = Stack()
        # push our starting node onto the stack
        s.push(starting_vertex)
        # make a set to track the nodes we've visited
        visited = set()

        # as long as our stack isn't empty
        while s.size() > 0:
        ## pop off the top, this our current nodes
            current_node = s.pop()

        ## check if we we have visited this before, and if not:
            if current_node not in visited:
        ### mark it as visited
                visited.add(current_node)
        ### print it (in this case)
                print(current_node)
        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### iterate over neighbors
                for neighbor in neighbors:
        #### and add them to our Stack
                    s.push(neighbor)
        '''
        https://raw.githubusercontent.com/LambdaSchool/Graphs/master/objectives/breadth-first-search/img/bfs-visit-order.png

        s = Stack(
            1
        )

        visited = set(1,2)

        current_node = 2
        neighbors = set(2)
        '''

    # Part 7: Implement Depth-First Search using Recursion
    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # base case
        # if the visited set and the path list are None
        # create new versions,
        # else use the versions passed in as parameters
        if not visited:
            visited = set()
        if not path:
            path = []

        # add the starting vertex to the visited set,
        # and add the vertex passed in to any vertices already in the list
        visited.add(starting_vertex)
        path = path + [starting_vertex]

        # if the starting vertex and the destination are the same,
        # return the path
        if starting_vertex == destination_vertex:
            return path

        # else loop through all remaining vertices,
        # if the vertex hasn't been visited, 
        # call dfs recursive and if there is a path,
        # return it
        for vert in self.vertices[starting_vertex]:
            if vert not in visited:
                path_copy = self.dfs_recursive(vert, destination_vertex, visited, path)
                if path_copy:
                    return path_copy 

        # if we get here, there was no path so return None
        return None
        

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
