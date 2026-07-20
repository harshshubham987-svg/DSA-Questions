'''
684. Redundant Connection

A graph started as a Tree.

A Tree has:

-> Connected graph
-> No cycle

One extra edge
is added.

Return the edge
that creates the cycle.

If multiple answers exist,
return the edge
that appears last
in the input.

Example 1:

Input:

[[1,2],
 [1,3],
 [2,3]]

Output:

[2,3]

Example 2:

Input:

[[1,2],
 [2,3],
 [3,4],
 [1,4],
 [1,5]]

Output:

[1,4]
'''

# Solution


class DSU:

    def __init__(self, n):

        # Total number of nodes
        self.n = n

        # Initially every node
        # is its own leader
        self.leader = [i for i in range(n + 1)]

        # Every component
        # starts with size 1
        self.size = [1] * (n + 1)

    # Find Ultimate Parent
    def find(self, x):

        # Node is its own leader
        if self.leader[x] == x:
            return x

        # Path Compression
        self.leader[x] = self.find(self.leader[x])

        return self.leader[x]

    # Union By Size
    def union(self, x, y):

        # Find ultimate parents
        u = self.find(x)
        v = self.find(y)

        # Cycle detected
        if u == v:
            return [x, y]

        # Attach smaller tree
        # below larger tree
        if self.size[u] >= self.size[v]:

            self.leader[v] = u

            self.size[u] += self.size[v]

        else:

            self.leader[u] = v

            self.size[v] += self.size[u]


def main():

    # Edge list
    edges = [[1,2],
             [2,3],
             [3,4],
             [1,4],
             [1,5]]

    # Find maximum node number
    n = edges[0][0]

    for i in range(len(edges)):
        for j in range(len(edges[0])):

            if edges[i][j] > n:
                n = edges[i][j]

    # Create DSU
    d = DSU(n)

    # Process every edge
    for edg in edges:

        u = edg[0]
        v = edg[1]

        # Try merging components
        val = d.union(u, v)

        # If both nodes already belong
        # to the same component,
        # this edge is redundant
        if val is not None:
            return val


# Main function execution
if __name__ == "__main__":
    print(main())


# Time Complexity: O(N × α(N))
# Space Complexity: O(N)


'''
Theory Explanation:

1. This problem uses

Disjoint Set Union (DSU)

also called

Union Find.

2. Initially,

every node
belongs to
its own component.

Example:

1

2

3

4

Parent:

1
2
3
4

3. Process every edge
one by one.

Example:

1 -- 2

Merge

Now,

1 and 2
belong to
the same component.

4. For every edge,

find the ultimate parent
of both nodes.

Case 1:

Parents are different.

Example:

1 -- 2

Parent(1) = 1

Parent(2) = 2

Merge them.

No cycle exists.

Case 2:

Parents are already same.

Example:

1 ----- 2
 \     /
  \   /
    3

When processing

2 -- 3

both nodes
already belong
to the same component.

Adding this edge
creates a cycle.

Therefore,

this edge
is the redundant connection.

5. Union By Size

Always attach
the smaller tree

below

the larger tree.

This keeps
the tree balanced.

6. Path Compression

Whenever find()
is called,

every node
directly points

to the ultimate parent.

Future searches
become almost O(1).

Example:

Before:

4

↓

3

↓

2

↓

1

After find(4):

4

↓

1

3

↓

1

2

↓

1

7. Since edges
are processed
in input order,

the first edge
that connects
two nodes already
in the same component

is returned.

For this problem,

that is also
the required answer.

Example:

1--2

2--3

3--4

1--4

When

1--4

is processed,

1 and 4
already belong
to the same component.

Hence,

[1,4]

is the redundant edge.

Important Steps:

-> Initially every node is its own parent.
-> Process edges one by one.
-> Find ultimate parent of both nodes.
-> If parents are different, perform Union.
-> If parents are same, a cycle is found.
-> Return that edge immediately.
-> Use Union By Size and Path Compression for efficiency.

Key Intuition:

A tree never contains a cycle.

While adding edges,

if two nodes
already belong
to the same connected component,

adding another edge
between them

must create a cycle.

That edge
is the redundant connection.

Pattern:

Graph
+
Disjoint Set Union (Union Find)
+
Union By Size
+
Path Compression
=
Cycle Detection in an Undirected Graph
'''