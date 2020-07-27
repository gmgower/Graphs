from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # create a new graph
    g = Graph()





if __name__ == "__main__":
    ancestors = [(1,3), (2,3), (3,6), (5,6), (5,7), (4,5), (4,8), (8,9), (11,8), (10,1)]

    print(earliest_ancestor(ancestors,3))