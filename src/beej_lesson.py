class GraphNode:
    def __init__(self, value):
        self.value = value
        self.edge = []
​
a = GraphNode(7)
b = GraphNode(3)
c = GraphNode(1)
d = GraphNode(6)
e = GraphNode(9)
​
a.edge = [b]  # a goes to b
b.edge = [c, d, e]
e.edge = [a]
​
"""
Binary tree pre-order DFT
​
def pre_order(n):
    if n is None:
        return
​
    print(n.value)   # "visit" the node
    pre_order(n.left)  # then visit the left neighbor
    pre_order(n.right)  # then visit the right neighbor
"""
​
def dft_dag_only(n):   # Only works on an acyclic graph
    # visit Node
    print(n.value)
​
    # visit all neighbors
    for e in n.edge:
        dft_dag_only(e)
​
def dft(n):
​
    # Keep track of nodes we've visited to avoid getting in cycles
    visited = set()
​
    def inner(n):
        # If we've been here, bail out
        if n in visited:
            return
    
        # visit the node
        print(n.value)
​
        # add to the visited set
        visited.add(n)
​
        # visit all the neighbors
        for e in n.edge:
            inner(e)
​
    inner(n)
​
dft(a)