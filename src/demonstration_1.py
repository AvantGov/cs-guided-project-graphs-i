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
"""


"""
UNDERSTAND: 




"""


# Definition for a graph node.
class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

def color_graph(graph, colors):
    # Your code here



"""
returning the tree paths problem: 

UNDERSTAND: 
- we want an array of paths 
- we will be doing a depth first search recursively to solve this 
    - add the current node to the stack 
    
    - while the stack is not empty, 
        - node = pop off the top of the stack 
        - process it --> add it to the current path we are on (need a var to store this)
        - add it's children to the stack 
    
    - we know a current path is complete when the current node is a leaf (no children)
        - we can then add it to the array of paths 

    - we will then need to backtrack up the tree in order to reach the next possible path 
        - we can accomplish this by stroing the current path up to the current node in the stack 



"""

def tree_path(tree):
    paths = []

    if tree is None:
        return paths
    
    stack = []

    stack.append((tree, [str(tree.value)]))
    current_path = []

    while len(stack) > 0:
        node = stack.pop(0)

        current_path.append(node.value)

        if node.right:
            current_path.append(str(node.right.value))
            stack.push((node.right, current_path))
            current_path.pop()

        if node.left:
            current_path.append(str(node.left.value))
            stack.push((node.left, current_path))
            current_path.pop()
        


    if not node.left and not node.right:
        path = "->".join(current_path)
        paths.append(path)
    
    return paths