"""
You are given an undirected graph with its maximum degree (the degree of a node
is the number of edges connected to the node).
​
You need to write a function that can take an undirected graph as its argument
and color the graph legally (a legal graph coloring is when no adjacent nodes
have the same color).
"""
​
# Definition for a graph node.
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = set()
        self.color = None
​
colors = ['Red', 'Green', 'Yellow', 'Blue', 'Purple']
​
def color_graph(graph, colors):
    # Your code here
    '''
    Inputs: A list of GraphNodes where each node keeps track
    of which other nodes it is connected to, as well as 
    an list of colors.
    Output: Doesn't output anything but it will have updated our 
    graph with a legal coloring (as in, each node will have been
    assigned a color).
​
    1. Pick an arbitrary node and pick an arbitrary color for it 
    2. Go to the nodes connected to this node, and add the color 
       of the current node to a list of 'illegal colors' 
    3. Pick a color for the node that isn't in its list of illegal colors
    '''
    # Most graph problems will likely exhibit O(V * E) since most 
    # of the time you have to access each connection
    # The total number of connections in a graph is number of 
    # vertices * number of edges for each vertex 
    # O(V * (E + C))
    # iterate through our list of GraphNodes
    for node in graph: # O(V) where V is the number vertices/nodes 
        # for each node, we need to figure out what its neighbors'
        # colors are and collect that information as 'illegal colors'
        # how do we want to hold the illegal colors? 
        # We want to know whether some color is in here 
        # Good candidates would be a dict or a set 
        illegal_colors = set()
​
        # O(E) where E is the number of edges/neighbors 
        for neighbor in node.neighbors: 
            # O(1)
            if neighbor.color not in illegal_colors:
                # add the illegal color 
                illegal_colors.add(neighbor.color)
​
        # figure out what colors from our colors list are usable
        # O(C) where C is the number of colors 
        for color in colors:
            # O(1) 
            if color not in illegal_colors:
                # pick this color 
                node.color = color 
                break
​
​
g1 = GraphNode('G1')
g2 = GraphNode('G2')
g3 = GraphNode('G3')
g4 = GraphNode('G4')
g5 = GraphNode('G5')
​
g1.neighbors.add(g2)
g1.neighbors.add(g4)
g1.neighbors.add(g3)
​
g2.neighbors.add(g1)
g2.neighbors.add(g4)
g2.neighbors.add(g5)
​
g3.neighbors.add(g1)
g3.neighbors.add(g5)
g3.neighbors.add(g4)
​
g4.neighbors.add(g1)
g4.neighbors.add(g2)
g4.neighbors.add(g3)
g4.neighbors.add(g5)
​
g5.neighbors.add(g2)
g5.neighbors.add(g3)
g5.neighbors.add(g4)
​
graph = [g1, g2, g3, g4, g5]
​
color_graph(graph, colors)
​
for node in graph:
    print(node.color)
