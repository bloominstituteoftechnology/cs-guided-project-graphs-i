'''
Object representation for a graph
''' 
# define a class that represents a graph node 
class GraphNode:
    def __init__(self, value=None):
        self.value = value 
        # some way to store connections to other GraphNodes 
        self.connections = [] 
​
g1 = GraphNode()
g2 = GraphNode()
g3 = GraphNode()
g4 = GraphNode()
​
g1.connections.append(g2)
g1.connections.append(g3)
g1.connections.append(g4)
​
# The most common graph representation 
# is the adjacency list
​
# Used to represent a directed graph
directed_graph = [
    [1, 2], # Node 0 
    [3],    # Node 1 
    [3],    # Node 2 
    [4],    # Node 3 
    [],     # Node 4 
]
​
# Write a function to print out each graph 
# node and all of the graph node's connections 
def print_graph(graph):
    '''
    Input: graph represented as an adjacency list
    Output: prints out each graph node with its connections
    ''' 
    # iterate with a for loop 
    # since we want access to both the index as well as the 
    # value at that index in the adjacency list, use `enumerate`
    for node, connections in enumerate(graph):
        print(f'Graph Node {node} is connected to {connections}')
​
print_graph(directed_graph)