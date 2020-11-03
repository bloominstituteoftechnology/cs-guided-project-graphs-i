"""
You are given an undirected graph with its maximum degree (the degree of a node
is the number of edges connected to the node).

You need to write a function that can take an undirected graph as its argument
and color the graph legally (a legal graph coloring is when no adjacent nodes
have the same color).

The number of colors necessary to complete a legal coloring is always one more
than the graph's maximum degree.

*Note: We can color a graph in linear time and space. Also, make sure that your
solution can handle a loop in a reasonable way.*
# Definition for a graph node.
class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

def color_graph(graph, colors):
    # Your code here
"""

# other unrelated problem reviewed:
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

# recursive:

def treePaths(t):
    paths = helper(t, [], [])
    return paths


# will need a helper, to pass in current path as we goo
def helper(t, current_path, paths):
    if note t:
        return
    
    current_path.append(str(t.value))
    

    if not t.left and not t.right:
        path = "->".join(current_path)
        paths.append(path)
    
    if t.left:
        helper(t.left, current_path, paths)
    
    if t.right:
        helper(t.right, current_path, paths)
    
    current_path.pop()
    return paths



# hacky way:
"""
def treePaths(t):
    # we want an array of paths
    paths = []
    # paths from roots --> leaves mean Depth-First
    if t is None:
        return paths
    
    stack = []
    # add the current note to our stack
    stack.append((t, [t.value]))
    current_path = []

    # while the stack is not empty:
    while len(stack) > 0:
        # node = pop off the top of the stack
        node, current_path = stack.pop() # pop off the end
        # "process" it --> add it to the current path we're on
        current_path.append(node.value)
        # add it's children to the stack
        if node.right:
            current_path.append(str(node.right.value))
            stack.append(node.right, current_path)
        if node.left:
            current_path.append(str(node.left.value))
            stack.append(node.left)
        # if node is a leaf: we're done with the current path
        if not node.left and not node.right:
            # we can add it to our array of paths
            path = "->".join(current_path)
            paths.append(path)

        # how do we "backtrack" the current path?
        # recursion or the hacky way, which is to store the current path up to the node in the stack 
    return paths
"""