"""133. Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node contains:
-> value
-> list of neighbors

Return the cloned graph.
"""

# Solution based on Leetcode Format

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):

    def dfs(self, node, visit):

        # If node is already cloned,
        # return its cloned reference
        if node in visit:
            return visit[node]

        # Create clone of current node
        clon = Node(node.val)

        # Store mapping of original -> cloned node
        visit[node] = clon

        # Traverse all neighboring nodes
        for neigh in node.neighbors:

            # Clone neighbor recursively
            c_neigh = self.dfs(neigh, visit)

            # Connect cloned neighbor
            clon.neighbors.append(c_neigh)

        # Return cloned node
        return visit[node]
        
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        # Return if graph is empty
        if not node:
            return node

        # Start DFS with empty visited dictionary
        c_node = self.dfs(node, {})

        # Return cloned graph
        return c_node


# Time Complexity: O(V + E)
# Space Complexity: O(V)

"""
Theory Explanation:

1. This problem uses DFS + HashMap.

2. Goal:
   Create a completely new graph
   without modifying the original graph.

3. Why HashMap (visit)?

   It stores:
   Original Node  --->  Cloned Node

   This prevents:
   -> Infinite recursion
   -> Cloning same node multiple times

4. DFS Steps:

   -> If node already cloned,
      return cloned node.

   -> Otherwise:
      Create clone.

   -> Store mapping in visit.

   -> Visit every neighbor.

   -> Clone neighbors recursively.

   -> Connect cloned neighbors.

5. Finally:
   Return cloned starting node.

Important Steps:

-> Deep copy means create new nodes.
-> Never reuse original nodes.
-> Dictionary stores original-to-clone mapping.
-> DFS automatically traverses the whole graph.

Key Intuition:

Whenever you visit a node,
create its clone once,
remember it in a dictionary,
then recursively clone and connect all its neighbors.
"""